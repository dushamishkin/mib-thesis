# Data and benchmark selection

Audit date: 25 September 2026. Research recommendation, not a frozen experiment or
supervisor-approved dataset choice. Read with the [approved design](../proposal/research-design.md).

**Recommendation: use a carefully specified DABstep derivative for the core pilot.**
Its public synthetic payment tables, fee schedules and manuals offer the best balance
of business relevance, executable checking, experimental control and preparation cost.
AgenticDataBench finance is the strongest alternative. LongDA HERD is the preferred
later transfer check. Business Bench offers useful reconciliation-task patterns.

The audit screened 18 benchmark families, inspected actual releases for six leading
candidates, and reproduced selected reference calculations in three datasets. This is
a broad targeted review, not an exhaustive systematic review or validation of every
task. No paid model calls, benchmark submissions or evaluated agent trials ran.

## Evidence and method

- [Pilot specification](pilot-spec.md): 12 proposed base tasks and one concrete
  document-pair specification. The complete suite is not implemented or gold-audited.
- [Source manifest](source-manifest.json): 76 downloaded files with pinned URLs,
  revisions, sizes and SHA-256 hashes. Includes public gold; researcher access only.
- [Audit evidence](audit-evidence.json): measured counts and calculation checks.
- [Reproduction script](../scripts/audit_benchmark_inputs.py): standard-library-only
  downloader and checker. Two implementations are a computational cross-check, not
  independent human review or an experimental V2 intervention.

Searches covered named candidates, documentation-grounded analytics, financial
table/text QA, executable data-science benchmarks, business procedures, and recent
rule-drift/ambiguity benchmarks. Representative searches: `DABstep dataset license
documentation`, `LongDA benchmark github`, `data analysis benchmark business rules
documentation 2026`, `LiveSQLBench business rule drift`, `DataSpace benchmark`,
`AgenticDataBench`, `DataCrossBench dataset code release`, and `KramaBench`.
Search discovery was followed by primary papers, author repositories, dataset cards,
licenses, task files and selected raw inputs. Third-party rankings are not evidence
for the recommendation.

Hard requirements are public usable inputs, a documented reuse route, meaningful
rules outside the question, executable references, fixed tables across document
variants, and no mandatory OCR, proprietary data or paid database hosting. Among
eligible candidates, prefer business relevance, manageable adaptation and several
calculation/rule families. No leaderboard score enters selection. Unresolved rights
or gold semantics are gates that other strengths cannot offset.

## Comparative screen

“Public” describes access, not unrestricted reuse. Repository software licenses do
not automatically resolve underlying data rights. Lower-priority candidates received
a primary-source screen rather than the complete file audit of the leading six.

