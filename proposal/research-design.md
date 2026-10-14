# Current research design

The September title/scope approval is historical. On 11 October 2026 the author approves
the failure-guided architecture below for the revised proposal. The author also accepts
the title, objectives, RQs and working hypotheses in the subsequent discussion.
The author subsequently adopts the two mechanisms and FinHelm adaptation path below.
Exact parameters and operational thresholds remain to be frozen. No renewed supervisor
approval or experimental findings are claimed.

## Approved title

Coordinating Distributed Business Knowledge in Multi-Agent Analytics: A Controlled Study of Shared Memory and Conflict Resolution.

Previously agreed title: When Analysts Become Agents: A Verification-Aware Benchmark for Multi-Agent LLM Systems in Business Analytics.
The approved title emphasizes coordination through shared context and conflict resolution. Executable verification remains part of the controlled design; this title decision does not introduce a new universal memory architecture or change the experimental conditions.

## Objective and continuity

Identify and address evidence/experience-use and semantic-verification failures within
one reproducible analytics MAS. Diagnose broadly, select one literature-grounded repair
per problem, and measure separate/joint effects, transfer and costs. Keep the strong
single-agent control. Earlier C1/V2 implementations are superseded by the adopted pair.

The original proposal already included V2, C1 and their combination. The revision removes broad priority claims and narrows the empirical question. See ../literature/positioning-note.md for the closest work.

## Author-approved research architecture — 11 October 2026

The author approves the two-problem map and bounded design for the revised proposal:
one baseline, literature-guided focus, separate/joint comparisons and common-candidate
review diagnostics. The author now fixes main-agent/subagent MAS and prioritises
DataPilot and DS-STAR as conceptual references. The revised working title is accepted;
approval is not model/budget permission or a protocol freeze. The author now authorises
a complete text-first revision; do not populate the DOCX before narrative review.
Earlier operational details at the end are historical, not the active protocol.

The [11 October mechanism recommendation](../literature/mechanism-selection.md)
compares DataPilot/DS-STAR and specifies evidence-checked experience reuse,
source-grounded counterexample review and a FinHelm-based adaptation path. The author
adopts this packet as the plan; no deployment or gains are claimed. The development
example is in benchmark/pilot-spec.md. The revised narrative is
[proposal-draft.md](proposal-draft.md); the old DOCX remains unchanged.

### Adopted mechanisms and operational revision

The research methodology is a controlled experiment with a 2 × 2 factorial design,
supported by trace-based failure analysis. On 14 October the author requests a simpler
methodology-first Chapter 3; this presentation revision retains the adopted experiment.
Its earlier detailed text is preserved as a historical reference in
[the Chapter 3 snapshot](archive/chapter3-detailed-2026-10-14.md), not another active
protocol. Current mechanism details remain in the linked mechanism packet and design.

Use the packet's source-based applicability admission at the memory-to-solver boundary
and source-first, discriminating fixture review. The fixed hierarchy has a coordinator
and evidence/experience, computation and review children. Adapt the pinned FinHelm
engine, subject to offline isolation/replay/accounting acceptance gates. All MAS
conditions retain ordinary source review, scoped retrieval and the same roles/routes.

Current display names are **Baseline**, **Evidence-checked experience reuse**,
**Source-grounded counterexample review** and **Both**. The author requests these
consistent names throughout the proposal; this standardises wording, not mechanisms. They explicitly supersede the earlier intervention candidate; do not map
new mechanisms onto C1/V2. Maintain strong ordinary and both-mechanism single-agent
controls under equivalent assets/tools and aggregate caps. The main factorial concerns
MAS mechanism effects; architecture comparisons require comparable procedures.

Use the packet's provisional reviewer caps, common-candidate pool, frozen development
bank and separate native/diagnostic tracks. Exact prompts, acceptable retention/rejection
trade-offs, model, task counts and total budget remain to validate/freeze before test.
Older recomputation/shared-context sections below document continuity and are superseded
where they conflict with this operational revision.

