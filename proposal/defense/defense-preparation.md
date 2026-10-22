# Proposal defense: presenter script

Updated 23 October 2026. Derived from the full English notes embedded in the 16-slide deck. This replaces the short cues; it contains no Q&A. Source links are in the relevant slide notes.

Planned allocation: 9:30. The script has 1139 words; actual duration requires rehearsal.

## Slide 1. Title (0:00–0:10)

Good morning. My research examines how analytical agents use business knowledge, and whether additional checks improve reliability enough to justify their cost.

## Slide 2. Company data and business context (0:10–0:45)

Imagine a company asking an agent for its May sales. The company has tables containing orders, amounts, dates and statuses. It also has business context: some is structured, such as metric definitions and data dictionaries; some is scattered across documents, emails and analyst notes. The agent must connect these sources before calculating. Our research studies this problem with public tables and documentation. Let me show why the context changes the answer.

## Slide 3. Business rules change the calculation (0:45–1:25)

This company counts completed orders in the month of completion. All three orders were placed in May and sum to 230. Excluding the cancelled order gives 150. However, the last order completed in June, so only 100 belongs to May under the documented rule. All three programs could run successfully. Choosing the right status filter and the right date column requires business knowledge. These numbers are an illustration, not an experimental result.

## Slide 4. Two ways the wrong answer survives (1:25–2:00)

Two separate failures can preserve that wrong answer. First, the analyst retrieves an old procedure and applies it although the current rules differ. Evidence-checked experience reuse would check that applicability before reuse. Second, the reviewer may confirm that the code runs and the sum is correct, while overlooking the business definition. Source-grounded counterexample review would challenge the interpretation with a small test. Whether these changes help is the question we will study.

## Slide 5. Reliability and cost-effectiveness (2:00–2:25)

The main question is how these two mechanisms, separately and together, affect reliability and cost-effectiveness in a hierarchical multi-agent system. We will measure both the targeted failures and final-answer quality. Strong single-agent controls will test whether the hierarchy adds value beyond the procedures themselves. To make the two failure problems precise, I first turn to MAST.

## Slide 6. MAST: a framework for describing failures (2:25–3:05)

MAST is a taxonomy developed from observed multi-agent failures. It groups fourteen failure modes into system design, inter-agent misalignment and task verification. This gives our practical problems a research vocabulary. A finding not passed on and received evidence ignored have distinct codes. Misapplied experience has no automatic inter-agent label. For review, MAST distinguishes a missing required check from an incorrect judgement on a check that was attempted. We will code observable traces; the experiment, rather than a taxonomy label, tests the repair.

## Slide 7. DABstep: a common test for analytical agents (3:05–3:45)

DABstep provides a common test for data-analysis agents, with public materials and a leaderboard hosted on Hugging Face. Agents work through payment tables and documentation to answer multi-step questions, such as finding applicable fee rules and calculating merchant fees. The evaluation split contains 450 questions. Final answers are scored for accuracy, allowing systems to be compared. We will use native task scoring for final quality and separate diagnostics for our two mechanisms. Scorer access must be confirmed before the campaign.

## Slide 8. Existing systems and mechanisms (3:45–4:20)

The leading DABstep systems provide different starting points. DataPilot prepares scoped analytical assets and procedures. DS-STAR combines planning, computation and review. NVIDIA shows how effective a prepared single agent can be. Their published scores use different models and resources, so they do not isolate architecture effects. We plan to adapt the public FinHelm engine. SQLDriller and TS-SQL motivate executable tests, while QueryProof already uses business-rule gates. Our contribution concerns a specific adaptation and controlled evaluation, not inventing testing or memory.

## Slide 9. A fixed hierarchy adapted from FinHelm (4:20–4:50)

Our multi-agent system has a main coordinator and three subagents: an evidence worker, a computational analyst and a reviewer. They have separate working contexts and transfer observable results. The same roles remain in all four multi-agent conditions. FinHelm provides the engine to adapt, subject to development checks. The hierarchy offers explicit boundaries for experience admission and source-first review; its advantage over one agent remains an empirical question.

## Slide 10. Evidence-checked experience reuse (4:50–5:25)

The first mechanism checks a retrieved procedure before it enters the analyst’s context. The evidence worker compares its applicability conditions with current documents. Supported experience is admitted; conflicting or unresolved experience is withheld. In the example, an order-date procedure conflicts with the completion-date rule, so analysis continues from current sources instead. We must measure both fewer inappropriate reuses and retention of useful experience. Rejecting everything would not demonstrate success.

## Slide 11. Source-grounded counterexample review (5:25–6:05)

The reviewer first reads the question and sources, then examines the candidate solution. It creates a small case that separates plausible interpretations. Consider one order placed in May but completed in June. An order-date calculation includes fifty in May; the documented completion-date rule requires zero. The reviewer executes the candidate on this case and judges its behaviour. The documents supply the expectation, not a hidden evaluator answer. Test validity and expected answers can still be wrong, so those also require evaluation.

## Slide 12. Controlled experiment and evaluation (6:05–7:00)

The methodology is a controlled two-by-two factorial experiment with trace-based failure analysis. We compare the baseline, each mechanism separately, and both together. The arrow shows the comparison order, not guaranteed improvement. Tasks, model, source access, initial assets and aggregate resource caps remain comparable. Ordinary and both-mechanism single-agent controls separate procedure effects from architecture effects. DABstep measures final answers. Reviewers also receive the same correct and incorrect candidate solutions, so better solving cannot be mistaken for better checking. We will report false acceptance, false rejection, coverage, failures and uncertainty. A combined win alone does not establish interaction.

## Slide 13. Research contribution and practical use (7:00–7:35)

The research contribution is a reproducible diagnosis and controlled evidence about the two mechanisms, including cases where they fail to help. Recurring trace evidence may justify refinements to MAST. The practical output is guidance for analytics teams: which checks to enable, when preparing knowledge is worthwhile, and when a simpler single agent is sufficient. These are expected outputs. No accuracy improvement has yet been demonstrated.

## Slide 14. Cost-effectiveness and business decisions (7:35–8:25)

This is also a business decision about investment in analytical automation. We separate operating spending from preparation and adaptation effort. Operating measures include model and tool cost, latency, failed runs and retries. Cost per correct answer is reported alongside coverage. Preparation includes the hours needed to organise knowledge and memory, and adapt the system to a task setting. We will compare quality at the same budget and cost at comparable quality. Amortising preparation over future queries requires explicit assumptions. Benchmark findings can guide design choices, but they cannot establish realised workplace productivity savings or return on investment.

## Slide 15. What may limit the benefits? (8:25–8:50)

The reviewer may share the analyst’s mistaken assumptions, or generate an invalid test. Filtering can also discard useful experience and add excessive cost. Too few relevant baseline failures would limit the study’s conclusions. Development validation and honest negative findings are therefore essential. One public benchmark and hierarchy cannot establish universal business deployment.

## Slide 16. Prepared work and next steps (8:50–9:30)

The proposal, literature synthesis, problem map and research design are prepared. Implementation and experiments remain future work. Late October covers the minimal harness and model and budget agreement. November covers implementation, validation, the pilot and protocol freeze. Main comparisons follow in December, with failure and cost analysis in January. February through April covers writing and submission, followed by the final defense in May. The study will establish which checks are worth using in business analytics. Thank you.

## Next preparation step

Rehearse aloud with the slides and presenter notes. After presentation review, prepare the requested HTML knowledge brief as connected explanations, without Q&A.
