# Experiments

No runs yet. Implement only after the data audit and budget agreement.
Core conditions: V0, V2, C1, V2+C1; strong single-agent and resource controls.
See [research design](../proposal/research-design.md) for definitions and statistical units.

## Provisional student-budget model plan

10 October 2026. Author stresses affordability; no numeric budget or paid run is approved.
The recommendation is one affordable base model in all core conditions and controls,
with a stronger-model replication only if justified and separately budgeted. Do not use
a stronger verifier than solver in the primary factorial or weaken the single-agent
baseline. Model selection is conditional on calibration showing useful task performance,
not favourable treatment effects. A one-model study limits model-level generalisation.

Initial comparison candidate: [GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna),
documented function calling/structured outputs and Standard short-context prices of
USD 0.10 per million input tokens and USD 0.50 per million output tokens.
Optional stronger-model check: [GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol),
USD 2.00 input and USD 10.00 output per million tokens in the same tier/context regime.
Official model/pricing pages inspected 10 October 2026; recheck before runs and confirm
account availability. Pin/document the supported version identifier; do not invent a
dated snapshot when the provider only exposes an alias.

Use local restricted Python/SQL tools, compact tool returns and bounded agent turns.
Do not put whole tables into prompts or pay for hosted analysis/search services in
the core experiment. Equal information access must survive any context-size savings.
Reset task memory, including cross-task provider state, without treating cost caching
as permission to share task answers. Log reasoning output as billable consumption.

The following are token-cost scenarios, not measured usage or power calculations.
Token totals cover the complete run across agents, checker passes and corrections.
Assume Standard short-context rates, uncached inputs, no explicit cache writes, no
paid hosted tools and no regional surcharge; taxes/local compute are excluded.

| Scenario | Total input / billable output per run | Luna cost/run | Sol cost/run |
|---|---|---|---|
| Bounded compact run | 100,000 / 20,000 tokens | USD 0.020 | USD 0.400 |
| Larger workflow | 500,000 / 50,000 tokens | USD 0.075 | USD 1.500 |

The larger workflow's aggregate input can span multiple calls; these prices assume
each call stays below the provider's long-context threshold. Reasoning/retries can
increase billable totals; context-tier, cache-write and regional premiums must be
included when applicable. Discounts are not assumed.

For the proposed development pilot, 28 instances × six configurations × three
repetitions = 504 runs: Luna token costs would be USD 10.08 or USD 37.80 in the two
scenarios. Three repetitions are illustrative, not a selected run count. A possible
main-study scenario of 100 base tasks × two variants × six configurations × three
repetitions = 3,600 runs would cost USD 72 or USD 270 on Luna, before reserve and
other costs. Neither scenario establishes adequate statistical precision or an
authorised campaign.

Recommend discussing a staged ceiling: at most USD 5 for small calibration, then
at most USD 20 for the pilot if measured usage permits completion. These are suggested
limits, not spending permission. If projected cost exceeds the ceiling, stop and
revise the scope transparently; do not discard failures or silently drop controls.
The main-study budget follows observed token use and independent-family requirements.
Strong-model replication must run all comparison conditions on a prespecified subset,
not only our preferred method or tasks selected after observing wins.

Implement a local cumulative spending guard before any paid run: reserve the worst-case
allowed next call, bound aggregate tokens/turns/retries, stop before the agreed total
and record interrupted/failed runs. A dashboard warning alone is insufficient. This
guard is proposed; no harness or guard has been implemented yet.

### China-based Qwen option

Author requests a cheaper Chinese option and notes the thesis is being written in
China. Prefer evaluating **qwen3.7-flash-2026-07-15 through Alibaba Cloud Model Studio,
Beijing**, before choosing a primary provider. This is a candidate, not an approved
model or paid launch. Its [official model page](https://help.aliyun.com/zh/model-studio/qwen3-7-flash)
documents the dated snapshot, function calling and structured output support.
This API model should not be confused with a downloadable open-weight Qwen release.

The [official Chinese pricing table](https://help.aliyun.com/zh/model-studio/model-pricing)
was checked 10 October 2026. Standard Beijing prices per million tokens:

| Candidate and per-request input tier | Input CNY | Output CNY |
|---|---|---|
| qwen3.7-flash-2026-07-15, at most 32K | 0.2 | 0.8 |
| Same model, above 32K and at most 256K | 0.6 | 2.4 |
| qwen-flash-2025-07-28, at most 128K | 0.15 | 1.5 |

For aggregate 100K input/20K billable output per complete run, Qwen3.7-Flash costs
CNY 0.036 when all calls stay in the first tier, or CNY 0.108 if all tokens use the
second tier: CNY 18.144 or 54.432 for the illustrative 504-run pilot. The older
Qwen-Flash would cost CNY 0.045/run or 22.68 for the same workload in its first tier.
Do not assume the smallest input price yields the cheapest overall run.
These estimates exclude tax/other services and do not assume promotional quotas,
caching or batch discounts. Thinking output is billable; tiers apply per request,
not to aggregate run input. International-region prices differ. We have not tested
account activation, payment, endpoint access or these models on our tasks.

Before paid calibration, agree a ceiling in CNY, confirm the actual account/region,
freeze thinking mode and version, and compare code/tool competence on a small
development sample without using treatment wins as the selection criterion. Keep
one base model across conditions and controls. Local open-weight inference is an
alternative only if suitable existing hardware and serving stability are confirmed;
no GPU rental or hardware purchase is recommended now. Main-study costs remain open.

Each retained run needs a manifest recording code commit, task/source versions and checksums,
model/provider/version, prompts, condition, caps, seeds where supported, repeats, timestamp,
tool/environment dependencies, failures/timeouts, tokens, latency and cost. Record actual
usage, not only caps. Preserve raw evidence and checksums in durable storage; commit compact
manifests/summaries here and keep bulk output in ignored artifacts/ or runs/.
Do not store irreplaceable evidence only in .scratch/. Document retrieval locations without secrets.
