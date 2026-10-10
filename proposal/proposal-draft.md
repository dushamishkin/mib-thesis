# Coordinating Distributed Business Knowledge in Multi-Agent Analytics: A Controlled Study of Shared Memory and Conflict Resolution

Author: Mikhail Dushkin

This is the complete narrative source for the current institutional DOCX draft. Administrative fields and dispatch checks are recorded separately in [review notes](proposal-review-notes.md). Scientific authority remains [research-design.md](research-design.md); this is a proposed operational protocol for supervisor review, not a frozen implementation.

# 1 Research frontier current status challenges and significance

## Business analytics requires both calculation and interpretation

My professional experience in banking analytics motivates this study:
tables may have schemas and column descriptions while the knowledge needed to construct
a business-correct query remains distributed across documentation. In this experience,
additional context can still contain conflicting or unclear definitions, and even
organised documentation may leave the appropriate relationships and filters uncertain.
This motivates the research question; it is not a measured workplace result or evidence
that additional context is generally ineffective. The
proposed experiments use public sources rather than internal bank material.

Business analytics often appears to be a calculation problem: select records, apply a
formula and report a number. In practice, the calculation is governed by definitions
distributed across tables and documents. A report may depend on which reporting period
is applicable, whether a transaction is eligible, which exceptions take precedence,
and whether a percentage is calculated from transaction counts or monetary amounts.
Code can execute successfully while implementing a rule that does not apply to the
requested report. Reliable analytical assistance therefore requires both computational
correctness and an interpretation supported by the governing documentation.

This distinction also concerns joins and aggregation grain. A technically valid join
can count the same business entity several times, while a plausible filter can omit
records that the intended definition includes. These are illustrative risks, not
reported workplace cases. A further illustration from this experience concerns trade-finance
limit utilisation: subtracting unused balances from total capacity requires a justified
active-limit definition at the reporting date and a documented treatment of umbrella
and company-level limits. Where records share underlying capacity, a simple row sum
could count it more than once. The exact workplace rules and calculation are not
established by this illustration. It motivates checking population and hierarchy
semantics before execution; it is not an experiment result or a bank case study.
The proposed procedures can organise and check available
evidence; they cannot guarantee recovery of a governing rule absent from the sources.
The core experiment therefore requires sufficient accessible evidence to determine
the answer, including in its resolvable-conflict variants.

Consider an illustrative fraud-rate report. One document defines the rate as the
number of fraudulent transactions divided by the number of eligible transactions.
Another defines a monetary exposure measure using transaction amounts. Both formulas
can be implemented correctly and produce plausible percentages from the same table.
The relevant reporting definition determines which answer is correct. Agreement between
two calculations is insufficient if both use the wrong definition. This example is a
motivation for the proposed experiment, rather than a failure observed in an existing
agent run. The practical question is how checking effort should be allocated between
recomputing a result and establishing the applicable business rule.

Existing benchmarks already recognise the importance of documentary knowledge.
DABstep supplies multi-step analytical tasks with payment-domain context and executable
data access [1]. LongDA studies analytical tasks requiring extensive documentation [2].
These precedents rule out a claim that combining tables and business documentation is
itself new. They also provide a feasible foundation for a controlled study using public
releases. The proposed project will build on the existing source audit rather than
conduct another broad benchmark search.

## Why study a team of agents?

A multi-agent analytical system distributes work across communicating model-driven
roles. Such a team could separate interpretation, calculation and checking, allowing
different agents to examine different evidence or produce distinct implementations.
However, role separation also creates opportunities for relevant evidence to be lost,
misinterpreted or replaced by an incorrect shared assumption. Communication adds cost,
and separate agents using the same model may make correlated errors. The existence of
several roles therefore does not establish that a team is necessary or more reliable.

The MAST study classifies multi-agent failures involving system design, inter-agent
misalignment and task verification [3]. This supplies a useful descriptive vocabulary
for examining visible failures, but its categories do not identify causal mechanisms
in the proposed analytical setting. Silo-Bench likewise examines distributed
coordination and describes failures of integration despite information transfer [4].
Together, these studies motivate measuring whether agents use the evidence they receive,
rather than treating communication as successful coordination by definition.