**Proposed objective:** identify where existing analytics MAS fail to use applicable
evidence/experience and where their reviewers fail to reject incorrect business
interpretations; select and evaluate one feasible mechanism in each problem group.
Use the entire [problem map](../literature/problem-mechanisms.md) for diagnosis, but
do not attempt to implement a repair for every mapped failure.

### Proposed revised title and objectives

Author-accepted working title for the next supervisor review: **Improving Evidence Use and Semantic
Verification in Multi-Agent Business Analytics: A Failure-Guided Controlled Study.**
Do not name AgenticData in the title until its use is feasible. Evidence use includes
retrieval, interpretation, handoff and application; the selected intervention narrows
to applicability of retrieved experience rather than repairing the whole map.
Semantic verification checks whether interpretation and computation implement the
question under applicable source-defined rules, beyond successful code execution.

Research objectives:

1. Develop an observable, auditable MAST-informed diagnosis of the two failure groups;
   propose analytics-specific refinements/subtypes if recurring errors are insufficiently
   distinguished, and assess coding consistency and diagnostic usefulness.
2. Compare existing methods against that map and select one feasible repair per group.
3. Implement the selected repairs in one fixed baseline with transparent adaptations.
4. Estimate separate/joint effects on targeted failures and native task quality.
5. Establish remaining failures, transfer limits, deployment/adaptation effort and
   cost-effectiveness at explicit quality and coverage levels.

### Internal research questions and working expectations

On 14 October the author requests that the proposal follow the form's objectives,
main contents and key issues, without a formal hypotheses section. The questions and
expectations below remain internal design aids, not required proposal fields or
prerequisites for a positive result. Chapter 2 of the narrative follows that structure.

- RQ1: which observable information-use and review failures recur in the
  chosen baseline, and which are addressed or left open by existing solutions?
- RQ2: does checking retrieved procedures against current sources reduce inappropriate
  reuse while retaining useful experience, and improve quality/resource trade-offs?
- RQ3: how does source-grounded counterexample review affect omission of required checks,
  false acceptance and false rejection on common candidates and end-to-end tasks?
- RQ4: what changes when both repairs are enabled, including additive interaction,
  remaining failures, transfer and cost-effectiveness relative to the baseline and
  strong single-agent control, accounting for preparation and runtime costs?

Directional hypotheses are proposed, not established findings or frozen thresholds:

- H1: the evidence/experience repair reduces its targeted interpretation or
  implementation errors and improves native task quality relative to the baseline.
- H2: the verification repair reduces acceptance of incorrect interpretations on
  common candidates, without an unacceptable increase in rejection of correct ones.
  Define the acceptable trade-off before held-out evaluation.
- H3: the combined system reduces incorrect final answers relative to either repair,
  reflecting their proposed complementarity. This is a testable expectation, not
  an assumption or claim of positive interaction.

RQ1 is descriptive and needs no forced directional hypothesis. Interaction sign,
transfer and cost-effectiveness remain exploratory unless stronger pre-study evidence
supports prespecified hypotheses. After mechanism selection, replace generic repair
wording with exact operations, measurements and comparisons.

These questions refine the earlier candidate questions; they do not predetermine
that a problem will recur, a repair will help, or a team will beat a single agent.
Consistent/conflicting-rule probes remain a possible diagnostic, not an additional
mandatory factorial across every benchmark.

### Sequence and scope gates

1. Operationalise the accepted map as a trace coding guide. For each code define
   required observable evidence, examples, counterexamples and an unknown category.
   Record failure location, object checked and semantic dimension separately rather
   than treating their cross-product as new MAST categories. Eligible population,
   reporting period, denominator, units, joins/grain and exceptions are diagnostic
   dimensions when a task actually requires them. Do not invent a denominator for
   an amount-only question. Audit repeatability and ambiguous cases; report whether
   coding was independently checked rather than assuming inter-rater validation.
