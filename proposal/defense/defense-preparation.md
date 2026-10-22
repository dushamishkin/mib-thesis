# Proposal defense: speech and question preparation

23 October 2026. English speaking draft for the 13 main slides. The five backup slides are hidden during the main slide show.

The script contains approximately 1,076 words. The planned slide allocation totals 9:30, allowing pauses and slide changes. This is a timing plan, not a measured rehearsal. Practise aloud with a timer and keep the complete presentation below ten minutes.

## Timed speaking script

### Slide 1. Title (0:00–0:15)

Good morning, professors. My name is Mikhail Dushkin. My proposal examines how analytical agents can use business knowledge more reliably, and whether additional checking justifies its cost.

### Slide 2. Business Calculation Correctness (0:15–1:05)

My motivation comes from analytical work where having tables and documentation still does not ensure a correct answer. Consider this illustrative sales example. There are two completed sales and one cancelled order. The business definition excludes cancelled orders and counts only customers with a completed purchase. A program using every row returns sixty. Applying the definition gives eighty. Both programs execute successfully. The difference is the business interpretation, particularly which records and customers belong in the calculation. This study concerns that kind of correctness.

### Slide 3. Two Problems and Two Proposed Mechanisms (1:05–1:45)

Two separate problems can produce this outcome. First, an agent may reuse a procedure that worked before, although the current business conditions differ. I propose evidence-checked experience reuse: check the procedure against current documents before using it. Second, a reviewer may approve an incorrect interpretation. I propose source-grounded counterexample review: challenge that interpretation with a small executable example. I will explain the theoretical basis and the detailed procedures shortly. First, these problems lead to the research question.

### Slide 4. Research Question (1:45–2:20)

The main question is how these two mechanisms, separately and together, affect the reliability and cost-effectiveness of a hierarchical multi-agent system for business analytics. I will first diagnose failures in the baseline. Then I will measure changes in those failures and in final answers. Finally, I will compare benefits with costs, including strong single-agent controls. The study allows the possibility that a mechanism, or the hierarchy itself, adds little value.

### Slide 5. DABstep and Existing Analytics Systems (2:20–3:05)

DABstep is a benchmark of multi-step analytical questions using tables and supporting documents. Its business rules make it suitable for evaluating more than successful code execution. It also provides a common evaluation setting for our main system references. DataPilot prepares scoped, versioned analytical assets. DS-STAR combines planning, computation and review. NVIDIA demonstrates a strong prepared single agent during inference. These systems achieved leading DABstep results in our dated audit, but their models and preparation differ. Their scores therefore motivate the study rather than establish the causal value of multiple agents.

### Slide 6. MAST and the Two Failure Problems (3:05–3:50)

MAST, the Multi-Agent System Failure Taxonomy, provides a vocabulary for diagnosing agent workflows. It separates system design, inter-agent misalignment and task verification. In our first problem, experience is applied outside its valid scope. DataPilot and ReasoningBank provide relevant precedents, but that misuse has no automatic inter-agent label. In the second problem, MAST distinguishes an omitted check from an incorrect judgement on an attempted check. SQLDriller, TS-SQL and QueryProof establish that executable tests and rule gates already exist. Our question is how a specified adaptation changes these failures, not whether we invented those ideas.

### Slide 7. Hierarchical Multi-Agent System (3:50–4:25)

The planned system has a main coordinator and three subagents with separate working contexts. The evidence worker checks experience, the analyst performs the calculation, and the reviewer challenges its interpretation. These boundaries let us test information filtering and source-first review. I plan one reproducible adaptation using the public FinHelm engine, subject to development checks. I do not assume a hierarchy is superior. Single agents receive comparable procedures and resources.

### Slide 8. Evidence-checked experience reuse (4:25–5:10)

The first mechanism acts before retrieved experience enters the analyst’s context. Each item records a procedure, its applicability conditions and its source. The evidence worker compares these conditions with current documents. Supported items pass through. Contradicted or unresolved items are withheld, while ordinary analysis from current sources remains possible. In our example, an old all-orders procedure conflicts with the completed-sales definition. We must also measure how often the mechanism rejects useful experience. A system that blocks everything would not demonstrate successful reuse.

### Slide 9. Source-grounded counterexample review (5:10–6:00)

