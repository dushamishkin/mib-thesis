# Proposal defense — production outline

Updated 23 October 2026 after author review of the first deck.
Current deliverables: [defense package](defense/README.md).
The scientific design is unchanged. No experimental results are available.

## Presentation structure

The author requests more organisational context and visual explanation before naming
failure mechanisms. Retain the university template's section order, while using
**16 main slides, no backup slides**, and short presenter cues. Planned allocation:
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
MAST is introduced only in Literature Review. DABstep, FinHelm and the testing/rule-gate
precedents appear there before the methods that use them. Cost-effectiveness has its
own business-focused slide after contribution and practical use.

## Slide content and purpose

### 1. Title — 0:10

Preserve the current full title, author, programme, supervisor and defense date.
Open with reliable business analytics and the value of extra checking.

### 2. A Company Has Data and Business Context — 0:35

A manager asks: “What were our May sales?” Show three inputs to an analytical agent:
tables of orders/customers/payments, structured context such as metric definitions and
data dictionaries, and unstructured context such as wiki pages, email threads and
analyst notes. The agent must connect records with applicable business meaning.
This is an illustrative organisational setting, not a commitment to live Confluence
integration or proprietary workplace data.

### 3. The Same Tables Can Produce Different Sales Figures — 0:40

Make the company-specific rule explicit: completed orders count in the month of
completion. The hypothetical table contains a 100-unit order completed in May, an
80-unit cancelled May order and a 50-unit May order completed in June.
Show the calculation stages: all orders placed in May total 230, completed orders total
150, completed-during-May orders total 100. These are illustrative arithmetic, not
benchmark results or a universal accounting definition. Choosing the status filter
and the governing date column requires business context.

### 4. How the Wrong Interpretation Reaches the Final Answer — 0:35

Problem one: the analyst retrieves and repeats an old procedure that sums orders by
order date, despite the current definition. Show the procedure, inappropriate reuse
and the 230 answer. Name **evidence-checked experience reuse** as the proposed repair.
Problem two: the reviewer approves 230 after checking execution and arithmetic while
failing to adequately check the business definition. Name **source-grounded
counterexample review**. Keep the two problems distinct and expressed through actors
and actions. Their broader classification comes later.

### 5. Reliability and Cost-effectiveness — 0:25

Present the main research question with selective bold emphasis on the two mechanisms,
**reliability and cost-effectiveness**, and **separately and together**. The remaining
wording uses regular weight. Strong single-agent controls test the hierarchy's added value.

### 6. DABstep: A Shared Test for Data-analysis Agents — 0:40

Introduce the full name, public Adyen/Hugging Face dataset and leaderboard, then show
inputs, the agent's multi-step task and final-answer scoring. Mention the 450-question
evaluation split and answer formats. A paraphrased example task type identifies
applicable fee rules and computes merchant fees. This is a shared evaluation setting,
not proof that every referenced system was built exclusively for this benchmark.
The existing native scorer measures final quality; diagnostics remain separate.

### 7. Existing Systems and Our Implementation Starting Point — 0:35

Compare DataPilot's assets, DS-STAR's review workflow and NVIDIA's prepared single agent
as high-performing DABstep references in the dated 14 October audit. Introduce FinHelm
explicitly as public memory/delegation/verification infrastructure and the reproducible
adaptation path. FinHelm is not presented as a leaderboard leader or a reproduction
of the other systems. Differences in model/resources/preparation prevent causal
interpretation of the published scores.

### 8. MAST and Existing Approaches to the Two Problems — 0:40

Introduce Cemri et al.'s paper and **Multi-Agent System Failure Taxonomy**, with 14
failure modes in three categories. Connect experience use to DataPilot/ReasoningBank,
and review to DS-STAR, SQLDriller, TS-SQL and QueryProof. Explicitly explain executable
tests and business-rule gates as existing ideas before their adaptation in Methods.
Distinguish omitted checks (candidate FM-3.2) from incorrect judgements (candidate
FM-3.3). Experience misuse has no automatic inter-agent label. Classification requires
observable traces and any domain refinement needs recurring evidence.

### 9. A Fixed Hierarchy Adapted from FinHelm — 0:30

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

### 12. Controlled Experiment and Evaluation — 0:55

Present the controlled 2 × 2 factorial comparison: Baseline, each adopted mechanism
alone and Both. Put a downward arrow outside the table to show the comparison from
baseline to both mechanisms. It does not imply guaranteed incremental quality gains.
Keep strong ordinary/both-mechanism single-agent controls with comparable information,
assets, tools and aggregate caps. Native DABstep tests final quality. Common correct
and incorrect candidates isolate reviewer quality. Report coverage and failures and
separate/joint effects; a combined win alone does not establish interaction.
Costs are explained on slide 14 rather than crowded into this slide.

### 13. Research Contribution and Practical Use — 0:35

Use two clearly balanced parts. Research contribution: explain where business knowledge
is lost or misapplied, test mechanism effects and provide a reproducible comparison,
with conditional MAST refinements. Practical use: help teams choose checks, judge
whether knowledge preparation/reuse is worthwhile and identify when a simpler single
agent suffices. Describe understandable outputs, not promised accuracy gains.

### 14. When Is Additional Checking Worth Its Cost? — 0:50

Give business relevance a dedicated slide. Separate operating spending, latency,
failures and retries from hours to prepare knowledge and adapt to a task setting.
Compare quality at the same budget and cost at comparable quality. Report cost per
correct answer with answer coverage. Preparation amortisation requires explicit
query-volume and valuation assumptions. These are planned evaluations, not measured
workplace ROI or demonstrated productivity gains.

### 15. What May Limit the Benefits? — 0:25

Use a single readable list, without a challenge/response table: correlated mistakes,
invalid tests or expectations, loss of useful experience and added cost, insufficient
target-failure prevalence, and limits of one hierarchy/benchmark. Explain safeguards
briefly in cues rather than repeating a second column on the slide.

### 16. Prepared Work and Next Steps — 0:40

Separate completed literature/design/proposal preparation from planned implementation
and experiments. Retain late-October feasibility/model-budget agreement, November
implementation/pilot/freeze, December comparisons/midterm, January analysis,
February–April writing/submission and May final defense. Preserve core comparisons
before adding optional transfer datasets. No agent performance results are claimed.

## Sources and next step

Use the original university master/layout, logo assets, colours and typography.
Keep diagrams, tables and emphasis editable. Source links belong in the relevant
slide notes and clickable citation labels, without backup reference slides.
DABstep's dataset/scoring description and MAST's abstract were rechecked on 23 October;
this is a bounded explanatory-source check, not a new leaderboard audit or full-paper review.
Detailed reading scope and mechanism evidence remain in the
[mechanism packet](../literature/mechanism-selection.md).

The author rejects Q&A preparation as the main reading format. The
[presenter cues](defense/defense-preparation.md) now contain short slide notes only.
After the presentation is settled, prepare a separate HTML knowledge brief in connected
explanations. Do not create that later artifact during this presentation revision.