2. Compare existing solutions using a mechanism matrix: addressed failure, operation,
   input/evidence, success-label or test-oracle source, demonstrated setting, residual
   failure, public implementation and adaptation cost. Link primary source cards;
   distinguish authors' evidence from our proposed analytics transfer.
3. Inspect and reproduce one accessible analytics MAS baseline. Diagnose development
   traces with the guide, including correct runs. Relevant-passage controls distinguish
   retrieval from downstream use. Natural traces and deliberately constructed review
   stress cases remain separate evidence. No paid run without model/budget agreement.
4. Select one information/experience mechanism and one review mechanism using declared
   criteria: observable and recurring on development tasks, semantically consequential,
   supported by a relevant existing method, implementable with available resources,
   and testable without hidden gold. Record alternatives and selection rationale.
   Do not select tasks or mechanisms for favourable held-out treatment results. If
   diagnosis does not support a problem, revise the scope explicitly rather than force
   an intervention. Selection must precede held-out evaluation.
5. Freeze the two implementations, resource controls, prompts, data splits, scorers
   and analysis. Run the four combinations on the same tasks: baseline, first repair,
   second repair, both. Keep strong single-agent and extra-compute controls; do not
   multiply all diagnostic probes and all models across every benchmark.

The existing V0/C1/V2/V2+C1 IDs apply only if the selected implementations retain their
defined intervention families. A different memory or review mechanism requires an
explicit agreed revision, not silent relabelling. Reader-facing names should describe
the actual operation once it is selected. No previously suggested shared specification,
blinded check, runtime gate or counterexample method is selected by this architecture.

### Long-term memory and diagnostic separation

#### Author-selected hierarchical MAS and strong-control rationale

On 11 October the author fixes a main-agent/subagent hierarchy as the study's MAS.
The [system audit](../literature/dabstep-systems.md) records mixed/unknown leaderboard
topologies and distinct preparation/review stages; scores are not a controlled
agent-count comparison. Distinct child contexts, delegated reasoning/action and
observable message/result transfer define the hierarchy operationally. A deterministic
tool or renamed single-context role is insufficient. MAST communication labels require
actual interactions. Roles and adaptation path are selected above; exact parameters remain to freeze;
no broad topology search is added.

DataPilot and DS-STAR are the primary conceptual references. Analyse their technical
descriptions through the two-problem map without waiting for official code. Separate
explicitly reported failures, demonstrated evaluation limits, described mechanisms,
unspecified details and our testable failure hypotheses. Missing detail is not evidence
of a system failure. An adapted implementation is not a faithful reproduction or a
controlled comparison with published scores. Implementation access remains necessary
for our own observable traces and controlled experiments, not for source-based review.
AgenticData remains related work. FinHelm is the adopted engine adaptation path;
OpenDsStar is a fallback only. Neither is another primary system to reproduce. The author also accepts using Scaling
Agent Systems and Strong Single Agent Baseline as design constraints; reading/version
limits and links remain in the system audit.

The adopted FinHelm engine has inspected MIT source for memory/subagents/checks;
its author's small dev comparison reports no mean accuracy gain from added checking,
with resource overhead. This is negative prior evidence, not our replication.
NVIDIA's inspected demo has empty distilled inference assets, so public code alone
does not confirm reproduction of its winning configuration. AgenticData remains an
intellectual precedent rather than the selected implementation.

Equalize preparation and runtime access. Compare the hierarchy's four repair combinations
against a strong single agent with the same model/tools/frozen assets and self-checking
allowance. Where feasible, simulate the same role procedure in one context. Do not
attribute additional compute, curated rules or labelled preparation to communication.
Report construction/reflection/maintenance cost and amortization separately. Conditional
mechanism benefits, not a presumed global leaderboard victory, justify the study.

#### Business relevance: deployability and cost-effectiveness

