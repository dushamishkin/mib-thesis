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

## Broader mechanisms pass — 11 October 2026

Author rejects selecting the proposed improvements yet and requests deeper mechanisms
from outside business analytics. The operational explanation is in
[problem-mechanisms.md](problem-mechanisms.md); do not turn these readings into chosen
interventions. Six cross-domain sources were inspected in selected sections, not
fully replicated or searched as a systematic review. New records remain outside the
generated Zotero bibliography pending identifier reconciliation.

- **Lost in the Middle**, [TACL 2024 paper](https://aclanthology.org/2024.tacl-1.9/),
  controlled QA/key-value setup and position/context experiments. Relevant information's
  position affects performance in tested models. Useful diagnostic of supplied versus
  usable context: change position while preserving content. Not a neural causal proof,
  handoff-compression study or measured limitation of our future model.
- **Large Language Models Can Be Easily Distracted by Irrelevant Context**,
  [ICML 2023 paper](https://proceedings.mlr.press/v202/shi23a.html), GSM-IC construction
  and selected robustness experiments. Adds irrelevant text without changing the answer
  and observes sensitivity. Useful harmless-distractor control; old models/math tasks
  do not establish modern business-rule error rates or a universal treatment.
- **Self-RAG**, [ICLR 2024 proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf),
  Section 3/Table 1 and training/inference description. Separates retrieval need,
  passage relevance, claim support and response utility using learned reflection tokens.
  Useful vocabulary for diagnosing where evidence fails. Document support is not itself
  a test of applicability to a particular business scope/date. Training and model
  decoding are required by the actual method; it is not simply an API prompt template.
- **Chain-of-Verification**, [ACL Findings 2024 paper](https://aclanthology.org/2024.findings-acl.212/),
  Section 3 and joint/factored results. Draft-derived verification questions are answered
  in contexts excluding the original draft in separated variants; improvements occur
  on tested factual tasks. Useful precedent for checking input dependence and atomic
  questions. No executable business tests/tool use were studied. Question generation
  still sees the draft: hidden answer and complete requirement coverage are different
  properties, with the latter a diagnostic concern we infer rather than a reported result.
- **ReasoningBank v2**, [paper](https://arxiv.org/html/2509.25140v2), Section 3,
  judge-noise analysis and Appendix E; latest arXiv history checked. Distils strategies
  from success/failure trajectories, retrieves by embeddings and injects items into
  instructions. Proxy success labels come from an LLM without gold at runtime.
  Useful example of experience content rather than raw-history reuse. Authors report
  robustness to simulated label noise in their tested range; systematic shared semantic
  errors are not equivalent to those flips. Broader memory architectures are not fully
  compared; web/SWE results do not establish an analytics-MAS failure or remedy.
- **Debate or Vote**, [NeurIPS 2025 proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/file/934252acd87f254d5d4672fbde283bd2-Paper-Conference.pdf),
  Sections 3–5, answer extraction Appendix F and limitations H. Separates sampling/voting
  gains from debate, and correct-to-wrong subversion from correction. Useful controls
  and transition metrics. Martingale analysis assumes a particular homogeneous belief
  update model; empirical protocol is mainly simultaneous talk, not every MAS topology.
  Oracle locking uses correct-answer knowledge and is an explanatory upper bound,
  never an admissible runtime component for our study.

These papers supply distinct diagnoses and methods to examine, not proof that context
ordering, reflection, memory or debate is the intervention to select. The practical
question is which mechanism recurs in our baseline under a valid development protocol.

## Focused follow-up: evidence use and erroneous verification — 11 October 2026

Author prioritises these two problems; checking cost remains a secondary criterion.
The following is selected-section reading, not replication or a systematic review.
No change to the proposal, approved title or frozen experimental parameters is implied.

### Author correction and stronger-method follow-up

The author explicitly requires **two distinct problems within one study**, classified
with MAST. The earlier shared specification and blinded review proposals were judged
insufficiently compelling; they remain unselected comparison candidates, not the
implementation recommendation. Do not merge information-use failures with checking
failures or require the old factorial to survive unchanged.

MAST mapping, based on v3 Appendix A and annotation methodology Section 3:

| Problem | MAST label when supported by visible evidence | Required distinction |
|---|---|---|
| Evidence/experience underuse | FM-2.4 Information withholding | One agent possesses a relevant finding but fails to convey it |
| Evidence/experience underuse | FM-2.5 Ignored other agent's input | A finding is conveyed but inadequately considered by its recipient |
| Evidence/experience underuse | FM-1.4 Loss of conversation history | Actual history truncation/loss, not any unsuccessful memory retrieval; conversation reset is FM-2.1 |
| Evidence/experience underuse | FM-2.6 Reasoning-action mismatch | A visible plan states a rule that the performed operation contradicts |
| Erroneous business-interpretation checking | FM-3.3 Incorrect verification | A review inadequately validates/cross-checks the interpretation or decision |
| Missing coverage in checking | FM-3.2 No or incomplete verification | A required semantic dimension is not checked; distinguish omission from incorrect judgement |

These are operational mappings, not new MAST definitions. A wrong answer alone cannot
establish any label. Retrieval failure and inappropriate cross-task experience transfer
have no automatic one-to-one label here; record the observed mechanism separately
rather than force it into FM-2.4 or FM-1.4. One trace may contain failures from both
problems. Preserve separate counts and evidence spans; use a manually audited subset
and report annotation agreement if independent annotation is available. MAST classifies
observations; controlled comparisons, not labels, establish intervention effects.

New selected-method readings, not replications or code-execution audits:

- **AgentSpec v3**, [method](https://arxiv.org/html/2503.18666v3), Sections 3, 5.3,
  6.3; latest arXiv history checked. Trigger/predicate/enforcement rules act at runtime,
  rather than leaving compliance to instructions. Useful design precedent for enforcing
  rule consumption at analytical checkpoints. Safety tasks do not establish analytics
  gains; automatically generated rules have coverage/rigidity errors. Final ICSE 2026
  metadata is also available in the author's proceedings PDF, DOI 10.1145/3744916.3764546.
- **SQLDriller**, [SIGMOD 2025 paper](https://ipads.se.sjtu.edu.cn/zh/publications/SQLDriller.pdf),
  Sections 3–5 and [repository README](https://github.com/SJTU-IPADS/SQLDriller).
  Candidate queries are distinguished by small counterexample databases; SQL outputs
  are compared with LLM interpretation of the natural-language request on those data.
  Useful concrete checking mechanism beyond reviewing a plausible answer. Its NL
  executor is fallible and ambiguity is excluded in the correctness definition.
  Distinguish dataset repair involving original gold SQL from runtime candidate
  optimisation. Python analytics would require a bounded adaptation, not automatic
  reuse of formal SQL tooling. This supersedes the earlier abstract-only reading marker.
- **MemTX v2**, [method](https://arxiv.org/html/2607.23929v2), Sections 3.4–3.6 and
  selected failure discussion. Retraction invalidates recorded downstream dependencies.
  Useful precedent for invalidating calculations after rule corrections. It does not
  provide environment replay or recover undeclared provenance; we propose neither its
  full transactional stack nor formal guarantees for analytics.
- **QueryProof v1**, [preprint](https://arxiv.org/html/2608.09254v1), Sections 4 and 7;
  arXiv history checked. Deterministic semantic-layer checks already gate analytical
  answers. Important close prior art against claiming a novel rule gate. Checks remain
  incomplete, and shared semantic-layer errors can escape both gates. Reported comparison
  is confounded by scaffold/information differences, with disclosed test exposure;
  its headline gain is not transferable evidence for our proposed MAS intervention.
- **MemoryLake DABstep implementation**, [author repository](https://github.com/memorylake-ai/memorylake-eval-dabstep),
  README architecture/trust sections only. Typed analytical intents, executable skills
  and rival semantic candidates are already described on DABstep. This is an engineering
  comparator, not a verified peer-reviewed result or audited implementation. Its reported
  offline snapshot uses model-generated references, so do not compare that percentage
  as an official benchmark score. Code, learning/evaluation isolation and dependencies
  remain to audit before using it as a baseline or claiming a gap.
- **AgentDebug v1**, [selected Section 3.2](https://arxiv.org/html/2509.25370v1):
  targeted diagnosis and re-rollout are relevant repair precedents. The narrative
  counterfactual-testing description differs from Algorithm 1's LLM-only critical-error
  detection comment. This discrepancy and use of success evaluation require protocol
  inspection before treating it as a gold-blind runtime repair method. Not a chosen
  intervention and not a replacement for MAST annotation.

Stronger bounded candidates, to compare with the previous simpler proposals:

1. **Enforced evidence use and dependency repair:** agents supply source-linked,
   versioned analytical requirements; the runtime requires observable checks tied to
   those requirements before finalisation. Record which computations depend on which
   rule. A correction invalidates dependent results and triggers bounded recomputation.
   The concrete change is enforcement/invalidation, not merely another context table.
   Check presence does not prove rule coverage or correctness; audit extraction and
   test validity. Rules are agent-derived from permitted documents, not hidden gold.
2. **Counterexample-based semantic verification:** a challenger constructs a bounded
   alternative interpretation (e.g. amount vs count denominator) and a small fixture
   on which its calculation differs from the analyst's. Execute both; judge applicability
   from question and permitted documentation. Disagreement exposes consequences but
   does not identify the correct interpretation by itself. Resolve from evidence or
   record unresolved status. No evaluator reference enters generation or adjudication.

Use separate ablations and a compute-matched alternative to distinguish these mechanisms
from more retries, context volume or candidate sampling. They are more operationally
specific, not demonstrated to be more effective. Admit them only if a small development
diagnostic reproduces the corresponding problem and implementation costs are feasible.
DABstep selection and official-versus-diagnostic evaluation protocol are canonical in
../benchmark/README.md. Keep final task accuracy and the two distinct failure rates;
retain cost/coverage and do not infer interaction from a combined win.

### Evidence ledger and closest methods

- **MAST v3:** [paper](https://arxiv.org/html/2503.13657v3), taxonomy Appendix A,
  selected failure examples N.9/N.11 and intervention discussion. FM-2.4 information
  withholding, FM-2.5 ignored input, and FM-3.3 incorrect verification describe observed
  MAS failures. Useful vocabulary for trace coding; these are not measured prevalence
  estimates for document-defined business rules. Trace classification alone does not
  identify an effective repair or support causal claims.
- **Silo-Bench v2:** [paper](https://arxiv.org/html/2603.01045v2), Sections 3 and 5.1–5.3.
  Its Communication-Reasoning Gap includes wrong answers after logs confirm receipt of
  all data. Useful for separating information delivery from successful integration.
  Tasks are distributed algorithmic calculations, not business-rule interpretation;
  verification-like behaviours in logs are not equivalent to formal verifier decisions.
- **DS-STAR v4:** [paper](https://arxiv.org/html/2509.21825v4), verifier/router methods,
  evaluation and selected Appendix A/L.4 passages. KramaBench accuracy rises from
  44.69 to 52.55 with oracle relevant-data access, diagnosing a retrieval boundary.
  The verifier already sees query, plan, code and execution output. Useful analytics
  comparator; neither result establishes its rate of approving wrong business rules.
  Verifier-removal comparisons also change planning, limiting pure causal attribution.
- **AgenticData v2:** [paper](https://arxiv.org/html/2508.05002v2), Sections 5–7,
  especially 7.3. Long-term memory gives little benefit across diverse Spider databases.
  Useful warning about task-dependent experience transfer, not proof that memory is
  generally ineffective or that incorrect business rules persist. Semantic validation,
  feedback routing and retrieved knowledge already exist in this system.
- **AMA v4:** [paper](https://arxiv.org/html/2601.20352v4), Sections 3–4.
  Fact/episode memory, source indices, retrieval judgement and conflict updates are
  already prior art. Default conflict updating favours latest state; business rules
  may instead require scope, effective-date and authority checks. That extension is
  our inference, not a measured AMA failure. Conversational memory evaluation does
  not directly test correctness of business calculations.
- **When Does Verification Pay Off? v2:**
  [paper](https://arxiv.org/html/2512.02304v2), Sections 5.3–5.4 and limitations.
  Solver–verifier solution similarity is associated with more acceptance of incorrect
  solutions across tested model pairs. Useful false-positive/false-negative methodology
  and motivation to examine shared errors. This is not a causal test of showing a
  reviewer the analyst's plan, nor a business-analytics MAS study. Latest v2 history
  checked; acceptance is an ICLR 2026 workshop, not the main conference.
- **TS-SQL:** [proceedings](https://aclanthology.org/2025.findings-emnlp.156/),
  DOI 10.18653/v1/2025.findings-emnlp.156; Sections 3, 4.3.2, 4.4.3 and Limitations.
  Collaborative test-data/code generation and execution feedback already address SQL
  semantic errors. Sampled misleading corrections include wrong tests and ambiguous
  deduplication requirements despite correct tests. Test accuracy limits performance.
  Useful closest comparator and a warning that executable tests are fallible.
  Test-data preparation uses gold SQL: audit this dependency before reusing the method
  in a verifier that must have no evaluator access. These cases do not establish
  false-acceptance prevalence for business-document rules in AgenticData/DS-STAR.

### Diagnosis before choosing a contribution

Separate four mechanisms: a relevant source is not retrieved; its finding is lost in
handoff/compression; the available finding is applied incorrectly; or an old episode
is reused outside its scope. Do not treat all four as a single memory failure.
Cross-session learning would expand the existing task-local design and is not proposed
as the initial implementation. Our narrow candidate is evidence use within one task.

The literature supports integration failures, incorrect verification and residual SQL
semantic errors. The specific claim that an analytics MAS accepts a wrong interpretation
of available business-document rules remains a hypothesis to reproduce. Available
evidence does not justify a new universal memory protocol or priority claim.

### Proposed bounded extension for author review

Study the chain **source passage → applicable rule → analytical operation → check**.
The contribution candidate is controlled evidence about this chain, not the invention
of agent memory, executable tests or independent checking. Two proposed interventions:

1. **Evidence-linked shared rules (C1 candidate):** agents populate metric, population,
   period, units, aggregation grain, join relationships, exceptions, source passage and
   applicability. Resolve conflicts from permitted evidence or mark ambiguity. This
   empty structure is never populated with evaluator answers. Its structure and
   reconciliation remain a bundle unless separately ablated.
2. **Independent source-based checking (V2 candidate):** the reviewer first derives
   requirements and an executable check from the question and the same permitted
   corpus, without analyst code/answer/messages or the C1 record. Log this attempt,
   then compare interpretations and calculations with the analyst. Construct boundary
   fixtures where appropriate, linking each expected behaviour to a source rule.
   Merely rerunning SQL is insufficient. Independent attempts and tests can still
   share errors; blinding has not been established as a remedy by the cited studies.

This is a refinement candidate within the existing V0/V2/C1/V2+C1 labels, not approval
to freeze the old factorial or adopt two large new systems. Baseline ordinary review
must already have code/results and equal source access. Retain a strong single-agent
and extra-compute control; no superiority or positive interaction is assumed.

Illustrative synthetic retail task, not an admitted experiment: documentation explicitly
defines net revenue as sales minus partial refunds recognised in the same quarter.
One qualifying sale of 100 and qualifying partial refund of 30 implies 70. Excluding
the entire refunded order gives 0. A reviewer repeating the analyst's interpretation
could agree; a source-derived partial-refund fixture could expose the discrepancy.
This is a proposed mechanism demonstration, not an observed agent trace.

### Concrete evaluation proposal, before any paid run

First audit one baseline's available code, source access, review prompts and feedback
routes. Use a small manually audited diagnostic set before choosing a full campaign.
Two distinct evaluations are needed:

- **Natural failures:** run the baseline on held-out, resolvable public-document tasks;
  inspect visible retrieval, messages, rule records, code and review decisions to locate
  where evidence ceased to constrain the answer. Do not infer private reasoning.
- **Verifier stress test:** submit correct candidates and controlled wrong-rule mutations
  (missing exception, wrong date scope, duplicate-producing join, wrong unit). Measure
  acceptance of wrong candidates and rejection of correct ones. This diagnoses checking;
  artificial errors cannot estimate the natural prevalence of those errors.

A diagnostic arm can provide the same relevant passages to every condition, separating
retrieval from downstream use. This is an oracle-context diagnostic, not a production
advantage for C1/V2. Keep evaluator references hidden, audit fixture expectations against
documents, include correct alternative queries, and distinguish unresolvable ambiguity
from answerable conflicts. Freeze treatment prompts/resource controls on development
tasks before held-out evaluation. Report task-level uncertainty and costs including
failed checks, revisions and timeouts; cost is retained but not the main question.

### Reading and implementation follow-ups

TS-SQL and When Does Verification Pay Off? remain discovery records pending Zotero
identifier reconciliation/import and generated-export review. SQLDriller's reading
scope is updated above. G²SQL (DOI 10.1016/j.eswa.2026.131276) remains a close-method
lead with metadata/abstract-level inspection only; its full methods/code must be read
before asserting absence of source-aware or independent verification. The provisional
extension above is therefore not a completed novelty determination.

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