The thesis will retain a fixed multi-agent team as its central object while including
a strong single-agent control. The single agent must be able to inspect the same
documents, execute calculations, revise its approach and check its own work within
comparable resource ceilings. A weak one-shot response would not establish the value
of delegation. If the single agent achieves comparable or better reliability at lower
cost, that finding would identify a boundary on the practical value of the team in
this setting. The project would still answer its comparative question, provided that
the tasks, controls and uncertainty support the conclusion. It would not justify a
general claim against multi-agent systems in other domains.

## Computational verification and its limits

Ordinary execution feedback tells an agent whether code runs and may reveal syntax,
runtime or data-access errors. It does not establish that the requested quantity was
computed. In this proposal, **independent executable verification** means that a checker
constructs its interpretation and an executable calculation from the task and permitted
sources before seeing the solver's numeric answer or code. The independently obtained
results are compared afterwards, with bounded opportunities to resolve disagreements.
Re-running the solver's unchanged code is not independent verification.

This intervention is intended to reduce dependence on a single computational pathway.
Its independence is procedural rather than a guarantee of semantic truth: the checker
and solver can still choose the same inapplicable rule. Shared model limitations,
ambiguous documentation and misleading source cues may cause agreement on a wrong
answer. The study must consequently score rule applicability alongside numeric
correctness and examine incorrect answers that survive checking.

AgenticData is the closest identified analytical system comparison. It combines
multi-agent analysis, plan validation and feedback memory, and reports component
ablations [5]. Its validation discussion includes semantic, data and grammar checks;
the evaluation also considers quality and resource costs. The proposed thesis cannot
claim to invent the combination of analytical agents, validation and memory. Instead,
it must specify how initially withheld independent recomputation differs from plan
validation and evaluate that distinction under a controlled protocol. The selected
sections inspected so far do not settle equivalence with the proposed experiment;
an omitted feature in a summary is not evidence that the complete system lacks it.

## Shared business context and conflict reconciliation

**Shared business-context alignment** means that agents explicitly record and
reconcile the specification governing the current task. The shared record identifies
the metric, population, reporting period, units, exclusions and supporting sources.
It starts empty and is populated by the agents from accessible evidence. Conflicting
claims require an explicit applicability decision or an unresolved-ambiguity status.
The researcher does not place the correct interpretation in this record. Otherwise,
an apparent improvement could result from supplying the answer rather than improving
coordination.

Here, shared memory is limited to the current task. It is not a proposed universal
memory architecture or a mechanism for learning from previous test answers. The
intervention bundles structured recording and explicit reconciliation; its estimated
effect will concern that bundle. Establishing the contribution of either component
alone would require a separate ablation, which is outside the initial core comparison.

Conflict-aware memory is established prior work. AMA's current inspected version
includes a Judge that filters retrieved memory and detects conflicts, with refreshing
and evaluation on conversational-memory benchmarks [6]. MemTX studies transactional
belief admission and repair, using controlled evaluation and downstream mock refund
episodes [7]. These sources are necessary to delimit the contribution: provenance,
conflict handling, repair and harm-sensitive evaluation cannot be claimed as new
primitives here. Their inspected settings and protocols differ from the proposed
analytical reporting tasks, but a different application alone does not establish a
scientific contribution. No formal guarantees from those systems are claimed for
the proposed shared-context intervention.

## Evaluation precedents and the proposed comparison

The public analytical benchmarks also constrain the motivation. LongDA notes limitations
of fixed-year documentation and an emphasis on final numeric answers [2]. This supports
examining documentary applicability as well as calculations, but it is a limitation of
that benchmark, not proof of a literature-wide gap. LiveSQLBench's release documentation
already describes business-rule drift [8]. Therefore, changing rules or including
conflicting documentation is insufficient as a standalone novelty claim.

The proposed comparison keeps the underlying tables fixed and constructs matched
document packages. One package provides consistent rules; the other introduces a
conflicting but resolvable claim. The information needed to establish authority must
be available to every condition. Harmless document changes will help distinguish the
effect of conflict from changes in document length or presentation. Related variants
will remain grouped for analysis instead of being counted as independent tasks.

