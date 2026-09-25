#!/usr/bin/env python3
"""Reproduce the September dataset audit. Researcher-only: reads public gold.

No model calls. Never expose this script, its inputs, or outputs to evaluated agents.
"""
import argparse
from collections import Counter
import csv
from decimal import Decimal, ROUND_HALF_UP
import hashlib
import json
from pathlib import Path
import sqlite3
import urllib.request

REPO = Path(__file__).resolve().parents[1]
D = Decimal


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line]


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def quantize(value, places):
    return str(value.quantize(D(10) ** -places, rounding=ROUND_HALF_UP))


def audit(root):
    result = {}
    base = root / 'dabstep/data'
    dev = read_jsonl(base / 'tasks/dev.jsonl')
    test = read_jsonl(base / 'tasks/all.jsonl')
    fees = json.loads((base / 'context/fees.json').read_text(), parse_float=D)
    payments = read_csv(base / 'context/payments.csv')
    selected = [f for f in fees if f['card_scheme'] == 'GlobalCard'
                and f['is_credit'] in (True, None)]
    mean = sum(f['fixed_amount'] + D(f['rate']) * 10 / 10000
               for f in selected) / len(selected)
    # A second implementation filters and aggregates independently in SQLite.
    sql = sqlite3.connect(':memory:')
    sql.execute('create table fees (scheme text, credit integer, fixed real, rate integer)')
    sql.executemany('insert into fees values (?, ?, ?, ?)', [
        (f['card_scheme'], f['is_credit'], float(f['fixed_amount']), f['rate'])
        for f in fees])
    sql_mean = sql.execute("select avg(fixed + rate * 10.0 / 10000) from fees "
                           "where scheme = 'GlobalCard' and (credit = 1 or credit is null)").fetchone()[0]
    gold = next(x['answer'] for x in dev if x['task_id'] == '1273')
    assert quantize(mean, 6) == gold == f'{sql_mean:.6f}'
    strict = [f for f in selected if f['is_credit'] is True]
    strict_mean = sum(f['fixed_amount'] + D(f['rate']) / 1000 for f in strict) / len(strict)
    result['dabstep'] = {
        'default_tasks': len(test), 'default_levels': dict(Counter(x['level'] for x in test)),
        'default_nonempty_answers': sum(bool(x.get('answer')) for x in test),
        'dev_tasks': len(dev), 'dev_levels': dict(Counter(x['level'] for x in dev)),
        'dev_nonempty_answers': sum(bool(x.get('answer')) for x in dev),
        'payment_rows': len(payments), 'payment_columns': len(payments[0]),
        'merchants': dict(sorted(Counter(x['merchant'] for x in payments).items())),
        'fee_rows': len(fees),
        'empty_list_counts': {k: sum(f[k] == [] for f in fees)
                              for k in ['account_type', 'merchant_category_code', 'aci']},
        'reference_1273': {'matched_fee_rows': len(selected),
                           'sum_fixed_eur': str(sum(f['fixed_amount'] for f in selected)),
                           'sum_rate': sum(f['rate'] for f in selected),
                           'decimal_answer': quantize(mean, 6),
                           'sqlite_answer': f'{sql_mean:.6f}', 'public_gold': gold,
                           'wrong_null_exclusion_answer': quantize(strict_mean, 6)},
    }
    sql.close()

    queries = read_csv(root / 'longda/benchmark.csv')
    herd = {}
    for name in ['herd2023.csv', 'short2023.csv']:
        rows = read_csv(root / 'longda/HERD/data' / name)
        source = [x for x in rows if x['questionnaire_no'] in ('01.a', '01.g')]
        assert len(source) == len({(x['inst_id'], x['questionnaire_no']) for x in source})
        totals = {q: sum(D(x['data']) for x in source if x['questionnaire_no'] == q)
                  for q in ['01.a', '01.g']}
        sql = sqlite3.connect(':memory:')
        sql.execute('create table responses (q text, value real)')
        sql.executemany('insert into responses values (?, ?)',
                        [(x['questionnaire_no'], float(x['data']) if x['data'] else None) for x in rows])
        for q, value in totals.items():
            assert sql.execute('select sum(value) from responses where q=?', (q,)).fetchone()[0] == value
        sql.close()
        herd[name] = {'rows': len(rows), 'institutions': len({x['inst_id'] for x in rows}),
                      'federal_thousand_usd': str(totals['01.a']),
                      'total_thousand_usd': str(totals['01.g'])}
    full = herd['herd2023.csv']; short = herd['short2023.csv']
    all_total = (D(full['total_thousand_usd']) + D(short['total_thousand_usd'])) / 1000
    all_federal = (D(full['federal_thousand_usd']) + D(short['federal_thousand_usd'])) / 1000
    full_federal = D(full['federal_thousand_usd']) / 1000
    long_gold = {x['internal_id']: x['answer'] for x in queries if x['survey'] == 'HERD'}
    assert quantize(all_total, 0) == long_gold['1']
    assert quantize(full_federal, 0) == long_gold['3']
    # This reproduces the inspected upstream numerical threshold, not our proposed scorer.
    wrong_scope_passes = abs(all_federal - D(long_gold['3'])) <= max(D(long_gold['3']) * D('.05'), D(1))
    result['longda'] = {'queries': len(queries),
                         'survey_counts': dict(sorted(Counter(x['survey'] for x in queries).items())),
                         'herd_files': herd,
                         'herd_total_million_usd': str(all_total),
                         'herd_all_federal_million_usd': str(all_federal),
                         'herd_standard_federal_million_usd': str(full_federal),
                         'herd_q1_public_gold': long_gold['1'], 'herd_q3_public_gold': long_gold['3'],
                         'wrong_population_passes_upstream_tolerance': wrong_scope_passes}

    base = root / 'repos/AgenticDataBench/AgenticDataBench'
    tasks = read_jsonl(base / 'testbed/tasks/dev.jsonl')
    dbpath = root / 'hf/shawnzzzh/AgenticDataBench/datasets/financial/pub_fin_data.sqlite'
    db = sqlite3.connect(dbpath.resolve().as_uri() + '?mode=ro', uri=True)
    q = """select sum(i.net_profit), sum(b.total_equity), sum(b.total_assets), count(*)
        from dim_company c join fact_income_statement i using(company_id)
        join fact_balance_sheet b using(company_id,period_date,period_type,report_type)
        where i.period_date='2024-12-31' and i.period_type='FY' and i.report_type='合并报表'
        and c.industry_name=(select industry_name from dim_company where stock_name='金山办公')"""
    profit, equity, assets, n = db.execute(q).fetchone()
    # Separate Python joins/aggregation, rather than rerunning the SQL expression.
    db.row_factory = sqlite3.Row
    companies = [dict(x) for x in db.execute('select * from dim_company')]
    industry = next(x['industry_name'] for x in companies if x['stock_name'] == '金山办公')
    ids = {x['company_id'] for x in companies if x['industry_name'] == industry}
    def eligible(x):
        return (x['company_id'] in ids and x['period_date'] == '2024-12-31'
                and x['period_type'] == 'FY' and x['report_type'] == '合并报表')
    income = [dict(x) for x in db.execute('select * from fact_income_statement') if eligible(x)]
    balance = [dict(x) for x in db.execute('select * from fact_balance_sheet') if eligible(x)]
    assert {x['company_id'] for x in income} == {x['company_id'] for x in balance}
    pprofit = sum(D(str(x['net_profit'])) for x in income)
    pequity = sum(D(str(x['total_equity'])) for x in balance)
    passets = sum(D(str(x['total_assets'])) for x in balance)
    answer = [quantize(pprofit / pequity * 100, 2), quantize(pprofit / passets * 100, 1)]
    assert answer == [f'{profit / equity * 100:.2f}', f'{profit / assets * 100:.1f}']
    gold = read_csv(base / 'testbed/gold/financial_236/result.csv')[0]
    assert answer == [gold['行业总体ROE'], gold['行业总体ROA']]
    result['agenticdatabench'] = {'public_tasks': len(tasks),
        'financial_tasks': sum(x['domain'] == 'financial' for x in tasks),
        'financial_236': {'matched_companies': n, 'roe_percent': answer[0], 'roa_percent': answer[1],
                          'sql_python_and_public_gold_agree': True},
        'income_statement_source_coverage': list(db.execute(
            'select count(*),count(source) from fact_income_statement').fetchone())}
    db.close()
    tasks = read_jsonl(root / 'hf/HKUSTDial/DataSpace/data/tasks.jsonl')
    text_only = [x for x in tasks if not x['pdf_files'] and not x['video_files']]
    result['dataspace'] = {'tasks': len(tasks), 'public_references': sum(x['reference_available'] for x in tasks),
        'workspaces_without_pdf_or_video': len(text_only),
        'public_references_without_pdf_or_video': [x['task_id'] for x in text_only if x['reference_available']]}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=REPO / '.scratch/benchmark-audit')
    parser.add_argument('--download', action='store_true', help='Fetch pinned public audit sources (~82 MB)')
    parser.add_argument('--output', type=Path, help='Optional researcher-only JSON report')
    args = parser.parse_args()
    manifest = json.loads((REPO / 'benchmark/source-manifest.json').read_text())
    for entry in manifest['files']:
        p = args.root / entry['path']
        if not p.is_file() and args.download:
            with urllib.request.urlopen(entry['url'], timeout=90) as stream:
                data = stream.read()
            if hashlib.sha256(data).hexdigest() != entry['sha256']:
                raise ValueError(f'Download checksum mismatch: {entry["path"]}')
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
        data = p.read_bytes()
        if len(data) != entry['bytes'] or hashlib.sha256(data).hexdigest() != entry['sha256']:
            raise ValueError(f'Input checksum mismatch: {entry["path"]}')
    result = {'audit_date': manifest['audit_date'], 'verified_source_files': len(manifest['files']),
              'scope': 'Offline feasibility checks, not model experiments or human gold audit.', **audit(args.root)}
    output = json.dumps(result, indent=2, ensure_ascii=False) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
    print(output)


if __name__ == '__main__':
    main()