The author targets an analytics system that can be adapted to new organisational
data/document environments with limited bespoke engineering. This is a practical
motivation relevant to MIB: adoption effort, organisational knowledge dependence,
quality/resource trade-offs and reuse economics. "Deploy anywhere" is not a demonstrated
capability, scientific novelty or a promised thesis deliverable. No commercial valuation,
realised staff savings or workplace ROI is inferred from benchmark scores.

Record task-independent components versus environment-specific rules, examples,
functions and configuration. Separate cold-start access (tables/docs, no curated
domain assets) from prepared access (frozen permitted development assets). Within each
comparison all conditions receive equivalent assets; a prepared system cannot be
credited with an agent-count benefit against an unprepared control. This distinction
does not require a second full factorial or an enterprise deployment campaign. A bounded
public transfer/cold-start diagnostic is optional after feasibility/budget review;
one fixed corpus cannot establish general portability.

Measure runtime tokens, model/tool cost, latency, failures and coverage, including failed
attempts and retries. For query volume N, report scenario total cost as preparation plus
documented adaptation/maintenance plus aggregate runtime cost; cost per correct answer
divides that total by correct answers, and is undefined when none are correct. Report
quality and coverage alongside this ratio, and compare cost at comparable quality or
quality under comparable budgets. Avoid selecting an artificially cheap system that
declines hard tasks. Log analyst/researcher setup effort prospectively, separating
reusable research infrastructure from environment adaptation. Human effort without
measured wages remains hours, not invented monetary savings. Amortisation and any
break-even query volume are labelled sensitivity scenarios, not observed business ROI.
Cost-effectiveness remains an evaluation dimension across the two problems, not a third
repair target or an assumed directional hypothesis.

#### Memory scope and reviewer measurement

Experience applicability is selected within problem 1. The bounded study adapts
admission from an existing memory bank, rather than constructing
a universal memory system. Build experience only from permitted development material;
freeze and reset the bank per evaluation run and declare memory/source access in every
condition. Holding that bank fixed studies reuse, not online learning. Accumulating
test-run experience would require a separate sequential protocol controlling order,
feedback and dependence. It is not silently included in the four-condition experiment.

For review quality, assess all checker variants on the same development/held-out
candidate pools, including correct and incorrect interpretations. Candidate pools
must be fixed independently of the treatment comparison, and reference labels stay
evaluator-only. Measure omitted required checks separately from wrong judgements
about checks that were attempted, with unknown cases retained. Record acceptance of
wrong candidates, rejection of correct candidates, coverage and downstream correction.
This diagnostic complements end-to-end benchmark accuracy; it does not replace it.

### Evaluation and contribution boundaries

Use the [benchmark programme](../benchmark/README.md): DABstep, QueryProof's WRB and
the AgenticData comparison sets, subject to exact-release/access/scoring gates. Apply
the selected variants to admitted original tasks using each benchmark's native metric.
Concentrate detailed trace coding and mechanism probes on a bounded diagnostic sample;
do not require exhaustive annotation on every benchmark or claim one universal score.
Set campaign size, models and repetitions after feasibility/budget assessment. An
unavailable release remains an explicit comparison limitation, not a substitute dataset.

Keep paired task comparisons and task/family dependence in the analysis. Estimate
isolated effects and the combined effect; specify interaction on the additive success
scale, with uncertainty. A combined win is not itself interaction. Costs, tokens,
latency, failures and coverage remain secondary outcomes, not a discarded concern.

Candidate contributions are an auditable analytics-specific operational refinement
of MAST, an evidence-based selection/adaptation of existing methods, and controlled
evidence of separate/joint effects and limits. The classification needs demonstrable
diagnostic usefulness beyond renaming errors. Neither scientific novelty nor empirical
benefit is established by accepting the map; compare closest prior work before claiming
either. Integrate diagnosis and solution review in the literature chapter, coding and
selection in methods, and effect/transfer analysis in results rather than allocating
a separate experiment or thesis chapter to every failure mechanism.

