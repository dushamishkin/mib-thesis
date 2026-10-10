# Current research design

Revised title, scope and roadmap approved by the supervisor, as reported by Mikhail Dushkin on 23 September 2026. Detailed hypotheses and implementation remain subject to pilot validation.

## Approved title

Coordinating Distributed Business Knowledge in Multi-Agent Analytics: A Controlled Study of Shared Memory and Conflict Resolution.

Previously agreed title: When Analysts Become Agents: A Verification-Aware Benchmark for Multi-Agent LLM Systems in Business Analytics.
The approved title emphasizes coordination through shared context and conflict resolution. Executable verification remains part of the controlled design; this title decision does not introduce a new universal memory architecture or change the experimental conditions.

## Objective and continuity

Estimate the separate and joint effects of independent executable verification and shared business-context alignment on the reliability and cost of multi-agent analytics. Retain MAS, business analytics, executable evaluation, MAST-informed diagnosis and the original intervention families. Refine task variation around rules in documentation rather than undertaking a general memory-architecture project.

The original proposal already included V2, C1 and their combination. The revision removes broad priority claims and narrows the empirical question. See ../literature/positioning-note.md for the closest work.

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

## Plain-language definitions for the proposal and defense

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

## Research questions and hypotheses

- RQ1: How do consistent versus conflicting-but-resolvable document-defined rules affect MAS correctness and false acceptance of wrong answers? A strong single-agent control contextualizes any coordination cost.
- RQ2: What are the separate effects of executable verification and context alignment, and how do those effects vary with rule consistency?
- RQ3: Does combining the interventions offer additional reliability worth its resource cost, and which observable failures remain?

Candidate hypotheses, to be frozen before the main study: verification improves computational correctness but can leave shared semantic mistakes unresolved; context alignment helps more under conflicting rules; combining them may improve reliability, but positive interaction and cost-effectiveness are not assumed. Do not turn these expectations into findings before experiments.

## Primary design

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

## Data and tasks

Use public tables with documentation specifying business rules. The [candidate-data audit](../benchmark/README.md) records the current source recommendation, inspected releases, reuse conditions and unresolved gates. The audit recommendation does not freeze dataset selection or task specifications. Our altered tasks are a derivative suite, not official benchmark results.

Start with 10–15 base pilot tasks. Keep tables unchanged across paired consistent/conflicting document variants. Vary one factor at a time: applicability dates, units, population definitions or exceptions. Include harmless/irrelevant document changes. Do not make the latest document invariably authoritative; source priority and scope must be evidenced. Unresolvable conflicts require ambiguity gold labels and separate coverage-aware scoring. Initial documents are readable text exports; OCR and slide interpretation are not core variables.

Compute reference answers independently and manually audit rule applicability and calculations. All systems see equivalent source information; none sees hidden evaluator labels. Split development/test by task family and prevent leakage through persistent memory. Synthetic alterations enable controlled inference but limit claims about naturally occurring enterprise archives.

## Evaluation and analysis

Primary outcomes: end-to-end task correctness and incorrect answers accepted as final. Report failures/timeouts, coverage, unnecessary refusals, rule applicability, computational checks, citation support, tokens, latency and cost. Numeric tolerances and multi-value answer matching are specified per task before evaluation.

Use paired task-level contrasts. Repeated runs quantify stochastic variability; confidence intervals must cluster by base task, including its document variants. Freeze the interaction scale, such as percentage-point success differences. The combined condition beating either individual condition does not itself prove synergy. Model families and run counts depend on pilot cost and variance.

MAST is a descriptive taxonomy with a manually audited trace subset. Use visible messages, shared records, tool calls and code to support diagnoses. Do not infer hidden reasoning or causal attribution from label frequencies alone. Controlled interventions support causal claims only within the specified experimental setting.

## Contribution and practical significance

Proposed empirical contribution: a reproducible paired task suite and controlled evidence about verification/context effects and their boundary conditions. We do not claim a first analytics MAS benchmark, a new general memory protocol or guaranteed superiority.

Practical contribution: acceptance tests and guidance on allocating checking effort between calculations and business definitions, with transparent cost/reliability trade-offs. No claim of realized analyst-time savings or monetary ROI without workplace measurement.

## Risks and exclusions

Main risks: incorrect gold rules, weak baselines, extra-compute confounding, ceiling/floor effects, dependence between task variants and synthetic realism. Address these before scaling. Executable verification exists in software engineering; analytics is chosen for business relevance and auditable computations, not exclusivity. Data alone is not the oracle: the evaluator combines data, specification and applicable rules.

No employer/proprietary data, human-subject study, live Confluence integration, broad topology search or formal universal-memory guarantees. See ../requirements/README.md for institutional requirements and ../ROADMAP.md for milestones.