| Candidate and primary source | Inputs, labels and reuse evidence | Fit and disposition |
|---|---|---|
| [DABstep](https://huggingface.co/datasets/adyen/DABstep) | CSV/JSON and Markdown; 450 default questions with blank answers, 10 labeled dev tasks; CC BY 4.0 dataset | Best compact core foundation, with explicit derivative semantics and new gold |
| [LongDA](https://huggingface.co/datasets/Yiyang-Ian-Li/LongDA) | 505 public questions/answers, 17 surveys; mixed formats and manuals; CC BY card header versus MIT benchmark statement | HERD transfer subset; full suite adds survey/parsing complexity |
| [AgenticDataBench](https://github.com/AgenticDataBench/AgenticDataBench) | 246 public tasks and gold artifacts; Apache-2.0 release; source-specific provenance still needs checking | Strongest alternative: financial statements and metric manuals |
| [LiveSQLBench](https://github.com/bird-bench/livesqlbench) | Base-Lite 270 and Large-v1 480 task records; HKB rules; SQL/test values blank, full labels by email; data CC BY-SA 4.0, code MIT | Strong semantic-rule comparator and SQL alternative; access/setup and ShareAlike affect adaptation |
| [DataSpace](https://github.com/HKUSTDial/DataSpace) | 410 input manifests, 60 public references; MIT release; text/PDF/video | Excellent evaluator reference; limited immediately eligible business tasks |
| [Business Bench](https://github.com/erphq/business-bench) | 187 desk definitions, generated inputs, references/checks, MIT; separate build track | Useful reconciliation extension; remove workbook-format confounds |
| [Spider 2.0](https://github.com/xlang-ai/Spider2) | Enterprise databases, external knowledge, executable evaluation; MIT repository; full Lite requires cloud-access steps | Strong related work; local subset possible, full setup not preferred |
| [BIRD](https://bird-bench.github.io/) | Databases, questions, external evidence and SQL; public development resources | SQL control; task-specific evidence can shortcut document discovery; source reuse not audited here |
| [InfiAgent-DABench](https://github.com/InfiAgent/InfiAgent) | CSV analysis; Apache-2.0 code, CC BY-NC 4.0 data in author README | Computational baseline, less native documentary rule structure |
| [DA-Code](https://github.com/yiyihum/DA-Code) | Wrangling/analysis/modeling; sample inputs and separate source/gold downloads; MIT repository | Broader coding objective; underlying data permissions need checking |
| [DSBench](https://github.com/LiqiangJing/DSBench) | ModelOff/Kaggle tasks; research/noncommercial restrictions and original creator rights | Business realism, but mixed terms and modalities increase preparation cost |
| [FinQA](https://github.com/czyssrs/FinQA) | Financial tables/text, answers and programs; public/private test files; MIT repository | Small evaluator sanity checks, limited organizational document structure |
| [TAT-QA](https://github.com/NExTplusplus/TAT-QA) | Financial table/text QA, public test gold; dataset CC BY 4.0, code MIT | Arithmetic/units checks; short QA context weak as main MAS workload |
| [DataCross](https://arxiv.org/abs/2601.21403v1) | Paper describes 200 cross-modal tasks and executable references | Relevant prior art; verified author data/code release not located in this search; OCR outside scope |
| [KramaBench](https://github.com/mitdbg/Kramabench) | Data lakes, reference pipelines and intermediate-task evaluation | Useful methodology; scientific workflows; reuse authorization not established from landing page |
| [DiscoveryBench](https://github.com/allenai/discoverybench) | Hypothesis discovery; [ODC attribution license](https://github.com/allenai/discoverybench/blob/main/LICENSE) | Scientific discovery is a different evaluation target |
| [SOP-Bench](https://github.com/amazon-science/sop-bench) | Procedures, generated tools/data and reference evaluation | Procedure-following comparison, but shifts focus toward operational actions; full data audit deferred |
| [Ambig-DS](https://arxiv.org/abs/2605.09698v1) | Prediction-target and evaluation-objective ambiguity suites | Important positioning reference; different ambiguity mechanism |

## DABstep: recommended core foundation

Inspected dataset revision `7ea3b597f6e3093ee6463276a1d1de19ada58c67` and
[paper v1](https://arxiv.org/html/2506.23719v1). Tasks draw on financial workflows,
but `payments-readme.md` explicitly calls the released transactions synthetic. Preserve
that distinction in the thesis.

The seven context files total about 24.2 MB: payments (138,236 rows, 21 columns, five
merchants, all 2023), 1,000 fee rules, merchant metadata, acquirer-country and MCC
mappings, and two Markdown documents. No OCR or hosted database is required. Measured
task counts are 72 easy and 378 hard default records, all with blank answers; development
has three easy and seven hard records with answers. Submissions and task-score files
must not be mined for our hidden gold.

Business semantics include basis-point units, fee eligibility, monthly windows, fraud
definitions and merchant/transaction relationships. These support controlled variants
that distinguish correct computation from correct rule selection. The compact corpus
leaves resources for strong controls and repeated runs.

There are real specification issues to resolve. The manual defines `null` as
unrestricted, while list fields often contain empty arrays: 720 account-type, 127 MCC
and 112 ACI entries. Empty-array semantics are less explicit. Section 5's fraud-ratio
wording is ambiguous; section 7 specifies fraudulent amount over total amount. The
guide is dated 2024 while payments are from 2023. Some illustrative categories differ
from released values. Overlapping fees, threshold inclusivity, refusal handling and
multiple-match aggregation need explicit contracts. These are input observations,
not model failures. See the
[pinned manual](https://huggingface.co/datasets/adyen/DABstep/blob/7ea3b597f6e3093ee6463276a1d1de19ada58c67/data/context/manual.md).

For development task 1273, Python Decimal and an independently written SQLite
filter/aggregate both recover EUR 0.120132, matching public gold. The calculation uses
144 rules, summed fixed components of EUR 10.25 and summed rate coefficients of 7,049.
Excluding null-valued credit rules gives EUR 0.117667 instead. This checks one family,
not the full monthly fee engine or every official answer.

The [pinned LICENSE](https://huggingface.co/datasets/adyen/DABstep/blob/7ea3b597f6e3093ee6463276a1d1de19ada58c67/LICENSE)
specifies CC BY 4.0. Preserve attribution/notices, link the license, identify changes
and avoid implying endorsement, following the
[license terms](https://creativecommons.org/licenses/by/4.0/). Keep upstream files
unchanged, including embedded notices. Clearly marked scenario documents will define
our derivative rules. Scores on that suite are not official DABstep scores.

## AgenticDataBench: strongest alternative

Inspected code `d110b63ff70dfc775fb7eabe8caaaed28c3868d6`, data
`3b0ac3fde63fd615de92bf70c1dd93b73f92d92f`, selected
[paper v1 sections](https://arxiv.org/html/2607.01647v1), financial manuals and one
SQLite database. The public file contains 246 tasks, including 24 in the financial
domain; the authors identify another 98 withheld tasks. The 24 financial tasks are
not all from one database or independent calculation families.

The 1.56 MB `pub_fin_data.sqlite` has 174 companies and 1,563 rows in each of three
financial statement tables. Its Chinese manual specifies CNY units, consolidated
versus parent-only reports, composite join keys and percentage formatting. English
questions can refer to Chinese names/documents. Task `financial_236` joins annual
consolidated statements for one industry: separate SQLite and Python computations
match public gold, ROE 4.49% and ROA 2.6%, over five companies. It is promising for
period, consolidation-scope, units and denominator variants.

The [data release](https://huggingface.co/datasets/shawnzzzh/AgenticDataBench) and code
declare Apache-2.0. However, its public-report provenance statement lacks row-level
links: all 1,563 income-statement `source` fields are null. Other domains include
fintech business datasets and heterogeneous upstream collections. Audit selected
origins/terms before redistribution; a release license alone does not establish every
domain's eligibility. Prefer DABstep initially for its simpler English fixed corpus.
Promote this subset if DABstep cannot supply enough sound task families. Keep language
and source access identical across treatments. `skills`, `eval_func` and gold paths
are researcher metadata, not agent-visible context.

## LongDA: transfer through HERD

Inspected dataset `1365b6ab65bba290c83c7bcbb2c9bcb70a79ddd4`, code
`02cbd7929efc6594a053f2c10480a89ceb56662c`, and
[v2 construction, evaluation and limitations](https://arxiv.org/html/2601.02598v2).
The older `EvilBench/LongDA` URL redirects to `Yiyang-Ian-Li/LongDA`.
All 505 queries have public answers in a declared test split. Our derivative family
split must be constructed separately. Original evaluation groups questions by
publication and permits context reuse within blocks; do not inherit unequal exposure
in our task-local-memory comparison.

HERD provides 18 research-finance questions. We downloaded both FY2023 CSVs and the
27-page guide, reading the population, units and format sections and visually checking
PDF pages 8–9. There are 664 standard-form and 250 short-form institutions. Expenditure
records are in thousands of dollars and the populations are stored separately. The
[official survey](https://ncses.nsf.gov/surveys/higher-education-research-development/2023)
and [publication table](https://www.ncses.nsf.gov/pubs/nsf25313/table/1) anchor provenance.

Python and SQLite sums recover USD 108,841.148 million in total R&D, rounding to gold
108,841. Standard-form federal funding is 59,603.993 million, rounding to question 3's
59,604. Including short-form institutions instead gives 59,678.935 million. This wrong
scope still passes the inspected
[upstream metric](https://github.com/Yiyang-Ian-Li/LongDA/blob/02cbd7929efc6594a053f2c10480a89ceb56662c/metric.py),
which allows the larger of 5% of gold or 1.0 in answer units. List matching can award
partial element credit. Our primary scorer must instead check rule applicability and
task-specific precision, with complete-answer correctness separate from diagnostics.

The card has a licensing inconsistency: CC BY 4.0 in its header, MIT for code/benchmark
in its licensing section, and a blanket public-domain description of survey materials.
Do not generalize this to every source. Prefer the
[official HERD public-use distribution](https://ncses.nsf.gov/explore-data/microdata/higher-education-research-development)
for transfer inputs; resolve benchmark-annotation terms before publishing adaptations.
Use verified text exports, with answer-bearing publications and `benchmark.csv` outside
agent access. This involves public institutional data, not participant recruitment.

## Other leading alternatives

**LiveSQLBench.** Inspected both task files and credit/cross-border HKB examples. Credit
rules include composite scores with explicit weights and caps. SQL/test fields exist
but their public values are empty: schema availability is not gold availability.
The authors' email access route was not invoked. Large-v1 explicitly covers business
rule drift; this is essential prior art, not evidence for our V2 × C1 interaction.
Dataset [ShareAlike terms](https://creativecommons.org/licenses/by-sa/4.0/) require
deliberate derivative-release packaging. Base-Lite SQLite is a lower-infrastructure
option. No database environment or official SQL evaluation was reproduced.

**DataSpace.** Inspected manifests, reference list, license and evaluator source. Of
410 tasks, 60 have public references. Only 21 workspaces contain neither PDF nor video;
five have references, all with patient-record questions. This conservative format
filter does not prove visual evidence is necessary for every excluded task. We did
not download the 2.88 GB archive or validate all workspaces. Its complete-table,
typed evaluator is useful prior art, but the immediately eligible business subset is
too small to displace the recommended foundation.

**Business Bench.** Counted 187 desk definitions and read bank-reconciliation task,
generator/check source, CSV and source email. The email explicitly gives the bank
record authority for a disputed check amount; prior-month outstanding items add a
temporal dependency. This is a strong C1 pattern. However, the task also scores XLSX
formulas/presentation. Adaptation would change its evaluation target. Task YAML exposes
trap descriptions and expected values and cannot be passed wholesale to agents.
The release's validation notes disclose regenerated-byte differences for 28 other
fixtures: pin supplied bytes rather than assume seed equivalence. The MIT release is
recent and its vendor develops one evaluated system. No workbook gold or model results
were independently reproduced here.

## Implications for the research claim

Documents in analytics, semantic validation with memory, executable business evaluation
and business-rule drift all have close precedents. In particular,
[AgenticData v2](https://arxiv.org/html/2508.05002v2) describes five evaluation datasets
and component ablations including validation and memory. Its bank dataset is not a
source to adopt under our constraints. The inspected sections do not establish our
controlled factorial with fixed-table rule variants; that is a bounded reading result,
not proof of global novelty.

LongDA v2 still explicitly excludes cross-year documentation drift in its limitations.
LiveSQLBench prevents generalizing that gap to the whole literature. Ambig-DS also
makes task ambiguity an existing research direction. Position our contribution around
separate/joint V2 and C1 effects, matched information/resources, rule applicability and
incorrect final acceptance. A combined win alone does not identify interaction.

Only selected paper sections and source files were read; no paper's model experiments
were reproduced. New sources are recorded by primary URL, not invented BibTeX keys.
Zotero and the versioned project bibliography were not changed by this audit.

## Reproduction and next action

From the repository root:

```bash
python3 scripts/audit_benchmark_inputs.py --download --output .scratch/benchmark-audit/recheck.json
python3 scripts/check_repo.py
git diff --check
```

Only the 76 pinned audit files (~82 MB) are fetched. Existing files must match hashes;
mismatches fail rather than update silently. Without `--download`, checking is offline.
The script installs nothing, executes no downloaded code and calls no models. The
committed evidence JSON records checks; downloads/extracted documents are scratch.

Next: implement the [12-base-task development specification](pilot-spec.md), with
independent computations and an author audit of semantic contracts. Before any model
run, freeze variants/family partitions, implement filesystem/network gold isolation,
and agree model/budget, roles, C1 schema, V2 withholding and resource controls. Full
monthly fee totals remain deferred until overlap, thresholds and population rules are
unambiguous. Main-study task counts must follow variance/cost evidence, not observed
treatment wins.