Four conditions separate ordinary team execution, independent calculation checking,
shared rule reconciliation and their combination. Their internal identifiers remain
V0, V2, C1 and V2+C1, respectively. Keeping the base model, team workflow and permitted
sources constant allows controlled intervention contrasts. An additional compute
control is needed because more checking also adds work. Common ceilings alone do not
establish equal consumed resources; actual tokens, retries, latency and cost must be
reported. A higher combined success rate alone cannot demonstrate complementarity:
the joint effect must be compared with the separate effects on a prespecified scale.

## Significance and bounded contribution

The candidate contribution is empirical knowledge about when the two checking mechanisms
help, fail or become unnecessarily costly. Computational checking may catch implementation
errors while accepting a mistaken rule. Shared reconciliation may prevent that mistake
or propagate it across agents. Their combination may be complementary, redundant or
harmful. These are questions to test, not findings already obtained. The principal
outcomes will include correct completion, incorrect final acceptance, coverage and
resource use, supported by auditable rule and calculation references.

The targeted review makes an incremental contribution plausible but does not establish
global novelty. A complete comparison with the closest protocols and implementations
remains necessary before freezing the contribution statement. If equivalent prior
evidence is identified, the project should be positioned transparently as a replication
or justified extension, with the author and supervisor involved in any substantive
change of scope. An exact combination of labels or a different dataset is not sufficient.

The central question is therefore: when do independent executable verification and
shared business-context alignment improve multi-agent business analytics, separately
and jointly, under consistent and conflicting document-defined rules? Addressing this
question with strong controls and task-level uncertainty could provide practical
guidance on analytical acceptance and checking effort. Positive, null and adverse
results are all admissible. No model experiments or intervention results exist at
this proposal stage.


Feasibility also depends on affordable executable workflows. Alibaba Cloud documents
function calling and structured outputs for Qwen3.7-Flash [9], making a dated API version
a candidate for development calibration. Model suitability must be demonstrated on
development cases, and affordability will be measured across the whole workflow,
including checking and corrections. Provider documentation establishes advertised
capabilities rather than performance on the proposed tasks.

## References

[1] Egg, Alex; Goyanes, Martin Iglesias; Kingma, Friso; Mora, Andreu; von Werra, Leandro; Wolf, Thomas. DABstep: Data Agent Benchmark for Multi-step Reasoning. arXiv:2506.23719v1, 2025. https://arxiv.org/abs/2506.23719v1.

[2] Li, Yiyang; Zhang, Zheyuan; Ma, Tianyi; Wang, Zehong; Murugesan, Keerthiram; Zhang, Chuxu; Ye, Yanfang. LongDA: Benchmarking LLM Agents for Long-Document Data Analysis. arXiv:2601.02598v2, 2026. https://arxiv.org/abs/2601.02598v2.

[3] Cemri, Mert; Pan, Melissa Z.; Yang, Shuyi; Agrawal, Lakshya A.; Chopra, Bhavya; Tiwari, Rishabh; Keutzer, Kurt; Parameswaran, Aditya; Klein, Dan; Ramchandran, Kannan; Zaharia, Matei; Gonzalez, Joseph E.; Stoica, Ion. Why Do Multi-Agent LLM Systems Fail?. arXiv:2503.13657v3, 2025. https://arxiv.org/abs/2503.13657v3.

[4] Zhang, Yuzhe; Liu, Feiran; Shan, Yi; Huang, Xinyi; Yang, Xin; Zhu, Yueqi; Cheng, Xuxin; Liu, Cao; Zeng, Ke; Zhang, Terry Jingchen; Jiang, Wenyuan. Silo-Bench: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems. arXiv:2603.01045v2, 2026. https://arxiv.org/abs/2603.01045v2.

[5] Sun, Ji; Li, Guoliang; Zhou, Peiyao; Ma, Yihui; Xu, Jingzhe; Li, Yuan. AgenticData: A Multi-Agent based Data Analytics System for Heterogeneous Data. arXiv:2508.05002v2, 2025. https://arxiv.org/abs/2508.05002v2. The version-specific title follows the v2 full text; the arXiv abstract record retains the earlier title.

[6] Huang, Weiquan; Wang, Zixuan; Lin, Hehai; Wang, Sudong; Xu, Bo; Li, Qian; Zhu, Beier; Yang, Linyi; Qin, Chengwei. AMA: Adaptive Memory via Multi-Agent Collaboration. arXiv:2601.20352v4, 2026. https://arxiv.org/abs/2601.20352v4.