The second mechanism changes review. The reviewer first reads the question and sources, before seeing the analyst’s solution. It then creates a small valid case on which plausible interpretations differ. In our sales example, including cancelled orders gives sixty, whereas the documented definition gives eighty. The documents establish the expected behaviour. Merely finding disagreement is insufficient. During experiments, the reviewer must generate its own tests without hidden answers. Tests can be invalid, uninformative, or based on a wrong expectation, so their validity and the review decision must also be evaluated.

### Slide 10. Controlled Experiment and Evaluation (6:00–7:10)

The methodology is a controlled two-by-two factorial experiment with trace-based failure analysis. Each mechanism is switched on or off, producing four MAS conditions. The baseline retains ordinary source use and review. I will use the same tasks, model, initial assets, tools and aggregate resource caps. Strong single-agent controls will use ordinary procedures and both mechanisms. Original DABstep tasks and native scoring measure final quality. Separate diagnostics target inappropriate reuse. For review quality, different reviewers receive the same correct and incorrect candidate solutions. This separates better checking from better solving. I will report false acceptance, rejection of correct answers, coverage and failures, alongside cost and preparation effort. The sequence is baseline diagnosis, implementation, pilot and protocol freeze, followed by held-out comparisons and analysis. A combined improvement alone does not establish positive interaction.

### Slide 11. Expected Results and Innovation Points (7:10–7:55)

The expected contribution is a reproducible, failure-guided study connecting mechanisms to targeted errors and final quality. It will establish separate and joint effects, including cases where additional checking fails to help. Recurring evidence may support analytics-specific refinements to MAST. For business teams, the practical output is guidance on how much to invest in preparing knowledge, reusing procedures and checking answers. I will distinguish preparation effort from runtime spending. These are expected research outputs, not performance results or measured return on investment.

### Slide 12. Challenges and Limitations (7:55–8:30)

The main risk is that the reviewer shares the analyst’s mistaken interpretation or generates an invalid test. Separate contexts do not guarantee independent judgement. The baseline may also contain too few target failures, or checks may cost more than their benefits. Development validation and honest reporting address those risks. Finally, one hierarchy and public benchmark cannot establish universal deployment across businesses. The initial study uses public materials and excludes employer data and production deployment.

### Slide 13. Expected Research Progress (8:30–9:30)

The proposal, literature synthesis, failure map and study design are prepared, along with a public-source audit. The agent implementation and experimental comparisons are future work. In late October I plan the minimal harness, access checks and model and budget agreement. November covers implementation, diagnostic validation, pilot calibration and protocol freeze. Main comparisons and the midterm report follow in December. January focuses on failure analysis, uncertainty and costs. February through April covers thesis writing, review and submission, with final defense expected in May. I will narrow optional datasets before sacrificing the core comparisons. The study ultimately asks which checks improve business correctness enough to justify their cost. Thank you.

## Likely committee questions and concise answers

### Why use multiple agents when a single agent performs well?

The hierarchy provides explicit boundaries for checking retrieved experience and
for source-first review in a separate context. Whether these boundaries help is an
empirical question. I include strong single-agent controls with comparable procedures,
information and resource caps. A single-agent advantage would be a valid finding.

### What makes this a multi-agent system?

A main agent delegates reasoning and actions to child agents with separate contexts.
The system records their results and transfers between roles. A tool call alone does
not establish multi-agent interaction. Actual delegation will be part of the execution record.

### What is new if memory and executable checks already exist?

The contribution is their specified adaptation to document-grounded analytics and a
controlled study of separate and joint effects. I connect final quality to inappropriate
reuse and review decisions, with fair single-agent comparisons and cost measurement.
I do not claim to invent memory, testing or business-rule gates.

### Are these failures already demonstrated in DataPilot and DS-STAR?

Their descriptions establish relevant mechanisms and motivate the failure questions.
They do not establish the prevalence of these errors in our adaptation or prove a
missing mechanism in every original configuration. Baseline trace diagnosis will test
whether enough target failures actually occur.

### Why DABstep?

It combines multi-step analysis with tables and documentation, including rules that
matter for business interpretation. It also provides a shared evaluation setting for
the system references. Original questions and native scoring measure final quality.
Modified diagnostic cases remain separate from official benchmark results.

### Can you access the original code and reproduce the published scores?

The implementation path is a reproducible adaptation using the public FinHelm engine,
subject to validation. DataPilot and DS-STAR are conceptual references. I do not promise
to reproduce their leaderboard scores or treat a different implementation as their original system.

