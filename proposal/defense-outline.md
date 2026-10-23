# Proposal defense — production outline

Updated 23 October 2026 after author review of the first deck.
Current deliverables: [defense package](defense/README.md).
The scientific design is unchanged. No experimental results are available.

## Presentation structure

The author requests more organisational context and visual explanation before naming
failure mechanisms. Retain the university template's section order, while using
**16 main slides, no backup slides**, and a full English presenter script. Planned allocation:
**9:30**, subject to spoken rehearsal within the professors' ten-minute limit.
The five-slide starter does not impose a slide-count limit.

| Template section | Slides | Planned time |
|---|---|---|
| Title | 1 | 0:10 |
| Background | 2–4 | 1:50 |
| Research Question | 5 | 0:25 |
| Literature Review | 6–8 | 1:55 |
| Research Plan & Method | 9–12 | 2:40 |
| Expected Results & Innovation Points | 13–14 | 1:25 |
| Challenges & Limitations | 15 | 0:25 |
| Expected Research Progress | 16 | 0:40 |

Background introduces the company, tables and business context. A worked example
then establishes why a technically correct computation can answer the wrong business
question. The two failure problems and mechanism names follow from that example.
Literature Review starts with MAST to theorise the two problems, then introduces
DABstep, existing systems, FinHelm and testing/rule-gate precedents
before the methods that use them. Cost-effectiveness has its
own business-focused slide after contribution and practical use.

## Slide content and purpose

### 1. Title — 0:10

Preserve the current full title, author, programme, supervisor and defense date.
Open with reliable business analytics and the value of extra checking.

### 2. Company data and business context — 0:35

A manager asks: “What were our May sales?” Show three inputs to an analytical agent:
tables of orders/customers/payments, structured context such as metric definitions and
data dictionaries, and unstructured context such as wiki pages, email threads and
analyst notes. The agent must connect records with applicable business meaning.
This is an illustrative organisational setting, not a commitment to live Confluence
integration or proprietary workplace data.

### 3. Business rules change the calculation — 0:40

Make the company-specific rule explicit: completed orders count in the month of
completion. The hypothetical table contains a 100-unit order completed in May, an
80-unit cancelled May order and a 50-unit May order completed in June.
Show the calculation stages: all orders placed in May total 230, completed orders total
150, completed-during-May orders total 100. These are illustrative arithmetic, not
benchmark results or a universal accounting definition. Choosing the status filter
and the governing date column requires business context.

### 4. Two ways the wrong answer survives — 0:35

Problem one: the analyst retrieves and repeats an old procedure that sums orders by
order date, despite the current definition. Show the procedure, inappropriate reuse
and the 230 answer. Name **evidence-checked experience reuse** as the proposed repair.
Problem two: the reviewer approves 230 after checking execution and arithmetic while
failing to adequately check the business definition. Name **source-grounded
counterexample review**. Keep the two problems distinct and expressed through actors
and actions. Their broader classification comes later.

### 5. Reliability and cost-effectiveness — 0:25

Present the main research question with selective bold emphasis on the two mechanisms,
**separately and together**, with reliability and cost-effectiveness in red. The remaining
wording uses regular weight. Strong single-agent controls test the hierarchy's added value.

### 6. MAST: a framework for describing failures — 0:40

Begin Literature Review with Cemri et al.'s **Multi-Agent System Failure Taxonomy**:
14 modes in three groups. This links the already introduced problems to prior theory.
For evidence use, FM-2.4 concerns a possessed finding not passed on; FM-2.5 requires
received evidence being ignored. Inappropriate experience reuse has no automatic
inter-agent code and may require finer domain coding. For review, distinguish omitted
required checks (candidate FM-3.2) from incorrect judgements on attempted checks
(candidate FM-3.3). Observable traces support labels; controlled comparisons test repairs.

### 7. DABstep: a common test for analytical agents — 0:40

Introduce the full name, public Adyen/Hugging Face dataset and leaderboard, then show
inputs, the multi-step task and final-answer scoring. Mention the 450-question evaluation
split and answer formats. A paraphrased task type identifies applicable fee rules and
computes merchant fees. This is a shared setting, not proof that every referenced system
was built exclusively for it. Native scoring measures final quality; diagnostics remain
separate and scorer access must be confirmed before the campaign.

### 8. Existing systems and mechanisms — 0:35

Compare DataPilot's assets, DS-STAR's review workflow and NVIDIA's prepared single agent
as high-performing references in the dated 14 October audit. Introduce FinHelm as public
memory/delegation/verification infrastructure and the adaptation path. It is not presented
as a leaderboard leader or a reproduction of the other systems. Model, resource and
preparation differences prevent causal interpretation of published scores.
Explain SQLDriller/TS-SQL executable tests and QueryProof business-rule gates here,
before their adaptation in Methods. These are existing ideas, not our priority claims.