[7] Li, Xiaoyang; Wang, Yiqi; Lu, Haohui; Chen, Zhi; Li, Mo; Song, Pingan; Zheng, Mingkai; Cai, Taotao. MemTX: Transactional Belief Commit for Stateful Agent Memory. arXiv:2607.23929v2, 2026. https://arxiv.org/abs/2607.23929v2.

[8] BIRD team. LiveSQLBench. Author repository README, sections News and Overview. https://github.com/bird-bench/livesqlbench. Accessed 10 October 2026.

[9] Alibaba Cloud. Qwen3.7-Flash model information. Model Studio documentation. https://help.aliyun.com/zh/model-studio/qwen3-7-flash. Accessed 10 October 2026.

# 2 Research objectives main contents and key issues

## Objectives and research questions

The objective is to estimate how independent checking and explicit reconciliation of business context affect the reliability and resource requirements of a fixed multi-agent analytical workflow. Correctness means answering the intended business question using applicable rules, not merely producing executable code. The study will examine document consistency as a task condition and compare the team with a capable single-agent alternative.

RQ1 asks how consistent and conflicting-but-resolvable documentary rules affect correct completion and incorrect final answers in the team, with a strong single-agent comparison. RQ2 asks what separate effects the checking and context procedures have and whether those effects change under document conflict. RQ3 asks whether their combination provides additional reliability worth its resource requirements and what observable failures remain.

The candidate expectations are that independent checking can detect calculation errors while leaving common interpretive errors unresolved; explicit rule reconciliation can be particularly useful under conflict; and combined checking can be complementary, redundant or harmful. These expectations will be prespecified after measurement validation and before the main evaluation. No positive interaction or team superiority is assumed. The experiment estimates effects of operational procedures: both can affect interpretation and computation, so their contrasts will not be described as pure measures of two isolated cognitive mechanisms.

## Main research contents

The first work package is to construct and audit matched analytical tasks from public tables and documentary rules. Each task needs an explicit researcher-side reference for the eligible population, applicable definition, calculation and evidence. Consistent and conflicting variants will preserve the tables and governing answer while changing a documentary claim. Examples must involve consequential business semantics, such as eligibility, reporting windows or aggregation definitions, rather than only identifying the preferred filename.

The second package implements the fixed workflow, four intervention conditions and controls, with isolated task state and recorded resource consumption. The third package evaluates correctness, coverage, errors and costs with paired comparisons and uncertainty that respects related tasks. The fourth examines a prespecified visible-trace subset to describe failures in evidence retrieval, rule application, communication and calculation, without inferring private reasoning.

## Key issues to be resolved

Three issues are central. First, procedural independence requires committing the checker's initial interpretation and calculation before revealing the solver's answer, code or shared record. Second, source authority and business meaning require enough accessible evidence for a defensible answer; researcher-only knowledge cannot compensate for missing agent-facing rules. Third, improvements must be distinguished from advantages caused by more resources or a weak single-agent implementation. The pilot will validate these properties and the scoring protocol before the study is expanded.

The initial scope excludes employer data, human-subject research, production deployment, broad topology search, persistent cross-task learning and multimodal parsing. Genuinely unresolvable questions would require separate clarification-aware references and are optional diagnostic work. They will not be silently mixed with the resolvable core tasks.

# 3 Research methods research scheme and feasibility analysis

## Experimental structure

A controlled experiment will cross two assigned procedures within a fixed analytical team: additional independent executable verification and a structured shared-context intervention. Each condition will be evaluated on matched consistent and resolvable-conflict document variants. Every system retains ordinary Python or SQL execution and receives equivalent task evidence. Table values and the applicable answer remain fixed within a document pair.

| Condition | ID | Independent check | Structured shared reconciliation |
|---|---|---|---|
| Baseline team | V0 | Absent | Absent |
| Independent calculation check | V2 | Present | Absent |
| Shared rule reconciliation | C1 | Absent | Present |
| Combined checks | V2+C1 | Present | Present |

Absent means that the additional prescribed procedure is not assigned; it does not prohibit ordinary document reading, discussion or self-checking. Natural checking in the baseline will be recorded rather than suppressed to create an artificial advantage. The optional text-only critic, V1, is secondary work and will not replace V2.

