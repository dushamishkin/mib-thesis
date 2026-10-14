# DABstep leaders and the rationale for a bounded MAS study

Checked 11 October 2026. This is a targeted leaderboard/source/implementation inspection,
not reproduced scores, a systematic review or an allegation about entrants. Proposal
artifacts are unchanged. Source cards below distinguish public descriptions, inspected
code and unresolved information. Generated bibliography was not edited or synced.

## Targeted follow-up — 14 October 2026

For the proposal's source-selection explanation, re-read the public Gradio configuration:
28 validated entries; NVIDIA, DataPilot and DS-STAR remain first, second and fifth by
hard accuracy at 89.95%, 87.57% and 45.24%. This is a check of ranking metadata, not a
new implementation audit or score reproduction. Reopened their technical descriptions,
MAST v3 and the two single/multi-agent comparison papers to support the simpler framing.
Detailed 11 October reading/code limits below remain in force.

## Scope and leaderboard snapshot

Read the public [leaderboard](https://huggingface.co/spaces/adyen/DABstep) through its
[app](https://adyen-dabstep.hf.space/) and public Gradio configuration. Observed 28
validated rows and 2,234 unvalidated rows. These counts are a dated snapshot, not stable
benchmark properties. Screened every validated row's metadata; investigated the six
entries above AgenticData on hard accuracy plus AgenticData. Also screened the distinct
linked unvalidated systems above AgenticData, grouping repeated submissions. Entries
without an identifiable implementation/article cannot be architecture-classified.
This is not a claim to have read papers/code for every anonymous unvalidated submission.

| Validated hard-rank | Entry | Easy % | Hard % | Listed model | Architecture evidence |
|---|---|---:|---:|---|---|
| 1 | NVIDIA KGMON Data Explorer | 87.50 | 89.95 | Claude Haiku 4.5 | One tool-calling runtime loop; separate preparation/review phases |
| 2 | DataPilot | 86.11 | 87.57 | Qwen3 | Main ReAct agent delegates competing hypotheses to subagents, per author description |
| 3 | gg-agent-gpt5-1104-1 | 88.89 | 62.96 | Doubao, despite entry name | No repo link; topology and exact configuration unknown |
| 4 | CambioML energent.ai DS Agent | 94.44 | 57.67 | GPT-5 | Product link; topology/code for this submission unconfirmed |
| 5 | DS-STAR | 87.50 | 45.24 | Gemini-2.5-Pro | Paper explicitly defines analyzer/planner/coder/verifier/router agents |
| 6 | Amity DA Agent v0.1 | 80.56 | 41.01 | Gemini-2.5-Pro preview | Author describes Planner–Executor–Feedbacker MAS |
| 7 | AgenticData | 94.44 | 40.48 | Qwen3 | Paper describes profiling/planning/validation/memory agents |

Scores are easy/hard accuracies, not two repetitions or two architectures. The native
450-task split is 72 easy/378 hard. Six validated entries exceed AgenticData on hard
accuracy; not all dominate it on easy accuracy. Leaderboard dates are submission fields,
not proof of when a method was invented. Scores alone do not control model, tools,
preparation, retries, human engineering or compute.

The [official instructions](https://adyen-dabstep.hf.space/) distinguish validated
and unvalidated submissions and close new validation requests ahead of v2. Unvalidated
does not mean invalid; a high score or an official scoring receipt alone does not prove
architecture, absence of leakage or faithful reproducibility. Answer exact-match does
not directly evaluate rule provenance, reviewer coverage or communication quality.

## NVIDIA: preparation is part of the system

**Primary description:** [NVIDIA author article](https://huggingface.co/blog/nvidia/nemo-agent-toolkit-data-explorer-dabstep-1st-place),
13 March 2026. Learning creates reusable functions and examples from labelled dev tasks;
fast inference uses Haiku; separate offline reflection/group-consistency supplies later
insights. It discusses insights from test questions: that is test-informed/transductive
adaptation, not evidence of access to hidden test answers. The described 20-second
runtime versus 10-minute from-scratch baseline excludes a demonstrated full amortized
preparation-cost comparison. No causal single-agent-versus-MAS ablation is supplied.

**Code inspection:** [launchable repository](https://github.com/PicoNVIDIA/data-explorer-launchable),
revision `a719eb8559daf72754eaf065f2a2ca402810c60b`. README_LAUNCHABLE.md identifies the
NVIDIA team and explicitly says the demo runs inference from scratch. Retrieved fourteen
selected files plus the few-shot file; inspected the README, configurations and selected
learning/inference code, without installation or execution:

- [Inference config](https://github.com/PicoNVIDIA/data-explorer-launchable/blob/a719eb8559daf72754eaf065f2a2ca402810c60b/dabstep_agent/inference/dabstep_config.yml)
  configures one tool-calling agent, Python execution and up to 20 iterations. One
  runtime agent does not mean one LLM call or one code execution.
- [Learning code](https://github.com/PicoNVIDIA/data-explorer-launchable/blob/a719eb8559daf72754eaf065f2a2ca402810c60b/dabstep_agent/learn/learn.py)
  places the supplied expected answer in the learning prompt; default input is dev.
  This is disclosed supervised preparation, not evidence of hidden-test leakage.
  Our protocol cannot expose hidden evaluator answers to any agent and cannot simply
  adopt that prompt for held-out tasks.
- `inference/helper.py` and `inference/new_solutions.md` are both zero bytes in this
  revision. The repo tells users to regenerate them with learn/distill. The exact
  winning artifacts, review history and effect of stochastic regeneration are not
  established by an accessible demo. No license file was visible in the inspected tree;
  inspect reuse terms before vendoring code. Public access alone is not a license.
- The repository contains multi-pass inference and majority-vote tooling; presence
  is not proof those settings produced the validated submission. The checked ordinary
  inference prompt supplies question/guidelines, not its `answer` field.

**Use in our study:** strong evidence that domain work can be amortized into executable
assets. This is close prior art for experience reuse, not proof that context/verification
problems remain unsolved. Compare equally prepared systems and count construction,
reflection, maintenance and per-task costs separately. Do not claim to reproduce 89.95%.

## DataPilot: the main-agent/subagent pattern already exists

[Author technical article](https://en.oceanbase.com/blog/24781555459) describes versioned
SOPs, metric definitions and executable assets, distinct build/runtime phases and a
unified ReAct entry point. It explicitly delegates alternative interpretations to
subagents, including ReCodeReasoningAgent, and promotes branches using regression
evaluation. Labelled evaluation is discussed but the inspected account does not fully
specify which labelled split supports each asset update or the validated score. This
is engineering documentation, not an independent replication or causal topology study.

Full submission implementation was not confirmed. The inspected
[open-source request](https://github.com/oceanbase/oceanbase/issues/2397) contains no
release-confirming response; this is a search lead, not proof code is unavailable.
The OceanBase database/skills/integration repositories are not the winning agent.

**Use:** particularly close to both selected problems and the proposed hierarchy.
Versioned assets, delegated competing interpretations and feedback-driven promotion
are prior art. A hierarchy or shared rule registry alone cannot be our novelty.

## DS-STAR, Amity, AgenticData and opaque validated entries

- **DS-STAR:** [v4 paper](https://arxiv.org/html/2509.21825v4), Sections 2 and Appendix A.
  The verifier receives query, plan, code and output; the router appends or repairs
  steps. Appendix A refers to other subagents explicitly. Despite the singular product
  name, this is a role-based multi-agent workflow in the paper's terminology. Use its
  verifier/input ablations as close prior art. Public third-party implementations,
  including IBM OpenDsStar, differ from the reported system; prior artifact limits
  remain in [reading-brief.md](reading-brief.md).
- **Amity:** the leaderboard's old article URL failed, but the
  [author-hosted Thai article](https://www.amity.co/th/ai-lab/agentic-ai-multi-agent-data-analysis)
  explicitly describes Planner, ReAct Executor and Feedbacker and links a whitepaper.
  Read the web description, not that whitepaper or a runnable implementation. This
  contradicts classifying all leading entries as single agents; author superiority
  language is not adopted as controlled evidence. Use for architecture comparison.
- **AgenticData:** current paper/memory/validator cards remain in the reading brief.
  Original system code remains unconfirmed. A similarly named unvalidated Gitee entry
  is not established as the original author's implementation.
- **gg-agent:** no code URL in validated row and no informative exact-name result in
  the bounded search. Agent count, underlying model version and evaluation procedure
  remain unknown. Do not infer topology from the singular entry name.
- **CambioML/Energent:** inspected the linked product page and targeted searches;
  no submission-specific code/paper was established. Product marketing claims around
  94.4% must not be substituted for its separate 57.67% hard score. Topology remains
  unknown. A commercial endpoint is insufficient for a MAST trace study.

## Additional linked unvalidated entries

| Entry/group | Public material checked | Conclusion for baseline admission |
|---|---|---|
| Lark Base / ByteDance | Linked product page, including alternate link | No submission code/topology established |
| VeigaPunk CodeAgent / GPT5 | Link returns to leaderboard | No implementation evidence from that link |
| VeigaPunk FeeEngine | [Repo](https://github.com/VeigaPunk/dabstep-fee-engine), selected `fee_engine.py`/`run_agent.py` | Deterministic domain solver exists; 100% is unvalidated; preparation/fidelity/license need audit |
| ThinkEvolve | [Product page](https://www.thinkevolveconsulting.com/query-your-data/) | Product claims; no submission code/scientific method established |
| DataSage | Linked author article; web and direct requests failed, direct HTTP 403 | Cannot treat unread ontology-method description as verified |
| Cascade Cognition | [Author report](https://www.cascadedynamics.ai/benchmarks.html) | Explicitly calibrates deterministic semantics against published graded artifacts/submission files; unsuitable as evidence of clean held-out generalisation; code on request |
| AgenticData-397B-emptyfix | [Gitee link](https://gitee.com/SmartDigit/dabstep-agent), HTTP 403 | Code contents/provenance unverified; not the original AgenticData release |
| FinHelm | [Repo](https://github.com/ZhouJiaJun2333/FinHelm), README, license, six selected source/docs files | Accessible implementation with memory and subagent/verifier controls; details below |
| Bare CLI entries | Public generic Codex/Claude Code links | Generic tools are not frozen submission harnesses; exact budgets/prompts not established |
| agentic-data-contracts | [Repo README](https://github.com/flyersworder/agentic-data-contracts) | Governed metric/context tooling; full code/submission reproduction not audited |

Repeated DataPilot/Cascade/Lark entries are grouped; the table covers distinct linked
systems above AgenticData in the observed unvalidated snapshot. MemoryLake has a prior
engineering card; its high unvalidated rows in this snapshot have no code link. Scores
without linked artifacts remain metadata, not evidence of method or correctness.
For Cascade, computing from raw tables does not remove test-information exposure in
the rules; this is based on its disclosure, not an accusation of copied answers. Do
not repeat its allegations about other entrants as established facts.

### FinHelm: promising infrastructure and relevant negative evidence

Inspected revision `89e1546cab8fdfd9e996e8f6a6efeec933bc1be5`: LICENSE confirms MIT
with identified third-party exceptions. The README describes a main agent, project/user
memory, optional `delegate` subagents and optional pre-delivery verification. Subagent
code runs a separate child Agent on fresh context, returning a report; this is an
actual delegation interface, not just renaming a Python tool.

[Author evaluation log](https://github.com/ZhouJiaJun2333/FinHelm/blob/89e1546cab8fdfd9e996e8f6a6efeec933bc1be5/docs/evaluation.md)
reports a 10-dev-task comparison: enabling verification kept mean accuracy at 73%,
increased input tokens about 1.8 times and time about 1.6 times; ordinary optional
delegation was not used in its tested runs. These are author-reported small-development
results, not our replication or proof of no MAS benefit. The log is close negative
evidence and shows that merely making delegation available is not an active MAS test.

[Verification hook](https://github.com/ZhouJiaJun2333/FinHelm/blob/89e1546cab8fdfd9e996e8f6a6efeec933bc1be5/src/data_agent/subagents/verify.py)
withholds solver code but asks the parent to send conclusions, numbers and conventions;
it can skip the nudge when too few steps remain. Thus semantic/candidate independence
and actual verification exposure need measurement. This is close prior art for our
previously unselected independent-check proposal. No installation, tests or agent runs
completed. Treat FinHelm as a feasible candidate to audit, not a selected baseline.

## What counts as MAS and where MAST applies

[MAST v3 Appendix B](https://arxiv.org/html/2503.13657v3) explicitly includes a
central planner with specialized child agents in HyperAgent and supervisor/service
agents in AppWorld. Peer-to-peer debate or simultaneous execution is not required.
For our operational definition, a hierarchical MAS has distinct agent contexts/roles,
delegated reasoning/action and observable result/message transfer. Sharing one base
model does not collapse those agents into one. A plain Python executor or renamed
single-context role instruction does not by itself establish a second agent.

Document the reasoning/context boundaries, delegation policy and actual invocations.
MAST communication labels require real inter-agent evidence; tool-only single-agent
runs have no inter-agent handoff to label. Keep nonapplicable/unknown codes rather than
force every error into FM-2.x. One product name, model family or main entry point does
not reveal the number of agents or preparation stages.

## Scientific rationale, counterevidence and design recommendation

Two important primary-source follow-ups:

- [Scaling Agent Systems v3](https://arxiv.org/html/2512.08296v3), Section 3.1, selected
  results and limitations; latest history checked. Controlled comparisons show task-
  dependent collaboration benefits and overhead/saturation. Centralized MAS is explicitly
  defined. This does not establish a DABstep-specific gain or a universal accuracy
  threshold. Use for conditional architectural rationale, not a promise to beat leaders.
- [Strong Single Agent Baseline v1](https://arxiv.org/html/2601.12307v1), abstract,
  workflow definition and selected methods. A single-agent simulation can match tested
  homogeneous workflows with efficiency advantages. Use to strengthen our single-agent
  control; neither this result nor its cache mechanism proves every MAS is redundant.
  These new works remain discovery readings outside Zotero/export, not full replications.

**Recommendation, not selected implementation:** keep the agreed two-problem study and
consider a compact hierarchical system based on an auditable implementation (FinHelm
now merits inspection alongside OpenDsStar). Do not build an always-talking large team
or make a topology search another experimental dimension. Fix topology and activation
policy before the main four-condition comparison and report actual delegation/checks.

The testable justification is bounded context separation for source/experience work
and genuinely additional semantic checks, with communication/integration risks exposed.
Potential benefit is a hypothesis, especially on already well-prepared DABstep tasks.
Independent contexts do not imply independent errors. Parallelism helps only separable
work and can cost more; modularity/inspectability alone is not evidence of better accuracy.

Use a strong single-agent implementation on the same runtime, same model, tools and
frozen source/asset bank, allowed to self-check under comparable aggregate caps. Where
feasible, simulate the same role sequence in one context to test whether extra agents
add value beyond procedure. Equalize offline preparation too. Record preparation cost
separately and amortize it over declared query volumes; no claimed universal cheapness.
All main held-out runs freeze memory/assets, exclude labelled test feedback and stay
separate from test-question offline-reflection experiments.

Native benchmark quality remains necessary, but no global leaderboard victory is
required. The study must show whether targeted errors actually decrease, whether final
quality benefits, and whether the hierarchy justifies its overhead compared with the
strong control. If it does not, report that boundary; a null result is informative only
with valid measurements and adequate uncertainty. Existing assets/verifier ablations
mean contribution claims require a concrete difference, not agents, memory or a critic
alone. Four-condition mechanism logic and common-candidate review tests remain intact.
