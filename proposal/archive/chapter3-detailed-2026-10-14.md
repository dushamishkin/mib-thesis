# Detailed Chapter 3 — preserved technical snapshot

Preserved on 14 October 2026 at the author's request before simplifying the proposal.
Source: proposal/proposal-draft.md at commit 44a6630. The complete chapter below is
unchanged. This is a historical technical reference, not the active proposal chapter
or a frozen experiment protocol. Current specifications remain in
[research-design.md](../research-design.md) and the mechanism-selection packet;
numbered citations below refer to the [proposal references](../proposal-draft.md).

# 3 Research methods, scheme and feasibility

## 3.1 Fixed hierarchy and implementation

The baseline will use a main coordinator and three child roles: evidence/experience worker, computational analyst and reviewer. Each child will have a separate context and tool-using loop. Explicit routing will invoke the same roles in every multi-agent condition and record messages, tools, calculations and resource use. Exact prompts, limits and correction routes will be development-validated and frozen before testing. Routing will not depend on favourable held-out results.

The selected implementation path is adaptation of the pinned FinHelm delegation engine [13]. DataPilot and DS-STAR remain conceptual anchors, not systems whose scores this adaptation reproduces. Unrestricted memory, optional delegation and default verification behaviour will be replaced by research-specific access and routing. If the engine fails offline checks, a documented fallback will be assessed before the pilot; changing implementation requires a recorded protocol revision.

The baseline already has ordinary execution, source access, scoped retrieval and candidate review. It can reject an inappropriate suggestion or detect a semantic mistake. No condition will be instructed to copy obsolete knowledge. All conditions share the same initial bank, metadata, retrieval rules, permitted documents and calculation interface. The interventions strengthen interfaces beyond this ordinary workflow.

## 3.2 Evidence-checked experience reuse

A frozen bank will contain reusable procedures with identifiers, material applicability conditions, donor-source pointers and preparation provenance. It will be prepared only from permitted development material. Entries derived from documents without prior runs will be called prepared assets, not learned experience. Trajectory-derived entries require documented development runs; external gold may evaluate those runs, but hidden answers will not be inserted into runtime lessons or target prompts.

Ordinary retrieval will respect available scope/version metadata in every condition. After the same candidate items have been retrieved, the treatment adds a check against the current question, schema and documentation. For each material condition, the worker records supported, contradicted or unknown with source pointers. Only supported procedures reach the solver. Rejected and unknown items remain in the trace; their raw instructions must not bypass admission through shared prompts, an index or another tool. Ordinary document-based solving remains available when no procedure is admitted.

Generic calculation procedures and domain-specific rules will initially be separate entries. This permits retention of a useful pattern while blocking an inapplicable rule. Memory will not change during held-out evaluation. Deterministic checks enforce identifiers, evidence fields and delivery, not semantic truth. The worker can misread sources or reject useful knowledge; evaluator auditing will measure these errors. This addresses admission at reuse, not every retrieval failure or an oracle-populated semantic layer.

## 3.3 Source-grounded counterexample review

The changed reviewer first receives the question and permitted documentation, before candidate answer/code. It records a bounded set of material semantic obligations and source support, without treating the evidence worker's approval as an oracle. It then inspects the candidate and identifies a plausible contrasting interpretation, such as different null eligibility, date endpoint, join grain or denominator.

It constructs a small schema-valid fixture on which the candidate and source-derived alternative should differ. Expected behaviour is recorded from visible rules before execution. The unchanged candidate and alternative run on isolated copies through the same replay interface. A difference establishes different consequences, not which interpretation is correct; source evidence resolves that judgement. Agreement on a non-discriminating fixture provides no verification evidence.

The development prototype will cap checking at two disputed obligations, one valid fixture per obligation and one regeneration attempt. Caps remain provisional until calibration, then fixed. Invalid fixtures, unsupported replay and unresolved meaning yield inconclusive status, not approval. One bounded correction and recheck will be available under the fixed resource policy. Failed attempts and skipped reviews will remain in the record and cost accounting.