A proposed fixed workflow has a source analyst, a computational analyst, a reviewing agent and a coordinating agent. The source analyst identifies relevant passages; the computational analyst produces executable calculations; the reviewer performs ordinary review or the assigned independent procedure; and the coordinator resolves recorded disagreements and produces the final response. These are proposal specifications to validate in development, not a completed or supervisor-approved implementation. Roles and message routes will remain constant across the four core conditions once frozen. All agents use the same base model and permitted sources. The coordinator has no privileged reference access.

## Task construction and business semantics

The existing source audit recommends a DABstep derivative for the core development tasks [1]. AgenticDataBench finance is an alternative if source suitability gates cannot be met, and LongDA HERD is a possible later transfer check [2]. This proposal does not repeat the completed broad benchmark screening. Final source admission requires checked reuse terms, clear documentary semantics and independently validated references.

The current development specification proposes 12 base queries across six families: fee quotation, eligibility sets, domestic volume, fraud metrics, reporting windows and conditional quotations. Two document variants per base query produce 24 instances, with four additional harmless-change instances giving 28 pilot instances. These are related development cases, not 28 independent business environments or a held-out test set. Main-study scope requires a defensible set of independent cases/families and a family-level development/test separation.

For each base task, the researcher will document a semantic specification covering the measure, eligible entities, reporting date or window, units, exclusions, relevant relationships and aggregation grain. Tasks involving hierarchy or joins require explicit evidence about whether records represent independent quantities or allocations of a shared quantity. The trade-finance utilisation illustration motivates these requirements, but no bank policy is inferred from it and no utilisation task is currently admitted. A suitable public or clearly labelled synthetic analogue would require a separate reference audit.

The consistent and conflict variants will differ in one consequential claim, such as eligibility, a unit or an applicability window. The conflicting statement must be plausible yet resolvable using source authority, scope or validity evidence supplied equally to every system. Dates, document names and source order will be varied so no universal shortcut determines authority. Harmless changes will preserve business meaning and help assess presentation effects. Both rival interpretations must produce different outputs, unless a case is explicitly designated an invariance control. Admission and exclusions occur before treatment results are observed.

## Intervention timing and correction

The shared-context procedure uses an initially empty task-local record. Agents populate metric definition, population, period, units, exclusions, relationships or aggregation grain where relevant, source passages and unresolved claims. Conflicting entries require an explicit evidence-based reconciliation or ambiguity status. The record will never be prefilled with the correct interpretation. In conditions without C1, ordinary messages remain available, but the prescribed common schema and reconciliation stage are absent.

For V2, the reviewer first receives only the question and permitted source corpus in a separate context. It develops and executes its own solution and commits its initial interpretation, evidence and result to the run log. Until that commitment, it cannot inspect the solver's code, numeric answer, messages or C1 record. The same withholding rule applies in V2 and V2+C1. Afterwards, the coordinator compares the independent and team outputs and can expose the relevant evidence and code for a bounded correction stage. The proposed initial correction limit is one comparison-and-revision round; pilot evidence may change this limit before the protocol is frozen for the main study. All corrections count toward resource usage.

This sequencing protects an initial independent attempt while allowing shared reconciliation to influence the team's solution and the later resolution of disagreements. Independence does not guarantee that interpretations are different or correct. The two procedures overlap in what they can improve, so the factorial estimates concern the assigned procedures and their interaction. Trace patterns will not be treated as proof of a uniquely identified internal mechanism.

## Single-agent and resource controls

The single-agent control will receive the same sources, executable tools and final-response requirements. Its workflow will explicitly include planning, rule specification, calculation and self-review; it will not be a weak one-shot prompt. It can revisit evidence and revise its solution within a comparable total resource ceiling. Because structured work may help regardless of delegation, this control must be given a comparably careful procedure. Comparing these chosen implementations can inform practical selection, but cannot by itself isolate every architectural difference between a team and one agent.

An additional-compute team control will extend ordinary review and revision while exposing the original solution, rather than requiring an initially blinded recomputation or a C1 record. Its extra turn and token allowances will be set before evaluation to approximate the checking workload within a common maximum budget. Exact allowances depend on measured development usage and will then be frozen. Equal ceilings will be reported alongside actual consumption. A quality/cost comparison will not be presented as pure mechanism identification, and realised tokens will not simply be statistically subtracted as though they were unaffected by the interventions.

