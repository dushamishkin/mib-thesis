# Proposal defense — presentation outline

Prepared 23 October 2026. Production outline for the [defense package](defense/README.md).
No experimental results are available.
Author reports that the proposal is ready and requests the outline before slide production.
Author approves slide production on 23 October, with MAST deferred until Literature
Review and DABstep introduced before the system comparison. The main speech has 13
slides. Five additional slides support questions and are hidden during the slide show.

## Format and sources

Plan: **13 main slides, 9 minutes 30 seconds of speech**, leaving 30 seconds within
professors' ten-minute limit. Backup slides support questions and are outside the speech.
The supplied five-slide [university starter](../requirements/proposal-defense-template.pptx)
provides the visual template and required topics, rather than a five-slide maximum.
The newly supplied copy is byte-identical to that canonical template.

The author-supplied `25 MIB Thesis defense tips(1).pdf` in `proposal/templates` specifies
at most ten minutes, roughly twenty minutes including questions, rehearsal timing,
and a written record of committee comments and answers afterwards. Both pages were
visually inspected. It lists sessions on 22 and 23 October; the author's reported
personal defense date is **23 October 2026**. Meeting access details are not reproduced.
The local source files remain untouched.

Content follows the author's current Word proposal, read in full, and the
[research design](research-design.md). The Word file contains author revisions and
must not be regenerated from Markdown during presentation preparation.
Literature details and evidence boundaries are in the
[mechanism-selection packet](../literature/mechanism-selection.md) and
[reading brief](../literature/reading-brief.md). Existing literature evidence is sufficient
for this outline; no new performance, novelty or current leaderboard claims are made.
The deck should use short citations tied to the proposal bibliography, with full links
in a backup references slide. Leaderboard figures, if added, must retain their audit date.

## Template sections and narrative order

The author requests the university template's section order explicitly. Use these
section labels in the deck, without spending time on separate divider slides:

| Template section | Main slides | Speech time |
|---|---|---|
| Background | 2–3 | 1:30 |
| Research Question | 4 | 0:35 |
| Literature Review | 5–6 | 1:30 |
| Research Plan & Method | 7–10 | 3:20 |
| Expected Results & Innovation Points | 11 | 0:45 |
| Research Questions, Challenges & Limitations | 12 | 0:35 |
| Expected Research Progress | 13 | 1:00 |

The title slide adds 0:15. Total: **9:30**. Template labels use corrected English
where needed while preserving their coverage and sequence. Open with business
calculation correctness, then briefly introduce the two failure problems and name
the proposed mechanisms, without introducing MAST in Background. Derive the research
question from this chain. Only then
review existing systems through the failure framework and explain the methods in detail.

Early introduction and later analysis serve different purposes. Slide 3 supplies
intuition only. Slides 5–6 introduce DABstep and establish the literature basis, MAST
and evidence boundaries.
Slides 7–10 specify the planned architecture and experimental operations.
Use one hypothetical sales example throughout. It is explanatory, not a benchmark
result or a claim about error frequency. Begin substantive content after the title
without an extra contents or divider slide.

## Main slides

### 1. Title — 0:15

Template section: **Title**.

**Improving Evidence Use and Semantic Verification in Multi-Agent Business Analytics:
A Failure-Guided Controlled Study**

Mikhail Dushkin · 125120990077 · Master of International Business
Supervisor: Prof. Liu Jialu · SJTU Antai · 23 October 2026

Opening sentence: “I study how analytical agents can use business knowledge more
reliably, and whether additional checks are worth their cost.”

Visual: university title layout. Preserve the full title; do not read it aloud word for word.

### 2. Business Calculation Correctness — 0:50

Template section: **Background**.

Show the question: “What is the average completed sales value per purchasing customer?”
The source document defines the denominator as customers with at least one completed
sale and excludes cancelled orders from sales value.

| Customer | Sales value | Status |
|---|---:|---|
| A | 100 | Completed |
| B | 60 | Completed |
| C | 20 | Cancelled |

A calculation using all rows returns 180 / 3 = 60. The source-defined calculation
returns 160 / 2 = 80. Both programs can run without an error. Correctness therefore
requires the question, tables **and applicable business definitions**.

Visual: three-row table, a short source excerpt, and the two calculations. Mark
“Illustrative example — not an experimental result.” Explain population and denominator
in ordinary language; do not introduce the whole failure taxonomy here.