## Author's practical motivation — clarified 10 October 2026

On 14 October the author adds professional experience as a data/business analyst in
banking. As agentic systems developed, the team tried applying them from ad hoc analysis
to complete analytical projects; context availability and use repeatedly limited
reliability. This is the author's account of prior experience, not a claim about
current employment or measured workplace outcomes. The proposal's Chapter 6 now states
this motivation in one paragraph; research-preparation evidence remains in project records.

The author reports encountering this problem in banking analytics work. Tables have
schemas, team/product organisation and column descriptions, but this structural
metadata does not reliably specify the business meaning required for a query.
Relevant context is distributed across knowledge-base pages and communication threads.
In the author's experience, supplying more context alone can leave contradictory,
missing or unclear definitions unresolved. Even organised documentation can leave
uncertainty about which relationships, joins, filters or aggregation rules implement
the intended business question. This is an author-reported motivation, not a measured
workplace finding, a universal claim about retrieval, or evidence of research novelty.

The analytical distinction is between knowing how tables are represented and knowing
which operations express the requested business meaning. The study targets the latter
within an executable analytical workflow. A wrong join, population filter or metric
definition can produce valid code and plausible numbers. Structured shared context is
a proposed way to make interpretations and their evidence explicit; independent checking
is a proposed way to challenge an analytical solution. Neither creates missing business
knowledge or establishes that multiple agents are necessary.

For task construction, distinguish evidence that is present but dispersed, contradictory
but resolvable, and insufficient to determine a unique answer. The core matched study
retains consistent versus resolvable-conflict variants with equivalent accessible
evidence. Truly missing governing rules cannot have a uniquely correct numerical answer
imposed from researcher-only knowledge; clarification/ambiguity cases require a separate
protocol and remain optional. Join/filter examples motivate task suitability checks,
not a silently approved new task family or experimental dimension.

Workplace experience motivates public-data experiments. Employer tables, internal
documents and messages are not study inputs, and the initial study will not establish
production-bank effectiveness. Broader source discovery and undocumented institutional
knowledge remain outside what the core comparison can establish.

### Author-provided illustration: trade-finance limit utilisation

The author describes a request to calculate total utilisation of trade-finance limits.
A naive approach subtracts the unused balance from the total limit amount at the
reporting date. The author identifies two interpretation requirements: determine which
limits are active using the applicable validity information, and account for umbrella
agreements linking a parent company to other companies. The exact validity predicate,
hierarchy/accounting treatment and utilisation definition were not supplied. Expiry
alone is the author's tentative interpretation of active status, not a verified policy.

This example motivates explicitly establishing the reporting date, eligible limit set,
meaning of balance fields, and relationship between umbrella and company-level records
before computation. Whether records represent independent capacity or allocations of
shared capacity must be evidenced; adding every row could double count if they represent
the same capacity. No particular aggregation or allocation formula is asserted here.
Distinguish utilised amount from a utilisation ratio before choosing a denominator.

This is an author-reported illustration without internal records, figures or policy
documents. It is not a bank case study, verified calculation, or admitted experiment
task. A public or clearly labelled synthetic analogue would need complete agent-visible
semantics and independently audited references before admission; the current pilot
specification and core factorial are unchanged.

## Why study a team rather than assume one is necessary

The motivation is a testable division of work: identifying applicable documentary rules,
writing calculations and checking evidence can be assigned to different agents. Separate
attempts may reveal inconsistencies, but communication overhead and correlated errors
can offset that benefit. Existing analytics MAS make the question relevant; they do not
prove that a team is necessary for our tasks. A single agent may perform all these steps.

The strong single-agent control must be allowed to plan, inspect the same sources,
execute code, revisit evidence and self-check within comparable total resource caps.
It must not be deliberately weakened to justify MAS. Task admission follows semantic
validity before treatment results. If the single agent performs better or achieves
similar reliability at lower cost, the study should report that boundary condition.
Within-team intervention effects remain informative, but cannot justify recommending
MAS over a better single-agent alternative. A null result requires adequate measurement
and uncertainty reporting; a weak or underpowered design is not rescued by calling it null.

