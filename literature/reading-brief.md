# Key source reading brief

Prepared 10 October 2026 for author review. This is a transparent, selected-section
reading brief, not an exhaustive review or a completed novelty assessment. Metadata
and reading/version status remain in [references.md](references.md); proposed research
claims remain in [positioning-note.md](positioning-note.md). No model experiments were
replicated. The links pin the versions supporting these summaries.

## Review contract

For each key source, show the author: primary link/version; plain-language summary;
sections inspected; why it is needed; what it does not establish; proposed use in the
proposal; outstanding checks. Separate reported findings from our interpretation.
Before changing the central gap or excluding a close comparator, present the evidence
and rationale for discussion. Routine factual verification and drafting can continue.
Do not infer absence of a method from an abstract or a short search result.

## Analytics-system limitations pass — 11 October 2026

Author requested limitations before selecting a research improvement. The proposal
text and DOCX remain unchanged. This pass covers selected architecture, evaluation,
appendix and limitations passages, not full-paper replication or a systematic review.
AgenticData v2, DataCross v1 and DS-STAR v4 are the latest versions listed in the
arXiv histories checked today. DataSeer uses the ACL 2026 proceedings PDF.
DS-STAR and DataSeer are discovery candidates, not yet reconciled into Zotero or
the generated bibliography. No implementation was executed or code release audited.

Evidence labels below distinguish **author statement**, **reported result** and
**reviewer inference**. An untested failure hypothesis is not an established limitation
of performance. Evaluation coverage limits do not prove architectural incapability.

### AgenticData: plan validation and feedback memory