### 3. Two failure problems and the proposed improvements — 0:40

Template section: **Background**.

Describe the two concrete problems and the two proposed mechanisms only. Do not
name or explain MAST here. Use “multi-agent system” in full in the research question.

Use two short rows, with no detailed codes or implementation steps yet:

| Problem | Proposed improvement to test |
|---|---|
| Available experience is applied under the wrong business conditions | Evidence-checked experience reuse |
| Review approves an incorrect business interpretation | Source-grounded counterexample review |

Explain each mechanism in one sentence. The first checks whether a retrieved
procedure applies to the current question and sources. The second tests an interpretation
using a small example whose expected behaviour follows the documents.
In the sales example, the first targets reuse of the all-orders procedure and the
second challenges approval of its answer. These are separate problems that can occur
in the same trajectory. Their theoretical framing and MAST mapping come in the
literature review.

Visual: the two rows with one sentence of explanation each. Transition: “These two
failure points lead to the research question.” Do not present either remedy as effective yet.

### 4. Research Question — 0:35

Template section: **Research Question**.

Main question: **How do evidence-checked experience reuse and source-grounded
counterexample review, separately and together, affect the reliability and
cost-effectiveness of a hierarchical multi-agent system for business analytics?**

Spoken supporting questions preserve the current internal RQs: which failures recur
in the baseline, how each mechanism changes its targeted failures and final-answer
quality, and whether any joint gains justify the cost compared with strong single agents.

Visual: main question in full, with a short objective underneath: establish which
changes help, under which conditions, and at what cost. No formal hypotheses block.
Transition: “To design that comparison, I first examined how existing systems handle
knowledge reuse and review.”

### 5. DABstep and Existing Analytics Systems — 0:45

Template section: **Literature Review**.

First introduce **DABstep**, a benchmark of multi-step data analysis using tables
and supporting documents. Its business-rule interpretation requirements motivate
its use as the primary end-to-end quality benchmark. Explain that the three systems
share this evaluation setting; this does not mean all were built exclusively for it.
Then compare DataPilot, DS-STAR and NVIDIA's DABstep system as high-performing references
in the project's dated leaderboard audit. Explain why each is relevant to this study:

| Reference | Documented mechanism | Relevance to this study |
|---|---|---|
| DataPilot | Scoped, versioned analytical assets and reusable procedures | Starting point for experience applicability |
| DS-STAR | Planning, computation, sufficiency review and refinement | Starting point for ordinary review |
| NVIDIA | Prepared tools and examples with a single agent at inference | Strong alternative to runtime delegation |

Use their technical accounts as design evidence. Their leaderboard scores involve
different models, preparation and tools and do not isolate mechanism effects. Keep
numbers and dated ranking details in backup. No claim of current rank is necessary.

Visual: the three-row comparison. Transition: “MAST helps make the remaining failure
questions more precise.”

### 6. Literature Review through MAST — 0:45

Template section: **Literature Review**.

Introduce **MAST: Multi-Agent System Failure Taxonomy** here for the first time.
It distinguishes system design,
inter-agent misalignment and task verification. Review existing mechanisms through
the two problem groups, keeping documented operations separate from our hypotheses:

| Problem | Literature starting point | What our study will investigate |
|---|---|---|
| Experience applicability | DataPilot scopes/version-controls assets. ReasoningBank retrieves past experience. | Does an explicit current-source check reduce inappropriate reuse while retaining useful experience? |
| Review coverage and judgement | DS-STAR reviews sufficiency. SQLDriller and TS-SQL use executable tests. QueryProof uses business-rule gates. | Does source-grounded counterexample review improve omission and false-acceptance outcomes? |

Explain that omitted checks and wrong judgements on attempted checks are distinct,
with candidate MAST FM-3.2 and FM-3.3 labels. Missing transfer or ignored received
evidence can map to FM-2.4 or FM-2.5 when traces establish those events. Misapplication
of experience has no automatic inter-agent code. Domain-specific refinements require
recurring observable evidence.

Present these as gaps to test within our reproducible adaptation. A missing detail
in a paper does not demonstrate that its system fails. Executable testing and selective
reuse already exist. The contribution concerns their specified adaptation and controlled
effects in document-grounded analytics. Detail on codes and source versions stays in backup.

