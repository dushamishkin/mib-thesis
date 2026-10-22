# Proposal defense — presentation outline

Prepared 23 October 2026. Discussion outline; no slide deck or experimental results yet.
Author reports that the proposal is ready and requests the outline before slide production.

## Format and sources

Plan: **12 main slides, 9 minutes 30 seconds of speech**, leaving 30 seconds within
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

## Narrative

An executable calculation can answer the wrong business question. Existing systems
combine prepared knowledge, computation and review, but their aggregate scores cannot
isolate the value of each procedure. We study two distinct failures and test two
specific changes within one reproducible hierarchy. Controlled comparisons establish
whether either change helps, whether both help together, and whether the benefit
justifies the effort compared with strong single-agent alternatives.

Use one hypothetical sales example throughout. It is an explanation, not a benchmark
result or a claim about the frequency of these errors. Do not start with a contents slide:
the first substantive slide should make the problem understandable.

## Main slides

### 1. Title — 0:15

**Improving Evidence Use and Semantic Verification in Multi-Agent Business Analytics:
A Failure-Guided Controlled Study**

Mikhail Dushkin · 125120990077 · Master of International Business
Supervisor: Prof. Liu Jialu · SJTU Antai · 23 October 2026

Opening sentence: “I study how analytical agents can use business knowledge more
reliably, and whether additional checks are worth their cost.”

Visual: university title layout. Preserve the full title; do not read it aloud word for word.

### 2. The calculation runs. But does it answer the business question? — 0:55

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

### 3. Existing systems provide the starting point — 0:45

Use three short rows:

- **DataPilot:** prepares reusable, versioned analytical assets and procedures.
- **DS-STAR:** organises planning, computation and iterative review.
- **NVIDIA's DABstep system:** demonstrates the strength of a prepared single agent at inference.

They are relevant high-performing DABstep references in the project's dated audit.
Their scores involve different models, tools and preparation; they do not show that
more agents cause better results. ReasoningBank and SQLDriller provide the more
specific memory and counterexample-testing precedents used later.

Visual: system / relevant mechanism / implication for our study. Keep rankings and
long bibliographic details in backup. Do not claim a demonstrated defect in an
unreproduced system from its technical description alone.

### 4. Two failure problems, not one — 0:45

Introduce **MAST: Multi-Agent System Failure Taxonomy**, covering system design,
inter-agent misalignment and task verification. Then show the two study targets:

1. **Inappropriate use of evidence or experience.** An available rule can be lost,
   ignored or applied outside its valid scope. The intervention focuses on the last:
   admitting a retrieved procedure that contradicts the current definition.
2. **Incorrect semantic verification.** A reviewer may omit a necessary business-rule
   check or consider that rule and still approve the wrong interpretation.

In the sales example, reusing an all-orders procedure is the first problem; approving
its answer after checking only arithmetic is the second. Incomplete and incorrect
verification correspond to candidate MAST FM-3.2 and FM-3.3 labels. Experience misuse
is not automatically an inter-agent failure; labels require observable traces.

Visual: two separate failure points along evidence → calculation → review. The wider
problem map guides diagnosis; we do not promise to repair every failure.

### 5. Research objective and key questions — 0:40

Objective: **improve the reliability and cost-effectiveness of hierarchical multi-agent
business analytics through two targeted, literature-grounded mechanisms.**

Present three accessible questions, grouping the internal RQs without changing them:

- Which evidence-use and review failures occur in the chosen baseline?
- What are the separate and joint effects of the two improvements on these failures
  and final-answer quality?
- Do any gains justify additional cost, including comparison with strong single agents?

Visual: three questions, no formal hypotheses block. Explain that a negative result
is informative: extra memory checks, review or delegation may not be worthwhile.

### 6. One reproducible hierarchy, with a reason for each role — 0:40

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

### 7. Evidence-checked experience reuse — 0:50

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

### 8. Source-grounded counterexample review — 1:00

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

### 9. How we isolate the effects — 1:05

Name the methodology: **controlled 2 × 2 factorial experiment, supported by trace-based
failure analysis**. Explain factorial simply: switch each improvement on and off.

| Condition | Evidence-checked experience reuse | Source-grounded counterexample review |
|---|---|---|
| Baseline | Off | Off |
| Evidence-checked experience reuse | On | Off |
| Source-grounded counterexample review | Off | On |
| Both | On | On |

The same tasks, model, source access, initial assets and aggregate resource caps make
comparisons interpretable. Add strong single-agent controls with ordinary procedures
and with both improvements, so architecture is not confused with better instructions.

Visual: four-condition matrix plus single-agent comparison underneath. Separate,
joint and interaction effects are different quantities; “Both wins” alone does not
establish positive interaction. Statistical detail belongs in backup.

### 10. What we will measure — 1:05

Show two evaluation tracks:

- **End-to-end:** original DABstep tasks and native scoring for final-answer quality;
  separate diagnostic cases expose rule changes and inappropriate experience reuse.
- **Review-only:** give different reviewers the **same correct and incorrect candidate
  solutions**, measuring whether checking improves independently of the solver.

Measure three groups: final correctness and answer coverage; inappropriate reuse and
review false acceptance / false rejection; runtime cost, latency and preparation/adaptation
hours. Report timeouts and failures. Compare cost per correct answer and quality under
comparable budgets; do not treat lower answer coverage as improved reliability.

Visual: two lanes feeding a compact quality / failure / cost scorecard. DABstep is
primary. Secondary benchmark use requires release and compatibility checks; do not
promise every dataset or merge diagnostic results into the official benchmark score.

### 11. Expected contribution and remaining risks — 0:45

Expected outputs are an auditable diagnosis, a reproducible implementation and controlled
evidence about which improvements help, when they fail, and what they cost. Recurring
trace evidence may support analytics-specific refinements to MAST.

The contribution is a bounded adaptation and evaluation of existing ideas, not the
invention of memory, executable checks or a universally superior MAS. Business relevance
is guidance on investment in preparation, reuse and checking, rather than measured ROI.

Visual: expected outputs beside two central risks: shared misinterpretation of sources
and insufficient benefit for the extra cost. Broader deployment and transfer remain
empirical limits. No experimental improvement has been demonstrated yet.

### 12. Current progress and research plan — 0:45

**Prepared:** literature synthesis, two-problem diagnosis, mechanism selection,
controlled-study design, public-source/task audit and proposal. These are preparation
outputs, not implemented agent performance results.

**Planned:** late October — minimal harness and budget agreement; November — implement
and validate mechanisms, pilot, freeze protocol; December — main comparisons and midterm
report; January — failure and cost analysis; February–April — thesis writing, revision
and submission; May — final defense.

Visual: preparation/planned-work boundary and a compact timeline. End with the central
question: “Which checks improve business correctness enough to justify their cost?”
Do not spend a separate slide saying only “Thank you”.

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