Primary source: [v2](https://arxiv.org/html/2508.05002v2), Sections 2, 5, 6 and 7.
The pipeline profiles sources and relationships, generates semantic plans, validates
them, routes error feedback through memory, and executes an optimised plan.

- **Reported result, Section 7.3:** long-term memory has little effect on
  Spider-2.0-Lite, which spans different databases. The authors attribute this to
  difficulty sharing experience across databases. This is a concrete boundary on
  memory transfer, not evidence that all memory is useless.
- **Author statement, Section 6:** error/context volume, unproductive planning cycles
  and routing feedback to the appropriate agent are challenges. Their memory design
  addresses these; the passage is not a measured residual failure rate.
- **Reviewer inference, Sections 5.1 and 6:** semantic detectors inspect a generated
  plan using the question and relevant knowledge, and memory recycles detector feedback.
  A missed interpretation error could therefore persist through correction. The paper
  does not establish how often this happens; independent source-based diagnosis is needed.
- **Evaluation coverage:** reviewed experiments compare components and benchmark
  accuracy; they do not establish robustness to controlled contradictory rule documents
  or the calibration of acceptance decisions. Separate computation and rule correctness
  is a possible diagnostic addition, not a demonstrated literature-wide gap.

**Why use it:** closest existing analytics architecture, and prior art for validation
plus memory. First check which semantic mistakes survive its existing detectors rather
than propose the generic addition of validation. No standalone limitations section was
identified in the reviewed v2; the results above are section-specific boundaries.

### DS-STAR: iterative planning, execution, verification and routing

Primary source: [v4](https://arxiv.org/html/2509.21825v4), Sections 3–6,
Appendices A, E and L. Analyzer descriptions feed planning and coding; a verifier
judges the current plan, code and execution result; a router adds a step or backtracks.

- **Author statement and result, Section 4.1:** retrieval remains a bottleneck.
  KramaBench accuracy increases from 44.69% to 52.55% when relevant files are already
  provided. This comparison supports a data-discovery boundary within this setting.
- **Author statement, Appendix E:** increased context raises input-token use to
  about 3.5 times ReAct. Cost analysis averages ten development tasks; its reported
  dollar figures are historical observations, not current prices or our budget.
- **Author statement, Section 6:** human domain-expert collaboration is future work;
  the evaluated framework is fully automated. This is outside our initial no-human-study scope.
- **Reviewer inference, Section 3.1 and Appendix L.4:** the verifier is exposed to
  the candidate solution and emits a binary sufficiency decision. Its listed prompt
  has no separate source-document input. Candidate influence and inadequate evidence
  checking are testable risks, not demonstrated causes of incorrect answers. Code can
  contain source access/results, so this does not mean the system never reads documents.
- **Methodological caution:** Appendix A already varies verifier model and inputs;
  merely using a cheap verifier or adding code/results to its prompt is prior art.
  Section 4.2's no-verifier comparison also changes step-by-step planning to full-plan
  generation; it does not isolate a pure verifier effect from all planning changes.

**Why use it:** concrete checking/routing baseline and an existing methodology for
component comparison. Its code-and-result-aware validation corrects the oversimplified
claim that existing analytical systems check only whether code runs.

### DataCrossAgent: source specialists and cross-source synthesis

Primary source: [v1](https://arxiv.org/html/2601.21403v1), Sections 3.2–5.3
and source-prioritisation/cross-pollination prompts. Specialists explore sources,
a coordinator ranks them, and a cross-analysis agent executes joins and tests.

- **Author-described evaluation boundary, Section 3.2:** task artifacts are
  reverse-synthesised from verified target insights. This enables reference checking,
  but is not a test on untouched enterprise archives with naturally conflicting rules.
- **Author-described measurement, Sections 3.5 and 5.1.3:** assessment combines
  numerical matching, embeddings and GPT-4o judgments. These report-level scores are
  not the proportion of completely correct executable tasks.
- **Reviewer inference, Section 4.3:** source priority partly depends on data richness,
  keyword overlap and coordinator judgment. A short exception document may be crucial
  without being rich or lexically prominent. This is a candidate test, not a reported failure.
- **Evaluation coverage:** source interaction and execution are already implemented
  and ablated. The inspected setup does not show that their advantage persists against
  an equally resourced single-agent implementation. Direct multimodal-model baselines
  and the iterative AgentPoirot comparator are not equivalent to that control.

**Why use it:** concrete alternative division of work by source, with existing
cross-pollination and numerical verification. No separate author limitations section
was identified; the 'Limitations' text in the reporting prompt concerns generated reports.
Multimodal extraction is outside our current scope; compare coordination rather than
silently expanding the thesis to image parsing.

### DataSeer: manager, planner/executor loop and multiple branches

Primary sources: [ACL record](https://aclanthology.org/2026.findings-acl.787/)
and [proceedings PDF](https://aclanthology.org/2026.findings-acl.787.pdf).
Inspected Sections 3–4, Limitations (printed p. 16039; PDF p. 10), Appendices A.1–A.2
and B.4.2. The manager maintains memory and edits prompts; planner and executor
explore; multiple trajectories are merged. Default base model is DeepSeek-V3-250324,
with additional GPT-4o experiments. This does not authorize our use of a paid model.

- **Explicit author limitation:** performance inherits model hallucinations,
  prompt sensitivity and difficulty with very long contexts.
- **Explicit author limitation:** additional reasoning rounds/branches introduce
  substantial token costs and latency. Adaptive computation or lightweight reasoning
  distillation is suggested as future work.
- **Reported result, Appendix B.4.2:** increasing branches from one to two to three
  raises InsightEval summary G-Eval from 0.6544 to 0.6901 to 0.7008, with diminishing
  gains. These are judge scores, not task-correctness rates or a measured optimal policy.
- **Reviewer inference, Section 3.1.3:** the executor accepts discoveries using its
  own confidence/novelty/diversity scores. Calibration of this self-assessment against
  independently verified correctness is a candidate diagnostic question.
- **Reviewer inference, Section 3.2:** the description permits later branches to use
  earlier insights; agreement should not be treated as statistically independent
  verification. Separate planner/executor instances alone do not establish independence.
- **Evaluation boundary, Appendix A.1:** insight/summary evaluation uses GPT-4o
  G-Eval. Claimed 'validated' insights are not thereby independently checked calculations.

**Why use it:** an analytics MAS with explicit efficiency limitations and concrete
memory/coordination prior art, from a Chinese research/industry context. Adaptive
allocation is a grounded candidate, but broad novelty and implementation feasibility
remain to be checked before choosing it.

### What this pass permits us to say

Existing systems already implement semantic validation, feedback memory, cross-source
communication and iterative correction. 'Add a critic/shared memory' is insufficient
as a contribution. Three candidate problems remain open for author discussion:

| Candidate problem | Present evidence | Diagnostic step before selecting an improvement |
|---|---|---|
| Checking effort is expensive and not equally useful on every task | Explicit DataSeer limitation; DS-STAR token overhead | Compare saved work against lost correctness under fixed/adaptive effort and matched total caps |
| Verification can accept an incorrect interpretation | Verifier/self-assessment architectures; failure rate and mechanism not established | Audit ordinary baseline attempts; distinguish rule errors, computation errors and final acceptance |
| Useful context is not retrieved, transferred or reused appropriately | DS-STAR retrieval contrast; AgenticData transfer boundary; DataCross ranking risk | Locate the relevant evidence along retrieval, message/summary and executable-plan stages |

These are alternative starting points, not three required thesis contributions.
No topic, intervention, model/budget or experiment design was newly approved.

## Why Do Multi-Agent LLM Systems Fail

[Cemri et al., arXiv:2503.13657v3](https://arxiv.org/html/2503.13657v3).

**Summary:** the authors classify observable failures in multi-agent systems into system
design, inter-agent misalignment and task verification, and examine interventions in
case studies. The abstract reports 14 failure modes across these three categories.
Appendix H discusses interventions whose effects depend on the system and setting.

**Inspected:** abstract, verification/communication discussion in Appendix G and selected
Appendix H passages; prior selected taxonomy reading is recorded in the index. This is
not a new full-paper reading.

**Why we need it:** it motivates separate attention to coordination and checking and
provides a vocabulary for visible-trace diagnosis. It also challenges the assumption
that adding agents or verification automatically improves results.

**Limits:** its taxonomy does not identify causes in our analytics tasks; its intervention
results are not our expected effect sizes. Our controlled comparisons must establish
effects independently.

**Proposed use:** background on MAS failure and a descriptive annotation framework.
Verify exact definitions when writing the annotation guide; check newer versions and
publication metadata before final proposal citation. Do not import an unqualified
percentage improvement as the motivation for our experiment.

## AgenticData

[Sun et al., arXiv:2508.05002v2](https://arxiv.org/html/2508.05002v2), revised title
“AgenticData: A Multi-Agent based Data Analytics System for Heterogeneous Data”.

**Summary:** an analytical MAS builds and validates plans for heterogeneous sources,
uses feedback memory and evaluates components including validation and memory through
ablations. It already combines these mechanisms; we cannot claim to invent that idea.

**Inspected:** architecture overview; Section 5 validation; selected Section 6 memory
passages; Section 7.3 ablations and surrounding evaluation descriptions. The source
audit previously inspected other selected methods/evaluation passages. No replication.

**Why we need it:** this is the closest currently identified system comparator. It
forces us to explain precisely what our intervention definitions, matched document
variants, resource controls and acceptance outcomes add to an existing analytics design.

**Limits:** the inspected sections do not establish our exact factorial comparison,
but that observation is not proof that the paper or all prior literature lacks it.
Its validation protocol is not automatically equivalent to our independent recomputation;
its memory includes cross-task use, while our core context resets between tasks.

**Proposed use:** the central closest-work comparison, not a passing citation. Complete
the design comparison before freezing the gap. Reconcile the v2 title in Zotero;
Consensus returned an older-title/three-benchmark abstract, while v2 describes five.

## DABstep

[Egg et al., arXiv:2506.23719v1](https://arxiv.org/html/2506.23719v1).

**Summary:** tasks require multi-step calculations and knowledge from payment-domain
documentation. Section 3.1 explains question/context packages and parameterised task
instances derived from fewer core questions; Section 2.3 describes accessible execution.

**Inspected:** selected setup and task-curation passages today; the prior release audit
and selected paper reading are recorded in [benchmark](../benchmark/README.md).

**Why we need it:** it supplies a practical, executable foundation for the proposed
development tasks and shows that analytics plus external documentation is existing work.
Parameterisation also warns us that related queries are not independent observations.

**Limits:** our conflict pairs and semantic references will be a derivative suite, not
official benchmark scores. The paper describes industrial origins; the released payments
README explicitly labels transactions synthetic. Preserve this distinction and do not
call the released tables employer/proprietary data.

**Proposed use:** task motivation and feasibility, with a compact explanation of source
adaptation. Final admission still needs author review of rule applicability and references.
Check current paper metadata/version before the final reference list.

## LongDA

[LongDA, arXiv:2601.02598v2](https://arxiv.org/html/2601.02598v2).

**Summary:** analytics tasks require locating and applying evidence in extensive public
survey documentation before executable computation. Section 6 explicitly notes fixed-year
snapshots and lack of cross-year/versioned-document robustness testing; it also describes
the emphasis of evaluation on final numbers.

**Inspected:** selected construction/statistics and Section 6 limitations; prior
construction/evaluation/source checks are recorded in the benchmark audit. No replication.

**Why we need it:** it supports the distinction between calculation and documentary
interpretation and motivates checking applicable rules and evidence alongside numbers.
HERD is a possible transfer source after the core pilot.

**Limits:** its documented drift limitation is local to LongDA. It cannot establish a
literature-wide absence of rule-drift evaluation or a unique advantage of MAS.

**Proposed use:** documentation-intensive evaluation and a bounded methodological
comparison; avoid adopting upstream numeric tolerances without task-specific validation.
Check current version and complete author/venue metadata before citation.

## LiveSQLBench

[BIRD team author repository](https://github.com/bird-bench/livesqlbench), README
inspected 10 October 2026, including Overview and Large-v1 description. This is a
changing release source, not a paper read or independently replicated experiment.
The earlier pinned data/release audit is in the benchmark manifest.

**Summary:** the release combines SQL tasks, external hierarchical knowledge and
executable evaluation. The README explicitly includes business-rule drift across
releases in the Large-v1 setting.

**Why we need it:** it prevents an overbroad claim that existing analytical benchmarks
ignore changing business rules. We need to distinguish release-to-release drift from
matched conflicting documents with unchanged tables and controlled intervention effects.

**Limits:** the README is release documentation. It does not itself settle the closest
paper comparison or whether an equivalent V2×C1 experiment has been performed.

**Proposed use:** an explicit novelty boundary and evaluation precedent. Locate/verify
the appropriate paper citation or cite the release documentation with access date;
do not invent author lists or BibTeX keys. No new Zotero record was created in this task.

## Current-version follow-ups inspected 10 October

### AMA current-version follow-up

[Huang et al., AMA v4](https://arxiv.org/html/2601.20352v4); arXiv submission history
checked 10 October confirms v4 as the latest listed version. Selected Sections 3.3–4:
the Judge filters retrieved memory for relevance and conflicts and triggers refreshing.
The evaluation uses conversational-memory benchmarks and several model backbones.
**Use:** acknowledge existing multi-agent conflict-aware memory. **Boundary:** this is
not evidence for our independent analytical recomputation or rule-conflict factorial.
The selected review does not establish all changes from v1 or reproduce the experiments.

### MemTX current-version follow-up

[Li et al., MemTX v2](https://arxiv.org/html/2607.23929v2); latest version in the
checked arXiv history. Selected repair limits and Sections 4–5: transactional belief
commit/repair is evaluated with a deterministic grader, common tools/runner and
downstream mock refund episodes. **Use:** provenance repair, controlled comparison and
harm-sensitive evaluation are prior art. **Boundary:** repair covers recorded provenance,
not environment replay; the outcome setting differs from analytical reporting. This is
selected-section reading, not a complete v1–v2 diff or an independent implementation audit.

### Silo-Bench current-version follow-up

[Zhang et al., Silo-Bench v2](https://arxiv.org/html/2603.01045v2); latest version in
the checked arXiv history. Selected Sections 3 and 5 describe algorithmic distributed
tasks and failures of integration despite information transfer. **Use:** strengthens the
case for testing coordination rather than assuming it succeeds. **Boundary:** it does
not establish effects of our analytics interventions or team necessity on our tasks.
No complete version diff or model-result replication was conducted.

These follow-ups inform the [design comparison](positioning-note.md), which separates
existing contributions from proposed empirical questions and unresolved equivalence.

## What remains before the gap can be frozen

### Proposal citation check — 10 October

The complete [proposal](../proposal/proposal-draft.md) uses seven papers from this
brief plus LiveSQLBench release documentation and official
[Qwen3.7-Flash documentation](https://help.aliyun.com/zh/model-studio/qwen3-7-flash).
The latter advertises function calling and structured outputs: it supports model
calibration feasibility, not performance on our tasks or a scientific novelty claim.
All nine primary reference URLs and the cited paper versions were checked again
for the final draft. The proposed 12–18-reference outline target was not a quota;
uncited framework/general background records were not added just to increase the count.
Remaining metadata reconciliation and reading limits are explicit in the
[review notes](../proposal/proposal-review-notes.md).

The next pass should compare the closest studies on independent checking, shared
context, conflict manipulation, equal information/resources, interaction analysis and
semantic acceptance. Unknown entries remain unknown. Prioritise AgenticData and the
relevant current memory/conflict papers already flagged in references.md. Bring material
changes to the author with evidence. A source supporting our motivation may also narrow
our novelty; both uses belong in the review.