### 7. Hierarchical Multi-Agent System — 0:35

Template section: **Research Plan & Method**.

Define **MAS: multi-agent system**. A main agent delegates to subagents with separate
working contexts: an evidence worker, a computational analyst and a reviewer.

The hierarchy provides two testable boundaries: check remembered instructions before
they enter the analyst's context, and let the reviewer examine sources before seeing
the analyst's interpretation. This is a reason to test the architecture, not a claim
that it must outperform a single agent.

Visual: main agent above the three children; label evidence transfer and review.
Implementation adapts one public engine, FinHelm, subject to development checks;
it does not claim reproduction of DataPilot or DS-STAR leaderboard scores.
All MAS conditions retain the same roles and ordinary source use and review.

### 8. Evidence-checked experience reuse — 0:45

Template section: **Research Plan & Method**.

A previous analytical procedure is useful only when its conditions still apply.
The evidence worker retrieves a procedure and checks its assumptions against current
source documents **before** passing it to the analyst. Supported experience is admitted;
contradicted or unresolved experience is withheld. Ordinary analysis from current
sources remains possible.

Return to the sales example: the retrieved all-orders procedure conflicts with the
current completed-orders definition, so it should not guide the calculation.

Visual: retrieved procedure → current-source applicability check → admit / withhold.
Use ReasoningBank and DataPilot as precedents, not as evidence that this exact
intervention is novel. Mention the trade-off: rejecting useful experience can also harm quality.

### 9. Source-grounded counterexample review — 0:50

Template section: **Research Plan & Method**.

The reviewer first reads the question and sources, then sees the candidate solution.
It constructs a small executable example on which competing interpretations disagree,
and uses the documented rule to judge the expected behaviour.

Reuse the sales fixture: the all-orders interpretation produces 60, while the completed-
orders interpretation produces 80. The source establishes which is correct; disagreement
alone is insufficient. A check that merely re-runs the same code cannot establish this.

Visual: source rule + two interpretations → distinguishing test → review decision.
The fixture is explanatory; experimental reviewers must generate their own valid tests
without hidden gold. An invalid or inconclusive test is not a successful verification.
SQLDriller and TS-SQL motivate testing; QueryProof makes clear that rule gates already exist.
The test generator and its judgement can still be wrong.

### 10. Controlled Experiment and Evaluation — 1:10

Template section: **Research Plan & Method**.

Name the methodology: **controlled 2 × 2 factorial experiment, supported by trace-based
failure analysis**. Explain simply: switch each improvement on and off while keeping
the hierarchy and ordinary source use and review in place.

| Condition | Evidence-checked experience reuse | Source-grounded counterexample review |
|---|---|---|
| Baseline | Off | Off |
| Evidence-checked experience reuse | On | Off |
| Source-grounded counterexample review | Off | On |
| Both | On | On |

Use the same tasks, model, initial assets, tools/source access and aggregate resource
caps. Include ordinary and both-mechanism single-agent controls to distinguish procedure
effects from architecture effects. Compare separate and joint effects. A combined win
alone is insufficient evidence of positive interaction.

Original DABstep tasks/native scoring measure end-to-end quality. Separate diagnostic
cases measure inappropriate reuse. A common pool of correct and incorrect candidate
solutions isolates reviewer false acceptance and false rejection from solver improvement.
Report final correctness with answer coverage and failures, plus runtime spending,
latency and preparation/adaptation effort. Secondary benchmark use remains gated by
release/access and compatibility checks.

Research sequence: diagnose the baseline, implement the mechanisms, pilot and freeze
the protocol, run held-out comparisons, then analyse failures and costs. The final
progress slide gives the calendar. Model/budget and sample sizes remain pilot decisions.

Visual: four-condition matrix with brief evaluation labels below. Full resource,
leakage and statistical controls go in backup. Preserve readable text and avoid a
dense methods slide containing every metric or parameter.

### 11. Expected Results and Innovation Points — 0:45

Template section: **Expected Results & Innovation Points**.

Expected outputs are an auditable diagnosis of the two failure groups, a reproducible
implementation, and evidence about separate/joint effects on final quality and targeted
errors. The study will also show the cost and preparation effort associated with each
condition. Recurring trace evidence may justify analytics-specific MAST refinements.