## Historical definitions — superseded intervention candidate

**Independent calculation check (executable verification):** a separate checking attempt
uses the question and source documents to construct and execute its own calculation,
then compares it with the team's result. Initially it cannot see the solver's code or
numeric answer. Different implementations can still share the same wrong interpretation;
independence here is a protocol property, not a correctness guarantee.

**Shared rule reconciliation (business-context alignment):** agents populate one explicit
task-local record of the metric, period, population, units, exclusions and supporting
sources. They resolve inconsistent entries using available evidence or record ambiguity.
The intervention does not supply the correct rule; ordinary source reading remains
available in every condition. Agreement on an incorrect rule remains an error.

Define both terms before introducing abbreviations. Proposed reader-facing names below
are aliases; canonical condition IDs and the optional V1 comparator remain unchanged.

## Historical research questions and hypotheses

Earlier candidate wording, retained for continuity; the revised RQ1–RQ4 above governs
current proposal planning. These are not additional research questions.

- RQ1: How do consistent versus conflicting-but-resolvable document-defined rules affect MAS correctness and false acceptance of wrong answers? A strong single-agent control contextualizes any coordination cost.
- RQ2: What are the separate effects of executable verification and context alignment, and how do those effects vary with rule consistency?
- RQ3: Does combining the interventions offer additional reliability worth its resource cost, and which observable failures remain?

Candidate hypotheses, to be frozen before the main study: verification improves computational correctness but can leave shared semantic mistakes unresolved; context alignment helps more under conflicting rules; combining them may improve reliability, but positive interaction and cost-effectiveness are not assumed. Do not turn these expectations into findings before experiments.

## Historical primary design — superseded by adopted mechanisms

Earlier implementation candidate. The four-combination logic is agreed above;
the specific C1/V2 mechanisms below remain under reconsideration.

Hold team roles, topology, base model and source corpus fixed. Cross verification absent/present with context alignment absent/present:

| Reader-facing condition | Canonical ID | Extra executable verification | Shared-context intervention |
|---|---|---|---|
| Baseline team | V0 | No | No |
| Independent calculation check | V2 | Yes | No |
| Shared rule reconciliation | C1 | No | Yes |
| Combined checks | V2+C1 | Yes | Yes |

All conditions can execute SQL/Python to solve tasks. V0 does not disable ordinary execution feedback. V1, the original text-only critic, is optional secondary work.

V2: an independent check recomputes relevant outputs and checks declared computations against available task evidence. It receives the same source access across conditions, no gold answer/reference code, and does not merely rerun the original query. Specify what is withheld from the checking attempt, what tests it can construct, and how detected errors trigger correction. Log all extra work.

C1: agents populate a shared specification of metric definition, period, scope, units, exclusions and supporting passages. They explicitly reconcile incompatible entries using evidence available to all conditions, or record unresolved ambiguity. The initial intervention bundles structure and reconciliation; do not attribute its effect to either component alone without an ablation. Store task-local context initially; cross-session learning is outside the core experiment.

Controls: strong single agent, comparable resource caps and measured consumption, extra-compute MAS control, and document-grounded validation inspired by AgenticData where feasible. Label adapted implementations accurately. On a diagnostic subset supply relevant passages to all systems to separate retrieval failure from interpretation/coordination. Distributed source access is an optional diagnostic extension, not another mandatory full factorial dimension.

### Draft operational specifications — 10 October 2026

