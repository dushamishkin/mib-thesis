# Section 1 — Research frontier, current status, challenges and significance

English narrative draft, 10 October 2026. Intended for the first substantive field of
the current university proposal form; not a completed or visually verified DOCX.
Primary links below identify the evidence versions. Complete numbered bibliographic
entries must be reconciled with Zotero during document assembly; these source links
are not a claim that final reference metadata has been verified. Selected reading
scope and inclusion rationales are in [the reading brief](../literature/reading-brief.md).
The scientific specification remains [research-design.md](research-design.md).

## Business analytics requires both calculation and interpretation

Business analytics often appears to be a calculation problem: select records, apply a
formula and report a number. In practice, the calculation is governed by definitions
distributed across tables and documents. A report may depend on which reporting period
is applicable, whether a transaction is eligible, which exceptions take precedence,
and whether a percentage is calculated from transaction counts or monetary amounts.
Code can execute successfully while implementing a rule that does not apply to the
requested report. Reliable analytical assistance therefore requires both computational
correctness and an interpretation supported by the governing documentation.

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

## Evidence links in order of appearance

These identify the inspected sources; replace with complete, verified numbered references
at the end of Section 1 when assembling the institutional document.

1. [DABstep, arXiv:2506.23719v1](https://arxiv.org/html/2506.23719v1).
2. [LongDA, arXiv:2601.02598v2](https://arxiv.org/html/2601.02598v2).
3. [Why Do Multi-Agent LLM Systems Fail?, arXiv:2503.13657v3](https://arxiv.org/html/2503.13657v3).
4. [Silo-Bench, arXiv:2603.01045v2](https://arxiv.org/html/2603.01045v2).
5. [AgenticData, arXiv:2508.05002v2](https://arxiv.org/html/2508.05002v2).
6. [AMA, arXiv:2601.20352v4](https://arxiv.org/html/2601.20352v4).
7. [MemTX, arXiv:2607.23929v2](https://arxiv.org/html/2607.23929v2).
8. [LiveSQLBench author release documentation](https://github.com/bird-bench/livesqlbench), accessed 10 October 2026.
