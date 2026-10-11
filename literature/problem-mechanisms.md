# Two research problems: technical mechanisms for author discussion

11 October 2026. Author requests deeper diagnosis before choosing an improvement.
This is an operational problem map and thinking worksheet, not a new intervention,
approved topic, systematic review or reproduced agent result. Selected source-reading
cards and limitations are canonical in [reading-brief.md](reading-brief.md).
The two problems remain distinct under MAST, even when they occur in one trajectory.

## Problem 1: evidence or experience does not adequately constrain the analysis

Do not infer this problem merely from a wrong answer. Establish what information was
available, what each agent actually received, and the first observable divergence.
An illustrative applicable rule is not just a metric name: it can carry population,
time, unit, grain, relationship, exception and authority/scope conditions. These are
our analytical dimensions, not a new definition taken verbatim from a cited paper.

| Stage | Technical object and possible failure | Evidence needed | Diagnostic contrast, not a chosen fix |
|---|---|---|---|
| Source access | Corpus permissions, file inventory, parsing, tool outputs; the document may never be readable | Permitted inventory and successful read output | Same task with accessible/readable source; do not call an access failure memory failure |
| Retrieval | Query rewrite, chunking, embeddings, ranking and top-k; the general metric passage is selected but its exception is absent | Retrieved passages, identifiers and scores where available | Supply the same relevant passages to every condition; distinguish retrieval from downstream use |
| Working context | Truncation, ordering, competing instructions, tool-output size; evidence is supplied but not used reliably | Exact visible input, positions and budget | Move identical evidence without changing its meaning or total length |
| Representation/handoff | Reader summaries, planner messages, intermediate tables; an applicability qualifier is omitted | Compare source finding, outgoing message and recipient input | Compare original passage with summary at matched resources; an added-token advantage needs control |
| Interpretation | Scope/authority reconciliation; topical relevance is mistaken for applicability to this task | Claimed rule, governing passage and justification | Change only applicability metadata or supply resolvable conflicts; never impose hidden policy |
| Application | SQL/Python filters, joins and aggregation; a correctly stated requirement is not implemented | Explicit plan and performed operation | Inspect or execute a discriminating case; a plan/code mismatch differs from an already wrong plan |
| Experience reuse | Stored trajectories/strategies, success labels, retrieval conditions; a past convention is reused outside its valid scope | Memory item, origin, retrieval and current conditions | With/without that item on matched in-scope/out-of-scope tasks; cross-session learning is separate scope |
| Updating | Corrected context and already-computed intermediate results can disagree | Rule versions, dependency record and recomputation trace | Show whether correction changes dependent computation; immutable stale output is not evidence of ignored input without a received correction |

The working-context probes are motivated by Lost in the Middle/GSM-IC; retrieval and
support distinctions by Self-RAG; experience probes by ReasoningBank. Transfer to
modern analytics MAS is a hypothesis. Full-information integration remains a separate
failure possibility, as discussed in the existing Silo-Bench card. These diagnostics
must not silently become a seven-dimensional experiment.

MAST's FM-2.4 requires a possessed finding not communicated; FM-2.5 requires received
agent input inadequately considered. FM-1.4 applies to actual history loss, and FM-2.6
to a visible stated-plan/action discrepancy. Not every retrieval or interpretation
error fits those labels. Preserve an unclassified/domain-specific mechanism when the
required MAST evidence is absent. Label observations, not hidden intentions/reasoning.

## Problem 2: a check fails to reject an incorrect business interpretation

Make the object of checking explicit. The following levels are an explanatory ladder
for this study, not a claim that every reviewed system implements them in this order.

| Object checked | What passing establishes | What can still be wrong |
|---|---|---|
| Syntax/runtime | The program parses/executes in this environment | Entire metric interpretation |
| Numerical plausibility | Result satisfies chosen range/shape constraints | Wrong population or denominator with plausible number |
| Plan/code agreement | Implementation follows the stated plan | The plan embodies an incorrect rule |
| Citation support | A cited passage supports a stated claim | The passage is inapplicable, superseded, or excludes an exception |
| Source applicability | Selected rule is supported for the task's scope/date/authority | Implementation or test expectations |
| Discriminating executable test | Candidate satisfies this test under its expected behaviour | Missing cases or an incorrect test oracle |

### Distinct failure mechanisms to inspect

1. **Coverage omission.** Reviewer checks execution or selected claims but never checks
   the disputed population/exception. FM-3.2 is a plausible label given visible omission.
   A checker can accurately answer all its questions while asking an insufficient set.
