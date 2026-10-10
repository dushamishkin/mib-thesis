# Detailed English proposal outline

Prepared 10 October 2026 at the author's request to discuss the outline before drafting
the full proposal. This is a proposed writing structure, not a completed submission or
new supervisor approval. The scientific authority remains [research-design.md](research-design.md);
requirements and dates remain in [requirements](../requirements/README.md) and
[ROADMAP.md](../ROADMAP.md). Use the current supplied institutional DOCX without
changing the order of its six substantive report fields.

## Title and central argument

**Coordinating Distributed Business Knowledge in Multi-Agent Analytics: A Controlled
Study of Shared Memory and Conflict Resolution**

The proposal will explain a business-analytics reliability problem: an executable
calculation can be internally correct while using an inapplicable definition, reporting
period, population or exception. A fixed multi-agent team may benefit from independent
recomputation, explicit reconciliation of business context, both, or neither. The study
will estimate these effects under matched consistent and conflicting documentation,
while measuring costs and comparing with a strong single-agent control.

Keep three distinctions visible throughout: calculation versus rule applicability;
task-local shared context versus persistent learning; completed source-feasibility work
versus future agent experiments. There are no experimental treatment results to report.

## Length and presentation plan

Suggested narrative budget: approximately 4,000–5,000 English words, excluding the
administrative fields and references. This is a writing recommendation, not a university
minimum. The actual template requires at least 1,000 English words in Section 1.

| Institutional field | Proposed narrative budget | Main review question |
|---|---|---|
| 1. Research frontier, current status, challenges and significance | 1,600–1,900 words | Why does this controlled comparison matter given existing work? |
| 2. Research objectives, main contents and key issues | 450–600 words | What exactly will be answered? |
| 3. Research methods, research scheme and feasibility analysis | 1,300–1,700 words | Can the proposed effects be measured fairly and credibly? |
| 4. Novelties of the proposed topic | 200–300 words | What bounded contribution is sought? |
| 5. Research schedule and expected outcomes | 250–350 words | What can be delivered by each institutional milestone? |
| 6. Prior experience and accomplished achievements | 200–300 words | What has actually been completed? |

Retain the bilingual form labels and required declaration. Put English subheadings
inside the report fields. Use two essential tables: conditions/controls and schedule.
A compact closest-work matrix and one task-variant illustration are useful if layout
permits. Do not add artificial results tables. Extra pages are allowed; final page count
will follow the template's rendered layout rather than an invented page limit.

## 1. Research frontier, current status, challenges and significance

Write a connected argument organised by research problems, with studies compared
within each subsection. Do not turn the review into one paragraph per paper.

### 1.1 Business analytics as a joint data and specification problem

- Introduce reporting, fee quotation and metric-comparison tasks whose correct answers
  depend on tables and documentary definitions.
- Use one clearly labelled illustrative example: a transaction-count fraud proportion
  versus an amount-weighted proportion. Explain why successful code execution cannot
  decide which definition governs the task. This is not an observed agent failure.
- Connect this distinction to business decisions about checking effort, auditability
  and the acceptance of wrong final answers. Avoid unsupported workplace savings claims.

### 1.2 Multi-agent analytical workflows and coordination failures

- Briefly explain role decomposition, communication and executable tools. Use one or
  two framework/survey sources for orientation rather than reviewing every framework.
- Explain why a team can distribute work but still share a wrong interpretation or
  lose evidence between agents. Team superiority is an empirical question.
- Position MAST as a descriptive failure taxonomy and motivation for trace diagnosis.
  Its annotations do not establish causal mechanisms in this study.
- State why the fixed team and strong single-agent control are necessary.
- Make team necessity an empirical question: explain the proposed division of work,
  communication costs and correlated mistakes. A better single-agent result is a
  boundary condition, not permission to discard tasks or weaken that control. Use
  the argument and definitions in [research-design.md](research-design.md).

### 1.3 Verification, feedback and their semantic limits

- Distinguish ordinary execution feedback, text criticism, self-refinement and an
  independently constructed executable check.
- Review selected verification/self-correction sources only for claims that bear on
  the proposed mechanism; inspect methods and limitations before citing.
- Explain correlated mistakes: two different implementations can agree on an incorrect
  population or rule. Executable agreement is informative but not a semantic guarantee.