With the four core conditions and these two controls, 28 pilot instances imply 168 runs per repetition. The number of repetitions is not yet selected. Any later stronger-model or additional single-agent ablation must run a prespecified comparison subset, not only favourable conditions. V1, transfer, topology variation and additional component ablations will be deferred if resources are limited.

## Reference answers scoring and isolation

Each admitted task will have a manually audited applicable-rule specification and two independently constructed reference calculations where feasible, for example Python Decimal and SQL. Numerical agreement is necessary evidence about computation but does not establish rule validity. Rule applicability, authority, precision, expected status and support passages must be reviewed separately. Cases with unclear gold will be repaired or excluded with reasons before evaluated runs.

The runtime will expose only an allowlist of the current task's tables and documents. It will not mount the thesis repository, generator, scoring code, public solutions, gold, prior transcripts or other variants. Evaluated agents will have no external network access. Solver and checker receive identical source permissions and no evaluator-only tools. Memory and execution state will reset between variants and runs; a provider cache must not introduce answer reuse.

All conditions return an answer, unit, status and concise evidence/rationale in the same format. End-to-end success requires a correct value or entity set, appropriate units, the applicable business rule and compatible evidence. Task-specific rounding, set matching and tolerances will be frozen in advance. Format compliance is scored separately. The primary error outcome is an incorrect answer released as final across all assigned attempts; an additional conditional error rate among answered attempts will be reported with coverage. This outcome does not imply a separate real-world approval gate.

Secondary measures distinguish rule correctness, correct computation under the selected rule, citation support, unnecessary refusal, unresolved status, timeout, tokens, latency and monetary cost. This decomposition can distinguish a well-executed wrong interpretation from a calculation mistake. Scoring and adjudication rules will be tested on development outputs. Wherever manual judgement is required, output review will hide condition identifiers where practicable, and ambiguous judgements will be logged for review. No private chain of thought will be requested as ground truth.

## Analysis and uncertainty

For each document setting, paired contrasts will estimate changes in success and final-error rates between procedures. The prespecified success interaction on the percentage-point scale is I = p(V2+C1) - p(V2) - p(C1) + p(V0). A combined condition outperforming both components does not by itself establish a positive interaction. The difference between intervention effects under consistent and conflicting documentation will address moderation by conflict.

Document variants and repeated runs will remain grouped by base task. Uncertainty estimation must also acknowledge related tasks within families; sensitivity summaries will report family-level variation, and a small family count will limit generalisation. Repetitions quantify stochastic variation on the sampled tasks rather than creating independent business cases. The development pilot is not a power justification. Main-study counts will follow measurement validity, observed variability, attainable precision and an agreed budget, rather than observed treatment wins.

Positive, null and adverse effects will be reported with effect sizes and intervals. An interval too wide to distinguish useful benefit from harm will be described as inconclusive. Reliability will be considered alongside coverage and measured resources. MAST-informed labels [3] on a prespecified visible-trace subset will describe retrieval, applicability, communication and computational failures where the evidence supports the distinction. Relevant-passage diagnostics, if feasible, will supply identical passages to all compared systems. Such diagnostics remain separate from the main evaluation and cannot establish mediation from trace frequencies alone.

## Feasibility and remaining gates

Preparatory work has pinned public source files and reproduced selected calculations using separate implementations. This establishes source and calculation feasibility, not agent performance or a fully admitted suite. A minimal harness, semantic audits, isolation checks and scorer validation remain necessary. No agent experiments have been run.

One affordable tool-capable model will be used across all core conditions and controls. A dated Qwen3.7-Flash API model is the initial calibration candidate, subject to account access, tool competence and an agreed spending ceiling. Its provider/version, thinking mode and exact caps will be frozen before evaluation. A one-model study limits generalisation across models. Calibration will use development cases and selection criteria about usable task performance and cost, not preferred treatment effects. Paid calls require a local cumulative budget guard and explicit budget agreement; no paid campaign is authorised at this stage.

The major feasibility costs include authoring semantic references and auditing outputs, not only API charges. If the proposed scope is excessive, models and task breadth will be reduced transparently while preserving the core comparisons and controls. Synthetic documentary modifications aid control but constrain claims about enterprise archives. The conclusions will concern the frozen tasks, procedures and model; bank deployment, analyst productivity and financial ROI require separate evidence.