### How can you measure errors when benchmark test answers are hidden?

Native scoring access and the exact benchmark release must be confirmed before the
campaign. Trace coding and separate controlled diagnostic cases provide mechanism-level
evidence. If official scoring is unavailable, I must disclose that limitation and avoid
presenting a development-subset result as a full official score.

### What is the difference between semantic verification and executing code?

Execution shows that a program runs. Semantic verification asks whether its interpretation
and operations match the question and applicable rules. In the sales example, both
calculations run, but only one uses the documented population and denominator.

### How can the reviewer know the correct test output?

It derives expected behaviour from the question and applicable source documents.
That derivation remains fallible. The evaluation audits fixture validity and source
support separately, records invalid or inconclusive checks, and measures wrong approvals
and rejection of correct candidates. Hidden evaluator answers never enter the reviewer.

### Why might this check be better than an ordinary critic?

A small distinguishing case makes the consequences of competing interpretations explicit.
It can expose an error that a general plausibility judgement misses. This is a hypothesis:
test generation can also fail, and ordinary review may already be sufficient on many tasks.

### How do you distinguish a better reviewer from a better analyst?

Reviewers will assess the same pool of correct and incorrect candidate solutions.
This comparison isolates changes in acceptance and rejection decisions. End-to-end
runs then measure the combined workflow. A lower frequency of wrong final answers alone
cannot establish that the reviewer improved.

### How will you use MAST without forcing errors into unsuitable categories?

I apply a label only when observable traces support it. Omitting a required check and
wrongly judging an attempted check are distinct. Out-of-scope experience reuse is not
automatically an inter-agent failure. Recurring cases may justify analytics-specific
subtypes, supported by definitions and checks of coding consistency.

### What if both mechanisms together work better?

I compare the baseline, each mechanism separately, and both together. This estimates
individual and joint changes. A combined win alone does not demonstrate positive
interaction. The analysis must explicitly compare the combined change with the effects
of the individual mechanisms and report uncertainty.

### Which model, sample size and budget will you use?

These are development decisions, not fixed claims in this proposal. I will choose
an affordable backbone with an agreed spending limit and calibrate task counts and
repeats in the pilot. The same model is used across conditions. Optional datasets are
reduced before the core comparisons are removed. No paid campaign starts without budget agreement.

### How does the study fit a business degree?

It concerns the reliability and economic value of analytical automation. I measure
final quality and answer coverage alongside operating cost and knowledge-preparation
and adaptation effort. This can guide investment in analytical systems. Public benchmark
results do not demonstrate realised productivity gains or workplace return on investment.

### What happens if you find no improvement?

A well-controlled null or negative result still identifies where additional checking
or delegation is not worthwhile. I will report targeted failures, useful experience
lost through filtering, reviewer mistakes and costs. I will not select only favourable
tasks or redefine success after seeing held-out results.

### What have you actually completed?

The proposal, literature synthesis, failure map, design and selected public-source
checks are prepared. The agent implementation, paid pilot and main performance
comparisons remain future work. The sales numbers in the presentation are illustrative.

## Rehearsal and defense checklist

- Rehearse once with the full script, then once using only the slides. Measure actual time.
- Aim to finish by 9:30. If behind, shorten literature narration and calendar detail.
  Preserve explanations of both mechanisms and the controlled comparison.
- Know the key distinctions: evidence versus experience, execution versus semantic
  correctness, final quality versus reviewer quality, joint gain versus interaction.
- Open the PPTX in the presenting application and check slide-show mode. Slides 14–18
  are hidden; use “See All Slides” or the application's slide navigation for questions.
- Keep the PDF as a visual fallback. It contains the main presentation only.
- Follow the original session notice for arrival, printing and online access. The
  supplied tips require a written record of committee comments and answers afterwards.
- After the defense, record actual feedback and agree any changes with the supervisor.

## Evidence and version boundaries

Scientific details: [research design](../research-design.md). Literature evidence and
reading limits: [mechanism-selection packet](../../literature/mechanism-selection.md)
and [system audit](../../literature/dabstep-systems.md). The main outline remains
[defense-outline.md](../defense-outline.md). Source URLs are embedded in slide notes
and the clickable references backup slide. Existing source checks were performed
11–14 October; no current leaderboard ranking or new full-paper review is claimed.