- Lead into V2 while retaining the optional V1 text-only comparator as secondary scope.

### 1.4 Shared context, memory and conflict reconciliation

- Explain structured recording of definitions, scope, units, exclusions and provenance.
- Compare analytics memory/validation with conversational memory, supersession and
  dependency-repair work. Read current relevant versions before describing their limits.
- Define the proposal's shared memory as task-local context. Do not claim a new universal
  memory protocol or formal transactional guarantees.
- Explain that C1 bundles structure and explicit reconciliation; a main effect cannot
  identify which component caused it without a later ablation.

### 1.5 Closest analytics systems and evaluation precedents

- Give AgenticData the most detailed system comparison: validation, memory, component
  ablations, source access, task structure and evaluation. Existing validation/memory
  combinations are prior art.
- Use DABstep and LongDA to explain documentation-dependent executable analytics.
  Mention Spider 2.0 or another relevant precedent only where it supports a distinct claim.
- Include LiveSQLBench as a boundary on novelty: business-rule drift already exists.
  Distinguish drift across releases from our paired conflict manipulation; neither is
  sufficient novelty by itself.
- Keep this a focused synthesis of the existing audit. Do not repeat the 18-family
  benchmark search or append its full comparison table.

### 1.6 Research gap, significance and transition to the questions

- Compare whether the inspected closest studies estimate both intervention effects
  and their interaction under fixed-table consistent/conflicting document variants,
  equivalent information, resource controls and explicit rule-applicability scoring.
- Phrase any gap as a bounded result of the inspected evidence, not proof that no
  previous study exists. An abstract that omits a design feature cannot prove absence.
- Present the proposed contribution as controlled evidence about boundary conditions
  and cost/reliability trade-offs. Null or adverse effects remain useful findings.
- End with the central question and transition to the objectives.

**References:** the template places references at the end of this field. Number them
in order of first appearance and provide complete verified metadata. Use a consistent
numbered style throughout the proposal; the form permits reference-format choice.
Use preprint identifiers and inspected versions where final venue metadata is unknown.
Do not impose final-thesis citation rules blindly on this proposal.

## 2. Research objectives, main contents and key issues

### 2.1 Overall objective

State the objective in measurable terms: estimate separate and joint V2/C1 effects on
correct completion, wrong final acceptance and resources in a fixed analytics MAS.
Use the three approved research questions in [research-design.md](research-design.md).

### 2.2 Questions and candidate expectations

- RQ1: effects of consistent versus conflicting-but-resolvable documentary rules;
  contextual comparison with a strong single agent.
- RQ2: separate intervention effects and their variation with rule consistency.
- RQ3: joint reliability, resource cost and remaining observable failures.
- Candidate expectations concern computational checking, semantic reconciliation and
  possible complementarity. Label them proposed hypotheses to freeze before the main
  study; do not assert positive interaction or MAS superiority.

### 2.3 Main research contents

Describe four work packages: construct/audit paired tasks; implement fixed conditions
and controls; measure outcomes and task-level effects; analyse visible failure traces
and practical trade-offs. State exclusions concisely by linking the scope to feasibility.

### 2.4 Key issues

Explain the main identification problems: independent verification, applicable-source
authority, equal information/resources, hidden-reference isolation and dependent task
variants. Connect each issue to a solution in the methods field.

## 3. Research methods, research scheme and feasibility analysis

### 3.1 Experimental logic and conditions

Present V0/V2/C1/V2+C1 in a 2×2 table. All systems retain ordinary executable tools.
Lead with the reader-facing names in the design's mapping table and define both
interventions before abbreviating them. Preserve canonical IDs for traceability.
Cross the four conditions with consistent/conflicting document variants while holding
tables fixed. Hold core team roles, topology, base model and source access constant.
Specify the final role workflow before runs; avoid inventing an approved team size.

Retain a strong single agent and an extra-compute MAS control. Match resource ceilings
and report actual consumption; equal ceilings alone do not prove equal used resources.
Explain the purpose and implementation boundary of each control. Any adapted
AgenticData-inspired validator must be labelled accurately and scoped for feasibility.

### 3.2 Task construction and source choice

Summarise the existing [data recommendation](../benchmark/README.md), not a fresh search.
The DABstep derivative is the proposed core, with AgenticDataBench finance as an
alternative and LongDA HERD as a possible transfer check. Source choice remains subject
to semantic and reuse gates.