The initial source interpretation is separated from the candidate, but later fixture construction uses candidate code. The complete reviewer is not fully blinded or statistically independent. The treatment bundles source-first specification and discriminating execution; its effect concerns that bundle rather than pure test generation. Candidate logic will not be silently repaired before testing. State, caches and fixture data will be isolated, and fixture execution cannot access real source tables to bypass the test. Selected passing checks do not certify full correctness.

## 3.4 Worked development example

The public development walkthrough concerns a fee quotation and its guide. A material distinction is whether a null eligibility flag denotes an unrestricted case or an ineligible case. A synthetic true-only donor procedure can be valid under its stated policy while conflicting with the target guide. This planted mismatch is a diagnostic stress case, not a naturally observed agent failure or an addition to official benchmark runs.

Checked reuse assesses the donor rule while retaining a compatible generic formula. If the solver nevertheless generates a true-only candidate, counterexample review can challenge it. For illustration, two otherwise matching rows have zero variable rate: one has a true flag and EUR 0.10 fixed amount; the other has a null flag and EUR 0.30. A true-only average returns EUR 0.10; including the unrestricted row returns EUR 0.20. Setting both flags to true gives EUR 0.20 under both interpretations, demonstrating why a non-discriminating test cannot establish correct null handling.

These numbers are researcher-only explanatory references. An evaluated reviewer must generate and validate its own complete fixture without receiving our witness or expected outcome. Offline Decimal and SQLite calculations have checked the illustration and original development calculation. This establishes arithmetic feasibility, not agent performance or intervention effectiveness.

## 3.5 Experimental conditions and controls

The two binary factors produce four conditions in the same hierarchy:

| Condition | Experience handling | Candidate review |
|---|---|---|
| Baseline | Ordinary scoped retrieval/source use | Ordinary candidate review |
| Checked reuse | Added source-based admission check | Ordinary candidate review |
| Counterexample review | Ordinary scoped retrieval/source use | Added source-first counterexample protocol |
| Both | Added source-based admission check | Added source-first counterexample protocol |

These names explicitly replace the previous proposed C1/V2 interventions for this revision. Checked long-term reuse is not the earlier task-local context record; counterexample review is not independent full recomputation. Old identifiers will not be reassigned to new mechanisms.

At minimum, architectural controls will be a strong ordinary single agent and a single agent equipped with both procedures. They receive the same model, tools, source access and frozen bank, with planning, execution and self-review. The same ordered procedures will operate in one context where feasible, without researcher answers. If comparable implementation is impossible, the limitation will be explicit and no isolated architecture claim made. Intermediate single-agent conditions are optional, not required for the main multi-agent factorial.

Aggregate caps include coordinator/child usage, tools, retries, fixtures and correction. Comparable ceilings do not imply equal consumption; actual cost and latency will be reported. Bounded matched-compute diagnostics may compare extra ordinary review or random tests against targeted procedures. The factorial estimates complete mechanism effects, including extra calls and changed delivered context. It does not identify gains solely from a cognitive process or context separation.

## 3.6 Data, preparation and evaluation tracks

DABstep is the primary comparative benchmark [1]. Original tasks, corpus, scorer and release will be pinned. Source modifications and planted bad lessons will not enter the native track. Prepared procedures come from documented development material, not held-out target solutions. Shared documentation across tasks is permitted but limits unseen-domain generalisation. Held-out scoring will not tune assets, prompts or caps.

Scoring access must be confirmed before the campaign. Aggregate-only scores cannot support invented task-level paired intervals or failure rates. A clearly labelled local track with independently audited references will support task-level mechanism analysis. Official validation status and local scores remain distinct.

A separate diagnostic track includes compatible/inapplicable experience, absent experience, applicability shifts, and common correct/incorrect review candidates. Native tasks and synthetic/document-conflict derivatives will be reported separately. Natural failure frequency cannot be inferred from planted errors. Genuinely ambiguous cases will not receive a numerical reference based on researcher-only conventions.

QueryProof's WarehouseReliabilityBench [12] and the datasets in the existing AgenticData comparison audit remain secondary targets. WRB, DABench, Spider 2.0 Lite, Real-Bank and Wiki-derived tasks require exact-release, access, compatibility and scoring checks. Unavailable releases remain limitations; substitute datasets will not be described as replication. Core comparisons take priority over breadth.

