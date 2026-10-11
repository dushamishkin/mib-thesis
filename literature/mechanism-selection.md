# Mechanisms and implementation recommendation for the revised proposal

11 October 2026. The author subsequently adopted the recommended pair and implementation
path for the proposal. This is not original-system replication or agent results.
The author selects hierarchical MAS
and DataPilot/DS-STAR as conceptual anchors. This document closes the bounded review,
worked-example and implementation-path questions at design level. The initial review left proposal artefacts unchanged; a subsequent author-authorised
narrative revision is now in proposal/proposal-draft.md. DOCX and generated bibliography
remain unchanged. No model/API calls or installs ran.

Read with the [problem map](problem-mechanisms.md), [system audit](dabstep-systems.md)
and [current design](../proposal/research-design.md). Source-based limitations and our
failure hypotheses must remain distinct. Missing source detail does not establish failure.

## Primary evidence and why it matters

### DataPilot — assets and reuse

[Author description](https://en.oceanbase.com/blog/24781555459), inspected asset/runtime
architecture, three asset layers, branch evaluation/promotion and illustrative loops.
It describes scoped/versioned semantic assets, reusable functions, delegated hypotheses
and regression-based promotion; its domestic-rule example selects against a golden
answer. It motivates studying reusable business knowledge and its preparation cost.
The account does not fully specify label splits or a runtime source-entailment protocol
for every reuse. That omission is not evidence that DataPilot lacks applicability
checking. Our proposed change is a hypothesis to test in our adaptation, not a repair
proven necessary in the original product. Article ranking/generalisation claims are
not adopted as current or controlled findings. No original agent release reproduced.

### DS-STAR — context, sufficiency and correction

[Paper v4](https://arxiv.org/html/2509.21825v4), latest history checked; inspected
Sections 3.1/4.2, Appendix A, algorithm and L.4. File analysis supports planning;
the reviewer assesses sufficiency from question, plan, code and output and routes
refinement. Hard DABstep accuracy is 45.24%, versus 26.98% without analyzer and 34.66%
without verifier. These system ablations do not isolate semantic false acceptance.
The published review template has no explicit document-reading or counterexample
execution stage. That is a protocol observation, not a measured reviewer error rate.
Use it to define a credible ordinary-review baseline; do not claim its reviewer only
checks syntax or that our method is absent from every possible DS-STAR configuration.

### Experience reuse: closest supporting and competing methods

- [ReasoningBank v2](https://arxiv.org/html/2509.25140v2): selected retrieval/schema
  and limitations, latest history checked. Experiences are retrieved by embedding
  similarity and inserted into instructions. Useful simple reuse precedent; its
  web/software settings and ongoing test-time memory differ from our frozen bank.
- [When Continual Learning Moves to Memory v1](https://arxiv.org/html/2604.27003v1):
  history, Sections 2–3 and selected organisation findings. In tested ALFWorld/BabyAI
  sequences, raw experience can hurt transfer while abstraction can help; benefits
  vary by direction and memory organisation. This supports a negative-transfer
  hypothesis, not its prevalence in document-defined analytics.
- [Learning How to Remember / MCMA](https://aclanthology.org/2026.findings-acl.1535.pdf):
  PDF title/metadata, introduction and selected Sections 3.1–3.2 passages inspected;
  ACL Findings 2026,
  DOI 10.18653/v1/2026.findings-acl.1535. A learned memory copilot manages representation
  and abstraction. Include as prior art against claiming selective memory reuse is new.
  Training a copilot is outside our initial student-budget scope; full results/code
  were not audited.
- [The Retriever Should Remember / EARM v1](https://arxiv.org/html/2608.22767v1):
  history, Sections III–V and VIII. Budgeted relevance scoring is amortised through
  persistent query-memory state; LoCoMo evaluation, noisy scorers and shift limits
  constrain transfer. Useful cost comparator conceptually, not evidence of business-rule
  validity. A changing online retrieval state is outside our main frozen-bank study.

### Semantic checks: nearest prior art

- [SQLDriller](https://ipads.se.sjtu.edu.cn/zh/publications/SQLDriller.pdf), Sections
  3–5 and author repository: separates rival SQLs with small counterexample databases,
  comparing execution with an LLM's interpretation of the question. This is the main
  methodological precedent for our second candidate, not an invented testing technique.
  Its fallible NL executor, SQL scope and unambiguous-question assumption constrain
  adaptation to document-grounded Python analytics. Dataset repair using reference SQL
  is distinct from an admissible gold-blind runtime verifier.
- [TS-SQL](https://aclanthology.org/2025.findings-emnlp.156/): current proceedings
  metadata rechecked; selected-method/error reading remains in the reading brief.
  Generated executable tests already exist; wrong expectations and gold-dependent
  preparation are important boundaries. Do not expose its reference SQL to our agents.
- [QueryProof v1](https://arxiv.org/html/2608.09254v1): history and selected Sections
  4/7 rechecked. Semantic-layer gates are existing analytics practice; both gates can
  share a wrong definition. Its comparison lacks equal scaffolding. A new checklist
  or execution gate alone would be insufficient novelty for our work.

These cards are selected readings, not systematic absence evidence or replications.
New discovery records are not yet reconciled in Zotero. No pinned citation key invented.

## Mechanism matrix through the two problems

Cells in the last two columns are our inference/research question unless explicitly
identified as author-reported. A description of a mechanism is not proof it solves a
failure, and a hypothesised boundary is not a demonstrated defect.

| Anchor | Observable operation | What it addresses | Oracle/evidence | Boundary to investigate | Required evidence in our system |
|---|---|---|---|---|---|
| DataPilot assets | Store/retrieve scoped definitions and functions | Repeated reasoning, knowledge reuse | Prepared assets; evaluation labels in example | Can useful experience be retained while task-inapplicable instructions are excluded? | Retrieved item, conditions, current sources, delivered context and ensuing operation |
| DataPilot promotion | Compare branches before committing assets | Regression and reusable-choice quality | Regression/answer feedback | Correctness on preparation tasks need not imply validity in a changed rule scope | Donor/target provenance, disjoint preparation and frozen target policy |
| DS-STAR analyzer | File descriptions inform plan | Source understanding | Data/description output | A description might omit a governing exception | Exact description, accessible source, recipient input; do not infer omission from wrong answer |
| DS-STAR review/router | Sufficiency judgement and refinement | Incomplete/wrong solutions | Candidate plan/code/output and question | Passing ordinary review might not cover a disputed interpretation | Required check versus attempted check and review decision |

Problem 1 focus proposed here: **misapplication of retrieved experience**, not all
retrieval, handoff and context failures. MAST FM-2.5 applies only if received agent
evidence is visibly disregarded; FM-2.4 only if a possessed finding is not passed on.
Negative transfer has no automatic MAST code. Keep the domain mechanism separate.
Problem 2 focus: review coverage omission (candidate FM-3.2) versus wrong judgement
on an attempted check (candidate FM-3.3), supported by observable trace evidence.

## Recommended pair and alternatives

| Candidate | Decision for this bounded study | Reason and caveat |
|---|---|---|
| Evidence-checked experience reuse | Recommend for problem 1 | Intervenes at the memory-to-solver boundary; measurable applicable/inapplicable reuse and preparation cost |
| Source-grounded counterexample review | Recommend for problem 2 | Challenges a specific rule interpretation with executable consequences; oracle and coverage remain fallible |
| Shared rule table only | Do not select alone | Representation does not require actual evidence use; already close to existing semantic layers |
| Blind full recomputation only | Retain as a simpler diagnostic comparator | Can repeat the same assumption; full rerun cost and FinHelm precedent weaken a standalone novelty claim |
| Dependency invalidation/replay | Defer | Requires a reproduced stale-result problem and dependency infrastructure; earlier MemTX card is prior art |
| Learned abstraction / online amortised reranker | Defer | Training or sequential state adds a separate research axis before the narrow failure is established |

This choice is a feasibility/causal-interpretability recommendation, not proven superior
to those alternatives. Development diagnosis must confirm enough relevant failures.
If frozen, publicly sourced experience is already harmless, or checks cannot discriminate
valid rival meanings, narrow/revise the scope rather than manufacture treatment wins.

### First change: evidence-checked experience reuse

Use one frozen bank prepared from permitted development sources/trajectories. Each
entry has an ID, procedure, material applicability conditions, donor source references
and preparation provenance. Entries do not contain hidden answers, held-out solutions
or researcher-only target rules. If preparation uses source-derived procedures without
actual prior runs, call these prepared assets rather than learned experience. Any
trajectory-based bank requires documented development runs after model/budget agreement;
gold may evaluate those runs externally but is not injected as a runtime lesson.
All conditions receive the same bank, metadata,
retriever and ordinary source access; the baseline can already reject a bad suggestion.
Baseline retrieval should already respect available domain/version tags and use ordinary
source review, following the asset-management precedent. Do not disable existing scope
filters to manufacture negative transfer. Test the added source-based condition check
beyond those filters; if they already exclude the legacy item, that run offers no
negative-transfer effect to repair. Freeze retrieval filters before evaluation.

1. Obtain the same initial candidate items in every condition, with the same retrieval
   cap. No treatment-specific oracle passage selection or privileged metadata.
2. Before candidate procedures reach the solver, an evidence worker checks material
   conditions against the current question/schema/docs. Produce `supported`,
   `contradicted` or `unknown`, with current evidence pointers. Source version alone
   is not enough to decide compatibility; a date/title alone does not establish authority.
3. The runtime delivers only supported procedures to the solver. Rejected/unknown
   items remain in the trace; their raw instructions are not silently injected by
   an index or shared session prompt. Ordinary document solving remains available.
4. Retain compatible generic procedures even when a domain-specific rule is rejected.
   Use separate entries initially, rather than asking agents to decompose bundles as
   another treatment. Do not update the bank during held-out evaluation.

The concrete manipulation is context admission at reuse, not a populated gold semantic
layer. The worker can misread conditions, omit one, or reject useful knowledge; validate
those decisions independently in the evaluator. Deterministic validation establishes
IDs/evidence presence and enforces delivery, not the truth of semantic entailment.
Keep bank representation fixed across arms so gains cannot be attributed to better
entries. Compare with ordinary applicability prompting/reranking on a small matched-
resource diagnostic if feasible. Extra calls and reduced context volume are part of
the treatment, not proof of a purely cognitive mechanism.

Measure applicable-item retention, contradicted-item admission, unknown decisions,
downstream rule use, task quality and full cost. Include valid, invalid and absent
experience cases. A toy planted mismatch is a stress case, not natural failure prevalence.
The first change does not perform candidate-answer verification or fixture testing.

### Second change: source-grounded counterexample review

Keep ordinary review in the baseline. For the changed reviewer:

1. From the question and permitted docs, before seeing the candidate, record a bounded
   set of material semantic obligations and source support. Memory approval by the
   first worker is not an authoritative oracle. This initial stage does not have the
   solver's answer/code, but subsequent fixture construction does: do not call the
   entire procedure fully blinded or statistically independent.
2. Inspect the candidate's code/plan and choose a plausible contrasting interpretation
   of one obligation, e.g. null eligibility, join grain, amount/count or date endpoint.
   Freeze prototype caps at at most two disputed obligations and one valid fixture
   per obligation, plus one fixture-regeneration attempt; tune only on development.
3. Construct small schema-valid data for which the candidate and source-derived
   alternative should differ. Record source-derived expected behaviour before executing
   either; expected values come from visible rules, never from evaluator references.
4. Run the unchanged candidate calculation and the alternative on isolated copies.
   A non-discriminating fixture is no evidence. Validate types, required fields,
   constraints and whether the tested semantic rule is meaningful on the fixture.
   On unsupported task types or an invalid fixture, record `inconclusive`, not a pass.
5. Resolve disagreement from source evidence, not majority vote or difference alone.
   Route one bounded correction and recheck the contested case. Unresolved meaning
   is logged as such; do not silently impose a researcher-only business convention.

All arms use a data-root/entry-point interface for replay; no code rewriting that
quietly repairs the candidate before testing. Separate each run's state and disable
network, access to real source data during fixture execution, and cross-run caches.
Fixture validity is not a formal SQL/Python equivalence guarantee. Hard-coded outputs,
hidden globals, domain coverage constraints and wrong expected behaviours can defeat
the check. Report them rather than treating successful execution as semantic proof.
Extra random testing/review at matched compute is a useful bounded comparator.

Measure omission, false acceptance, false rejection, valid/discriminating fixture rate,
correction and subversion, quality and cost. Diagnose the reviewer on the same fixed
correct/incorrect candidate pool across conditions, independent of each solver's output.
Passing selected checks is not certification of full business-semantic correctness.

## Worked example and offline evidence

The complete walkthrough is in [pilot-spec.md](../benchmark/pilot-spec.md), section
"Candidate-mechanism walkthrough". It extends the already permanently-development
fee quotation example; no second canonical task definition or new bank policy is created.
Re-fetched only fees/manual/dev at the existing pinned revision, checked manifest hashes,
and independently recalculated with Decimal and SQLite: 0.120132 for true-or-null,
0.117667 for true-only. A synthetic two-row witness produces 0.200000 versus 0.100000;
a no-null control produces 0.200000 under both. No agents generated these results.

The documented conflicting worksheet and synthetic legacy lesson are diagnostic
adaptations, not unmodified official DABstep tasks or evidence of deployed-system failure.
Numeric references, scripts, this note and the pilot specification are evaluator-only.
An evaluated agent must generate its own applicability decisions/fixtures from its
sanitised task package. Do not give it our witness or expected number as a hidden fix.

## Recommended reproducible implementation path

Recommend adapting the **FinHelm agent/delegation engine**, pinned at
`89e1546cab8fdfd9e996e8f6a6efeec933bc1be5`, for one explicit research baseline.
This is infrastructure reuse; DataPilot/DS-STAR remain the conceptual anchors.
Use a main coordinator and three child roles: evidence/experience worker, computational
analyst, reviewer. Each child has its own context/tool loop. Fix routing in the wrapper
and log actual invocations, rather than hoping the parent chooses to delegate.
Same roles and activation policy in all MAS arms; only the two mechanisms vary.

**Why this path:** selected code inspection confirms child `Agent.run`, separate child
contexts, tool selection, events, aggregate usage and DABstep preparation. The inspected
Docker boundary specifies no network and read-only data. This supplies actual hierarchy
without reconstructing DataPilot's database/asset platform or all DS-STAR modules.
It does not establish that unmodified defaults meet our research protocol.

Required changes before any evaluated run:

- Disable user/global memory and writes; supply only a task-allowlisted frozen experience
  bank. `app.py` shares session context with children; ordinary memory-index injection
  would bypass the proposed admission gate. Separate permitted reviewer context too.
- Replace optional delegation and the default verification nudge with fixed routing.
  The nudge contains candidate numbers/conventions and can skip near the step cap;
  it is not our proposed review protocol. Reserve review resources and report skips.
- Freeze project instructions/skills; remove unrelated database, external/MCP and user
  clarification access. Every comparison receives equivalent source and asset knowledge.
- Isolate the run from gold, development answer files, evaluator code, user home and
  other variants. Existing Docker options require a complete allowlist/tool-access test;
  they are not proof of research leakage isolation. Pin data/scorer instead of `main`.
- Use an identical replayable calculation interface and scratch isolation in all arms.
  Account for all child, failed, fixture, revision and preparation costs.

Selected inspected FinHelm paths: `app.py`, `memory.py`, `subagents/tool.py`,
`subagents/verify.py`, `tools/sandbox.py`, `tools/python/kernel.py`,
`evals/dabstep/prepare.py`, `pyproject.toml`; all under the pinned revision.
Links: [delegation](https://github.com/ZhouJiaJun2333/FinHelm/blob/89e1546cab8fdfd9e996e8f6a6efeec933bc1be5/src/data_agent/subagents/tool.py),
[application](https://github.com/ZhouJiaJun2333/FinHelm/blob/89e1546cab8fdfd9e996e8f6a6efeec933bc1be5/src/data_agent/app.py),
[sandbox](https://github.com/ZhouJiaJun2333/FinHelm/blob/89e1546cab8fdfd9e996e8f6a6efeec933bc1be5/src/data_agent/tools/sandbox.py).
License/negative development findings remain in the system audit. No install or test run
of this framework completed; executable deployment feasibility remains a gate.

**Alternative examined:** IBM OpenDsStar at `2d2cc46f6455db8dd0d0c2c734e8fb92606584dd`.
Read verifier code, selected graph/base-node/execution-environment sections and dependency
manifest. Its sufficiency review uses candidate history/code/output; graph roles and
subprocess execution are inspectable. The package has a broader mandatory dependency
stack and its default graph is not the selected autonomous-child hierarchy. It would
need an outer controller and explicit experience/review isolation. Prefer it only if
FinHelm's interfaces fail the offline acceptance gate, not as a second full experimental
system. [Pinned verifier](https://github.com/IBM/OpenDsStar/blob/2d2cc46f6455db8dd0d0c2c734e8fb92606584dd/src/OpenDsStar/agents/ds_star/nodes/verifier.py).
No framework performance, integration or safety result was reproduced.

### Offline-to-pilot acceptance gates

Before requesting any paid pilot, use fake providers and deterministic fixture code
to prove child separation/message logging, gate blocking (including index bypass),
unmodified replay, invalid/non-discriminating fixture handling and aggregate accounting.
Test that all runtime tools fail to read evaluator/other-task files. Then agree one
model and total pilot budget; freeze caps after cost calibration. No model selected here.
Publish our source, prompts, routing, bank provenance, deviations and pinned manifests.
Call it a DS-STAR/DataPilot-inspired hierarchical baseline, not their reproduced system.

## Evaluation, contribution and proposal readiness

Author-adopted display names: **Baseline**, **Checked reuse**, **Counterexample review**,
**Both**. Two binary factors, one fixed hierarchy. This explicitly revises the earlier
interventions rather than silently renaming C1/V2: checked long-term reuse differs from the earlier task-local C1,
and counterexample review is not necessarily the former independent recomputation V2.
Retain old IDs only historically; the author has agreed the explicit design revision.

Strong single-agent controls should include ordinary self-review and, where feasible,
the same two mechanisms in one context, with equivalent information and aggregate caps.
Comparing an improved hierarchy only to an unimproved single agent cannot isolate the
value of multiple contexts. Matched-compute diagnostics can be bounded; do not multiply
every alternative, model and probe across the whole benchmark programme.

Working predictions for discussion: checked reuse should reduce inappropriate reuse
without excessively excluding useful items; counterexample review should reduce false
acceptance at acceptable false-rejection/coverage cost; their combination may reduce
final errors. None implies better quality on every task, positive interaction or a
cost advantage. Under compatible assets and already-correct solutions, extra checks
may be wasteful. Freeze operational thresholds and evaluation contrasts before test.

Primary comparative track: unmodified DABstep tasks and native scoring. Fixed public
development materials may prepare the bank, but not target-task answers/solutions.
Do not tune on held-out submission scores. Full-score access must be confirmed before
the campaign; official validation is closed and the open unvalidated scoring route
has not been exercised. If only aggregate scores are available, they cannot support
claimed task-level paired intervals or MAST rates. Use separately audited local
references/diagnostic candidates, clearly labelled, for those measurements.

Secondary mechanism track: applicability-shift and reviewer stress cases, including
valid-reuse/no-memory and correct-candidate controls. Keep native results separate
from synthetic/document-conflict derivatives and natural error rates separate from
planted errors. Use the existing benchmark gates for WRB and transfer datasets.

Potential incremental contribution: controlled evidence about **source-checked reuse
and discriminating semantic review separately/jointly**, their targeted failures and
full-cost limits in one hierarchical analytics system with a strong single-agent
control. Gates, memory, abstraction, counterexamples and MAS are existing ideas.
No claim of first combination, universal protocol, guaranteed improvement or absence
of an identical prior method follows from this bounded review.

Business analysis: measure quality/coverage and total cost per correct answer; preparation
and adaptation hours remain distinct from runtime money. Use prespecified query-volume
amortisation scenarios, not invented ROI. DABstep is one environment and cannot prove
deployment anywhere. A bounded public rule-shift diagnostic can test one portability
failure without a new enterprise integration study.

The author agrees this pair and requests a complete narrative before DOCX formatting.
The proposal describes planned methods, the example, controls and development gates.
Completed deployment, natural failure prevalence and experimental gains
are not prerequisites for a proposal and must not be invented. No proposal prose was rewritten during the initial review; the subsequent full
narrative revision follows author agreement.