Describe the proposed 12-base-task development pilot and the six families in
[pilot-spec.md](../benchmark/pilot-spec.md): fee quotes, eligibility, domestic volume,
fraud metrics, windows and conditional quotes. Explain consistent/conflict pairs and
harmless document controls. Keep documentary authority available to every system;
rotate authority patterns so dates/filenames cannot shortcut the task.

Use one schematic pair to show unchanged tables and a single conflicting claim.
The pilot is development work, not held-out evidence or a power calculation. The main
study requires additional independent families and a family-level development/test split.
Task admission follows semantics before treatment runs, never favourable outcomes.

### 3.3 Intervention protocols

- V2: independently reconstruct the interpretation and computation from the same
  sources; initially withhold solver code and numeric answer; compare afterwards and
  record bounded correction attempts. Freeze withholding, comparison and retry rules.
- C1: agents populate an initially empty shared specification with evidence and
  explicitly reconcile conflicts or record unresolved ambiguity. No researcher-supplied
  correct interpretation belongs in the intervention schema.
- Reset task-local state between variants and runs. Record all intervention work and
  resources. Distinguish independent implementation from independent semantic truth.

### 3.4 Reference answers and isolation

Explain independent reference computations plus author audit of applicable rules,
precision, evidence and status requirements. Gold and reference code remain outside
both solver and checker access. Runtime allowlists and network restrictions prevent
access to researcher notes, public solutions, other variants and previous transcripts.
Reference validation is an admission gate; the current suite is not fully audited.

### 3.5 Outcomes and scoring

Define end-to-end correctness to include value, unit, applicable rule and compatible
supporting evidence. Define incorrect final acceptance across all attempts and report
its conditional rate among answered tasks separately, together with coverage.
Record abstention, unnecessary refusal, timeout, computational correctness, rule
applicability, citation support, tokens, latency and cost. Task-specific tolerances
must be fixed before evaluation. Unresolvable ambiguity, if included, has separate
gold/status rules and is not conflated with resolvable conflict.

### 3.6 Analysis and observable failures

Use paired contrasts and base-task-clustered uncertainty intervals, keeping document
variants and repetitions in the same cluster. Consider residual family dependence
and report the limited independent-family count honestly. Do not inflate sample size
by treating repetitions as new tasks.

For each document setting, prespecify the success-percentage-point interaction:

`I = p(V2+C1) - p(V2) - p(C1) + p(V0)`.

An improvement of the combined system over both individual systems is not itself
evidence that I is positive. Report effect sizes, uncertainty and costs, including
negative results. Main-study task counts, models and repetitions follow budget and
pilot variance rather than treatment wins.

Use MAST-informed annotation of a manually audited visible-trace subset. Separate
retrieval, applicability, information transfer and computation where evidence permits;
do not infer private reasoning. Relevant-passage diagnostics supply passages equally
to all conditions. Explain limits of causal interpretation outside the controlled suite.

### 3.7 Feasibility, validity risks and scope reduction

Use the existing offline source/calculation audit as feasibility evidence. Describe
risks of gold errors, weak controls, extra compute, ceiling/floor effects, related
tasks and synthetic documentation. State concrete mitigations and a fallback order:
preserve the core factorial and controls; reduce models/task breadth; defer V1,
transfer, component ablations and additional access/topology studies.

No paid campaign is authorised. Model/budget, exact caps, team workflow, repetitions
and main-study size remain decisions to settle before running experiments.
Use the provisional low-cost model and bounded cost scenarios in
[experiments](../experiments/README.md); distinguish recommended limits from approved spending.

## 4. Novelties of the proposed topic

Frame three candidate contributions in prose: a controlled comparison of V2/C1 and
their interaction under document conflict; an auditable paired derivative suite with
semantic as well as computational scoring; measured reliability/resource boundary
conditions and practical acceptance guidance.

Explicitly acknowledge prior analytics systems, validation, memory and rule-drift
evaluation. A changed application domain is not sufficient novelty. These contributions
are sought outcomes, not achieved findings or universal protocol guarantees.

## 5. Research schedule and expected outcomes

Condense the canonical [roadmap](../ROADMAP.md) into a milestone table for the proposal:
October proposal/defense and subsequent pilot; November task/analysis freeze;
December experiments and midterm; January analysis; February full draft; March revision;
April final submission; May defense. Do not turn tentative experiment timing into
completed progress.