Cold-start and prepared access will be distinguished. The main reuse experiment requires a prepared bank, identical across systems. A bounded cold-start or public rule-shift diagnostic may assess an adaptation boundary after feasibility review, without adding a second mandatory factorial. One environment cannot establish universal portability.

## 3.7 Outcomes and failure evidence

Primary comparative outcomes are task correctness and incorrect answers delivered as final. Failures, timeouts and unanswered attempts remain in the assigned-task denominator. Coverage and accuracy conditional on a returned answer accompany them. Native scoring remains unchanged; local semantic references and tolerances will be audited before evaluation.

Reuse diagnostics measure applicable-item retention, contradicted-item admission, unknown decisions and downstream application. Reviewer variants receive a fixed common pool of correct and incorrect candidates, independent of their own solvers. Measure false acceptance, false rejection, omitted obligations, inconclusive outcomes, valid discriminating fixtures, correction and introduction of new errors. This prevents improved solver output being mistaken for reviewer improvement.

A bounded trace sample, including correct runs, will be coded using messages, retrieved entries, source pointers, code, tests and decisions. Omission differs from an attempted check judged incorrectly. MAST categories require observable evidence [8]; the guide will include examples, counterexamples and unknown cases. Repeatability and any independent annotation will be reported accurately. No unperformed inter-rater validation or hidden reasoning will be claimed.

## 3.8 Analysis and cost-effectiveness

All four conditions run on the same admitted tasks. Repetitions measure stochastic variation, but repeated runs and related variants are not independent samples. Paired contrasts will estimate separate/joint effects; uncertainty respects base-task clustering and related families. Where sufficient families exist, family-level sensitivity analysis will be reported. Precision and feasibility determine campaign size before held-out results are inspected.

For success proportions on the same tasks, additive interaction is:

`I = p(Both) - p(Checked reuse) - p(Counterexample review) + p(Baseline)`.

A combined win over either individual condition does not establish positive interaction. Prespecified contrasts, denominators and primary outcomes will limit selective reporting. Wide uncertainty will not be interpreted as equivalence.

Business analysis separates preparation/adaptation effort from runtime expense. Runtime includes model/tool cost, tokens, latency and failures. Preparation covers construction/checking of permitted assets. Setup hours distinguish reusable research infrastructure from environment-specific adaptation; hours are not converted into invented savings.

For declared query volume N, monetary scenario total cost comprises paid preparation, documented adaptation/maintenance charges and cumulative runtime. Human setup/adaptation hours are reported separately; they enter a combined monetary scenario only under an explicitly stated valuation assumption. Cost per correct answer divides total cost by correct answers; it is undefined if none are correct. Quality and coverage accompany the ratio. Compare cost at comparable quality and quality under comparable budgets, with amortisation sensitivity across declared volumes. Human effort remains hours unless explicitly valued in a labelled scenario. Break-even scenarios are not observed ROI. Greater accuracy can still be uneconomical, and preparation may pay off only after substantial reuse.

## 3.9 Feasibility and scope management

Before paid pilots, fake providers and deterministic calculations will test context separation, message logging, admission blocking, replay, invalid fixtures and aggregate accounting. Tools must not access evaluator references, other-task outputs or uncontrolled memory. Defaults and Docker settings alone do not prove isolation. Replay must preserve candidate logic.

One affordable tool-capable model will be selected after access/cost calibration; Qwen is a candidate consistent with the author's China-based study and budget concerns. No exact model/provider or spending ceiling is approved. Version, reasoning mode, prompts and caps will be frozen. A one-model study limits generalisation; replication is optional. Paid calls require an agreed total budget and cumulative guard.

The study uses public sources, with no employer data, human-subject study or production deployment. Risks include wrong source interpretations, weak controls, invalid fixtures, insufficient natural reuse failures, scorer restrictions, task dependence and annotation effort. Development gates can narrow the study if needed. Substantive changes will be recorded before testing; favourable held-out treatment effects will not determine task selection.

---

End of preserved snapshot.