# 4 Novelties of the proposed topic

The proposed contribution is controlled empirical evidence about when independent checking and shared rule reconciliation improve multi-agent business analytics, and when their additional cost or shared errors make them unattractive. The study will examine whether documentary conflict changes their effects and whether their combination provides more than the sum of component improvements on a prespecified outcome scale. The comparison addresses the application of available business knowledge to executable analytical decisions.

A second sought contribution is an auditable paired derivative task suite with references for business-rule applicability as well as calculations. Keeping tables and governing answers fixed across document variants supports interpretable comparisons. Trace and resource records will make limitations and failures inspectable. These are evaluation artefacts to construct and validate, not completed benchmark contributions.

The practical contribution sought is guidance on allocating effort between interpretation, checking and coordination, with a strong single-agent alternative. Existing work already studies analytics validation and memory [5], conflict-aware memory [6,7], distributed coordination [4] and business-rule drift [8]. The project does not claim a first analytics MAS benchmark, a new general memory protocol or guaranteed team superiority. Its novelty depends on a sufficiently substantive question and comparison with the closest protocols, not a new combination of labels or another dataset. If equivalent evidence is found, the contribution statement will be revised transparently with the author and supervisor before the main study.

# 5 Research schedule and expected outcomes

The immediate milestone is an English proposal reviewed by the supervisor before submission on 15 October 2026, followed by the proposal defense on 22 October. The intended dispatch date is 11 October, with feedback requested by 13 October and revisions on 14 October. Supervisor response time is not confirmed. The institutional schedule requires supervisor approval before upload and review before 20 October. Print delivery arrangements and the exact submission cutoff remain to be confirmed.

| Period | Planned work | Expected output |
|---|---|---|
| 11 to 22 October 2026 | Supervisor review, proposal submission and defense | Approved proposal and defense feedback |
| Late October 2026 | Semantic task audits, minimal harness and budget calibration | Admitted development cases and tested isolation |
| November 2026 | Validate procedures, controls and scoring; expand tasks | Frozen evaluation suite and analysis plan |
| December 2026 | Conduct feasible experiments and prepare midterm report | Run evidence and midterm submission by 20 December |
| January 2027 | Analyse effects, uncertainty, costs and visible failures | Comparative findings and targeted robustness checks |
| February to March 2027 | Write thesis, obtain feedback and revise | Full thesis and reproducibility package |
| 7 to 14 April 2027 | Final thesis and plagiarism-check submission | Supervisor-approved submission |
| Mid to late May 2027 | Final defense on the institutional date | Defense and final revisions |

Expected research outputs are audited public task packages and references, a reproducible fixed-condition harness, a prespecified evaluation protocol, trace/resource evidence and a thesis reporting comparative results. Recommendations will depend on measured reliability and costs. Null or adverse effects remain valid possible outcomes, but imprecise findings will be acknowledged as inconclusive. Exact task counts, repeat counts and any model replication will be set after pilot feasibility and budget agreement. Optional extensions will be deferred before weakening controls or selecting only favourable tasks.

# 6 Prior experience and accomplished achievements

My experience in banking analytics motivates attention to the distinction between documented data structure and business-correct analytical interpretation. The trade-finance utilisation example illustrates the need to define active limits and hierarchy treatment before computation. This experience is motivation rather than a measured workplace study; no internal bank tables, documents or messages will enter the experiments.

The revised title, scope and roadmap were approved by the supervisor according to my report of the discussion on 23 September 2026. The detailed implementation and hypotheses still require pilot validation. A research design, focused source-reading record and draft pilot specification have been prepared. Bibliographic records and selected primary-paper sections have been audited; metadata verification is not equivalent to a complete reading or replication of every paper.

A public-data feasibility audit screened 18 source families and inspected six leading releases. It pinned and checksummed 76 source files and reproduced selected DABstep, AgenticDataBench and LongDA HERD calculations using separate Python and SQL implementations against available public references. These are offline source and calculation checks, not intervention findings. A 12-base-query development specification exists, but the full suite has not passed semantic admission.

There is currently no completed experimental harness, no pilot agent run, no main-study result and no frozen test suite. The proposed intervention effects and practical recommendations remain questions to evaluate. This preparatory work supports a feasible next phase of reference auditing, controlled implementation and prespecified evaluation.