Expected outputs: audited task packages/references, reproducible fixed-condition
harness, prespecified evaluation, traces/cost evidence, comparative analysis, thesis
and practical acceptance guidance. Positive, null and adverse effects are all admissible.
Exact costs and statistical precision remain conditional on pilot feasibility.

## 6. Prior experience and accomplished achievements

Report documented preparatory work: approved direction (with approval provenance),
research design, literature metadata/selected-section review, reproducible public-source
audit and proposed pilot specification. Describe the calculation cross-checks as offline
feasibility work, not V2 agent results or validated treatment effects.

State accurately that no harness, pilot agent runs, main-study findings or frozen test
suite exist. Do not invent publications, professional experience or awards. Avoid
mistaking a Zotero metadata audit for completed full-paper reading.

## Literature review execution plan

The [reference index](../literature/references.md) is the canonical reading/audit record;
Zotero owns bibliography metadata. Start with the 29 existing records and targeted
comparisons in the benchmark audit. Approximately 12–18 substantive references may
support a focused proposal; this is a provisional writing target, not a citation quota.

1. Build a researcher-side claim/evidence matrix: proposed claim, paper/version,
   supporting section, limitation, and intended proposal subsection. Every important
   novelty claim requires methods/evaluation inspection, not abstract-only evidence.
   Present each key source to the author with a primary link, plain-language summary,
   inspected sections, reason for inclusion, limits and unresolved follow-ups. Start
   with the [reading brief](../literature/reading-brief.md). Clearly separate the paper's
   findings from our interpretation; consequential positioning changes are discussed
   with the author rather than silently adopted.
2. First inspect MAST, AgenticData, DABstep, LongDA and LiveSQLBench. Check current
   primary-source versions and metadata. Then address AMA/Silo-Bench/MemTX follow-ups
   only insofar as the proposal depends on their claims. Use selected older framework
   and self-correction studies for background rather than a long historical catalogue.
3. Use Consensus for bounded searches on independent checking in analytics, shared
   context/conflict reconciliation, and controlled validation–memory comparisons.
   Fetch promising records, then verify the actual primary paper and relevant sections.
   Screen out irrelevant domains and do not infer peer review from search inclusion.
4. Compare closest studies by task type, source access, intervention, controls,
   conflict manipulation, outcomes and limitations. Distinguish supported differences
   from unresolved evidence. Revise the gap if a closer study is found.
5. Reconcile any new record by DOI/arXiv ID in Zotero, preserve project keys, review
   automatic export and update the reading index. Do not manually edit references.bib.
6. Write the synthesis, check each claim against its evidence, number citations and
   reconcile the final reference list. An unverified claim should be narrowed or omitted.

The 10 October Consensus discovery test found AgenticData and its record was fetched.
Its abstract describes three benchmarks and the older title; the primary v2 has a
revised title, five benchmarks and validation/memory ablations. This illustrates why
discovery metadata cannot replace version-specific reading. No new bibliography
records or live Zotero synchronization are claimed in this outline task.

## Personal and administrative fields

Known project facts can populate author, supervisor, school and approved title, subject
to the author's check of official spellings. Leave these fields explicitly unresolved:

- Student ID; official degree-program category, major and study-mode wording. The
  template's Academic Master Student and Full-time entries are prefilled examples,
  not confirmed personal facts.
- Actual defense date/venue entries and any room/platform; institutional dates are
  recorded in requirements but the exact field convention should be checked.
- Project-source checkbox: self-proposed appears plausible but requires author confirmation.
- Student signature and actual signing date. Replace the sample 2026-09-18 date;
  never generate a signature.
- Submission cutoff/timezone, accepted file formats, approval/signature procedure,
  printed copies and physical delivery. These are process questions, not text gaps.
- Supervisor email address for a sendable draft; never invent an address.

## Next deliverable and acceptance

After discussing this outline, draft the complete English narrative in the supplied
DOCX. Verify source claims and references; retain no empty substantive field; render
and inspect every page; resolve layout defects; report remaining personal/admin fields;
prepare the supervisor email draft. Target author dispatch on 11 October, approval
before submission on 15 October, and defense on 22 October, as recorded in the roadmap.
This outline itself has not produced or visually verified a completed proposal DOCX.