The scientific contribution is a failure-guided adaptation and controlled evaluation
of existing mechanisms. It does not depend on claiming the invention of memory or
executable checks. Practical significance is guidance on when investment in knowledge
preparation, reuse and review is worthwhile for analytical teams.

Visual: concise output statements and the comparison that supports each one. Use
“expected outputs”, not fabricated accuracy improvements. An unchanged or worse outcome
can still establish when the added mechanism is unsuitable. Limitations come next.

### 12. Research Questions, Challenges and Limitations — 0:35

Template section: **Research Questions, Challenges & Limitations**.

Focus on unresolved questions and feasibility rather than repeating the central RQ.
A reviewer may generate an invalid test or share the analyst's wrong interpretation.
The baseline may show too few relevant failures, and useful checks may add more cost
than benefit. A fixed hierarchy and public benchmarks limit conclusions about other
organisations, models and workflows.

Explain the corresponding safeguards briefly: validate test expectations and case
validity, check target-failure prevalence during development, report null/negative
findings and total costs, and keep conclusions within the tested setting. Private
bank data and production deployment are outside scope.

Visual: three concise challenge/response rows. The explanation must make clear that
separate agent contexts do not guarantee independent or correct judgement.

### 13. Expected Research Progress — 1:00

Template section: **Expected Research Progress**.

**Prepared:** literature synthesis, two-problem diagnosis, mechanism selection,
controlled-study design, public-source/task audit and proposal. Preparation outputs
are distinct from future implementation and agent performance results.

| Period | Planned work | Reviewable output |
|---|---|---|
| Late October | Minimal harness, isolation/accounting checks and model/budget agreement | Feasible baseline and agreed pilot limits |
| November | Implement mechanisms, validate diagnostics, pilot and freeze protocol | Frozen comparison and analysis plan |
| December | Main comparisons and midterm report | Task-level results with costs and failures |
| January | Failure coding, uncertainty and cost analysis | Findings and scoped practical recommendations |
| February–April | Thesis writing, review, revision and submission | Complete thesis and reproducibility materials |
| May | Final defense | Research presentation and defense |

Visual: short timeline, with a clear boundary between completed preparation and
planned work. Close by returning to the objective: establish which mechanisms
improve business correctness enough to justify their cost. No separate thank-you slide.

## Backup slides for questions

1. **Literature and contribution boundary:** DataPilot, DS-STAR, NVIDIA, ReasoningBank,
   SQLDriller, TS-SQL, QueryProof and FinHelm; documented contribution, limitation of
   available evidence and precise adaptation in this study. Include full source links.
2. **Failure coding:** eligible population, reporting period, denominator, joins/grain,
   units and exceptions; observable evidence for each MAST code, ambiguous/unknown cases,
   and conditional analytics-specific refinements. Do not infer a review action from
   a wrong final answer alone.
3. **Test validity and leakage controls:** source-defined expected behaviour, valid
   distinguishing fixtures, frozen development memory, hidden evaluation answers outside
   every agent's access, separate natural errors and planted stress cases.
4. **Fair comparison and analysis:** equivalent preparation and tool access, aggregate
   resource caps, task-paired uncertainty, related-task clustering, common candidate
   pool, and separate main effects / interaction. Actual delegation must be recorded.
5. **Feasibility and business cost:** affordable model and total budget agreed before
   paid runs; pilot determines sample size/repeats; preserve core comparisons before
   optional datasets. Preparation hours and runtime spending remain separate, with
   explicit amortisation scenarios and no workplace ROI claim.

## Slide-production and rehearsal rules

Use the supplied visual template, editable diagrams and minimal readable text. Keep
these exact mechanism names throughout: **evidence-checked experience reuse** and
**source-grounded counterexample review**. Spoken explanations can describe the steps
in plain English without inventing alternative labels.

Place short source citations beside literature-dependent claims. Example numbers must
say “illustrative”; planned outcomes must not look like result charts. Include no
fabricated benchmark accuracy, budget, significance or implementation-completion claim.
Rehearse the complete speech with slide timing; move detail to backup if it exceeds
ten minutes. Prepare concise answers on why MAS, novelty, reviewer fallibility, fair
single-agent controls, cost and the value of a null result.

The professors' tips also call for advance arrival, the relevant offline/online
arrangements, and recording questions and answers for the defense secretary. Confirm
personal session instructions using the original notice, rather than copying another
session's meeting details into the presentation.