For the complete proposal, the assistant proposes four fixed roles: source analyst,
computational analyst, reviewer and coordinator. In V2 and V2+C1 the reviewer first
receives only the question and the same permitted corpus, withholding solver code,
answer, messages and the C1 record until it logs an initial independent interpretation,
evidence and calculation. Later comparison permits a proposed single revision round.
C1 also records relationships/aggregation grain where relevant. The single-agent
control explicitly plans, specifies rules, computes and self-reviews; extra-compute
MAS extends ordinary exposed-solution review without the blinded attempt or C1 schema.
These are proposed procedures for development validation, not frozen parameters or
new supervisor approval. Their effects do not isolate pure cognitive mechanisms.
These earlier specifications do not describe the rewritten [proposal-draft.md](proposal-draft.md).
Use the adopted operational revision above and the mechanism packet for current methods.

## Historical task-variant candidate

Use public tables with documentation specifying business rules. On 11 October 2026,
the author selects DABstep for comparative task quality while research framing remains
open. The [benchmark record](../benchmark/README.md) distinguishes unmodified official
evaluation from separately reported mechanism diagnostics/derivatives, and records
release/scoring and implementation gates. Task selection, campaign size and interventions
are not frozen. Our altered tasks are a derivative suite, not official benchmark results.

Start with 10–15 base pilot tasks. Keep tables unchanged across paired consistent/conflicting document variants. Vary one factor at a time: applicability dates, units, population definitions or exceptions. Include harmless/irrelevant document changes. Do not make the latest document invariably authoritative; source priority and scope must be evidenced. Unresolvable conflicts require ambiguity gold labels and separate coverage-aware scoring. Initial documents are readable text exports; OCR and slide interpretation are not core variables.

Compute reference answers independently and manually audit rule applicability and calculations. All systems see equivalent source information; none sees hidden evaluator labels. Split development/test by task family and prevent leakage through persistent memory. Synthetic alterations enable controlled inference but limit claims about naturally occurring enterprise archives.

## Earlier evaluation specifications — retain only compatible principles

Primary outcomes: end-to-end task correctness and incorrect answers accepted as final. Report failures/timeouts, coverage, unnecessary refusals, rule applicability, computational checks, citation support, tokens, latency and cost. Numeric tolerances and multi-value answer matching are specified per task before evaluation.

Use paired task-level contrasts. Repeated runs quantify stochastic variability; confidence intervals must cluster by base task, including its document variants, and acknowledge dependence within families. The proposal specifies the percentage-point success interaction I = p(V2+C1) - p(V2) - p(C1) + p(V0); confirm this in the frozen analysis plan. The combined condition beating either individual condition does not itself prove synergy. Model families and run counts depend on pilot cost and variance.

Incorrect final acceptance is measured across all assigned attempts, with a separate
conditional error rate among answered attempts and coverage. Distinguish rule
correctness from calculation correctness under the chosen rule. These outcomes do
not assume a separate production approval gate. Main-study sample size follows
valid measurement, variance/precision and budget, not favourable treatment effects.

MAST is a descriptive taxonomy with a manually audited trace subset. Use visible messages, shared records, tool calls and code to support diagnoses. Do not infer hidden reasoning or causal attribution from label frequencies alone. Controlled interventions support causal claims only within the specified experimental setting.

## Contribution and practical significance

Proposed empirical contribution: a reproducible paired task suite and controlled evidence about verification/context effects and their boundary conditions. We do not claim a first analytics MAS benchmark, a new general memory protocol or guaranteed superiority.

Practical contribution: acceptance tests and guidance on allocating checking effort between calculations and business definitions, with transparent cost/reliability trade-offs. No claim of realized analyst-time savings or monetary ROI without workplace measurement.

## Risks and exclusions

Main risks: incorrect gold rules, weak baselines, extra-compute confounding, ceiling/floor effects, dependence between task variants and synthetic realism. Address these before scaling. Executable verification exists in software engineering; analytics is chosen for business relevance and auditable computations, not exclusivity. Data alone is not the oracle: the evaluator combines data, specification and applicable rules.

No employer/proprietary data, human-subject study, live Confluence integration, broad topology search or formal universal-memory guarantees. See ../requirements/README.md for institutional requirements and ../ROADMAP.md for milestones.