### 9. A fixed hierarchy adapted from FinHelm — 0:30

Show a main coordinator and evidence, computation and review subagents. Explain separate
working contexts and observable result transfers. Keep the same roles in all MAS
conditions. The fixed hierarchy is a hypothesis about useful boundaries, not an
assumption of superiority. The implementation remains planned, subject to validation.

### 10. Evidence-checked experience reuse — 0:35

Show retrieval, current-source applicability checking and admission. Supported items
pass to the analyst; contradicted or unresolved items are withheld. Return to the
order-date/completion-date procedure conflict. Ordinary analysis from current sources
remains available. Measure both reduced inappropriate reuse and retention of useful
experience, using the same frozen bank and ordinary source access in all conditions.

### 11. Source-grounded counterexample review — 0:40

Reviewer reads sources first, then generates a valid distinguishing example. Use one
50-unit order placed on 29 May and completed on 2 June. An order-date calculation puts
50 in May; the current completion-date rule requires zero. Source-defined expectations
establish which interpretation is correct. Test validity and expected answers remain
fallible. Runtime reviewers never receive hidden evaluator answers or researcher fixtures.

### 12. Controlled experiment and evaluation — 0:55

Present the controlled 2 × 2 factorial comparison: Baseline, each adopted mechanism
alone and Both. Put a downward arrow outside the table to show the comparison from
baseline to both mechanisms. It does not imply guaranteed incremental quality gains.
Keep strong ordinary/both-mechanism single-agent controls with comparable information,
assets, tools and aggregate caps. Native DABstep tests final quality. Common correct
and incorrect candidates isolate reviewer quality. Report coverage and failures and
separate/joint effects; a combined win alone does not establish interaction.
Costs are explained on slide 14 rather than crowded into this slide.

### 13. Research contribution and practical use — 0:35

Use two clearly balanced parts. Research contribution: explain where business knowledge
is lost or misapplied, test mechanism effects and provide a reproducible comparison,
with conditional MAST refinements. Practical use: help teams choose checks, judge
whether knowledge preparation/reuse is worthwhile and identify when a simpler single
agent suffices. Describe understandable outputs, not promised accuracy gains.

### 14. Cost-effectiveness and business decisions — 0:50

Give business relevance a dedicated slide. Separate operating spending, latency,
failures and retries from hours to prepare knowledge and adapt to a task setting.
Compare quality at the same budget and cost at comparable quality. Report cost per
correct answer with answer coverage. Preparation amortisation requires explicit
query-volume and valuation assumptions. These are planned evaluations, not measured
workplace ROI or demonstrated productivity gains.

### 15. What may limit the benefits? — 0:25

Use a single readable list, without a challenge/response table: correlated mistakes,
invalid tests or expectations, loss of useful experience and added cost, insufficient
target-failure prevalence, and limits of one hierarchy/benchmark. Explain safeguards
briefly in presenter notes rather than repeating a second column on the slide.

### 16. Prepared work and next steps — 0:40

Separate completed literature/design/proposal preparation from planned implementation
and experiments. Retain late-October feasibility/model-budget agreement, November
implementation/pilot/freeze, December comparisons/midterm, January analysis,
February–April writing/submission and May final defense. Preserve core comparisons
before adding optional transfer datasets. No agent performance results are claimed.

## Sources and next step

Use the original university master/layout, logo assets, colours and typography.
Keep diagrams, tables and emphasis editable. Use a consistent type hierarchy, lighter
headings, body text of roughly 18 pt and table text of 15–17 pt, with clear spacing.
Reserve bold for the cover, table headers and selected phrases in the RQ. Full notes
contain continuous English narration, with source links separated from spoken text.
Sources also have clickable labels on the relevant slides; there are no backup slides.
DABstep's dataset/scoring description and MAST's abstract were rechecked on 23 October;
this is a bounded explanatory-source check, not a new leaderboard audit or full-paper review.
Detailed reading scope and mechanism evidence remain in the
[mechanism packet](../literature/mechanism-selection.md).

The author rejects Q&A preparation as the main reading format. The
[presenter script](defense/defense-preparation.md) contains the full English narration
exported from slide notes.
The [HTML knowledge brief](defense/defense-brief.html) is now delivered as connected
explanations, with a separate tab containing the exact full speech from saved PowerPoint
notes. It is a fixed preparation snapshot, not an automatically synchronised presentation.