2. **Incorrect semantic judgement.** Reviewer checks the disputed meaning but accepts
   an unsupported interpretation. Inspect source evidence and decision, not just a
   reassuring final phrase. FM-3.3 is the primary candidate.
3. **Dependence on the candidate response.** Review input contains the answer/plan to
   assess; CoVe provides a factual-QA precedent for examining conditioning separately.
   It does not prove that all exposed analytical reviewers copy answers.
4. **Correlated errors.** Different roles/calls can share a misleading source, default
   convention or solution distribution. Agreement then supplies less independent
   information than the agent count suggests. Similarity/false-acceptance association
   is reported in the existing verifier-study card; causality is not established.
5. **Consensus replacing evidence.** A correct minority can revise to a wrong peer
   answer. Debate or Vote distinguishes correction and subversion; its formal result
   has restrictive assumptions and is not a theorem about every MAS. Inspect answer
   transitions and the cited reason for changing, not merely final consensus.
6. **Faulty test oracle.** Test expected outputs come from an interpretation too.
   SQLDriller/TS-SQL are relevant precedents; executing a generated check does not
   certify its expectation. Cases where rival queries agree are non-discriminating.
7. **Shared authoritative error.** Analyst and reviewer consult the same mistaken
   semantic layer. Additional checks against that layer cannot independently establish
   documentary correctness. QueryProof explicitly describes this boundary.
8. **Feedback loop into memory.** An accepted answer may supply the success label for
   future reusable experience. A verifier error could therefore change later priors.
   ReasoningBank's judge dependence motivates this hypothesis, but its tested label
   noise robustness is contrary evidence to a blanket claim that noise ruins memory.

Items 3–8 describe proposed explanatory mechanisms, not additional MAST labels.
One trajectory can contain both FM-2.x and FM-3.x; separate their evidence and counts.
Shared-input errors can persist even with no communication failure, and lost evidence
can cause a wrong calculation even when a later reviewer correctly rejects it.

## Why final accuracy alone cannot distinguish the problems

For an explicit approval event A and wrong candidate W:

`P(wrong and accepted) = P(wrong candidate) × P(accepted | wrong candidate)`.

This is a probability identity, not an independence assumption. A better generator can
reduce wrong accepted answers without improving the reviewer. A better reviewer can
reduce acceptance of wrong candidates without improving evidence use upstream.
Compare both end-to-end outcomes and reviewer decisions on the same controlled pool;
also measure rejection of correct candidates and coverage. In workflows without an
explicit reviewer gate, final acceptance needs its own operational definition.

## Worked mechanism distinctions: illustrative, not observed traces

Suppose public synthetic documentation explicitly defines an eligible population and
an amount-based rate. Keep that definition visible to all conditions.

- Reader finds the exception but omits it from the handoff: information transfer.
- Reader conveys it; planner disregards it: received input not used.
- Planner states it; SQL omits its filter: plan/action mismatch.
- Planner selects the wrong denominator despite intact evidence: interpretation error,
  not automatically any of the preceding labels.
- Reviewer checks only successful execution: coverage omission.
- Reviewer considers the denominator and endorses the wrong one: incorrect judgement.
- Correct calculation appears early, but debate replaces it: possible subversion.
- The wrong convention is stored as a successful strategy: possible experience loop.

For each case, ask what one observation would distinguish it from its neighbour.
Do not infer the whole chain from a single wrong final number.

## Questions for developing a contribution, without selecting one yet

1. Where exactly does available evidence stop constraining the solution?
2. Is the bottleneck missing evidence, lost qualifiers, wrong applicability, or failed
   integration of complete information? What diagnostic would refute each explanation?
3. What does the reviewer see and check? Does it detect mistakes, choose among
   candidates, or generate a competing solution? Those are different tasks.
4. Does interaction rescue correct candidates more often than it overturns them?
5. What is already stored as experience, and how was its success/applicability labelled?
6. Which narrow mechanism recurs enough on development traces to justify changing it?
7. Can the hypothesised improvement beat a simpler matched-compute comparison on
   original tasks and transfer, with negative results and abstentions retained?

Evaluation targets and access gates live in [benchmark/README.md](../benchmark/README.md).
Original benchmark metrics must remain separate; a new diagnostic score must not be
presented as an official benchmark result. Do not rewrite the frozen proposal artifacts
or launch a paid campaign before agreeing a mechanism, model/budget and valid protocol.
