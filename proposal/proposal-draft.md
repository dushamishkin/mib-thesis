# Improving Evidence Use and Semantic Verification in Multi-Agent Business Analytics: A Failure-Guided Controlled Study

Author: Mikhail Dushkin
Student ID: 125120990077
Programme: Master of International Business
School: Antai College of Economics and Management, Shanghai Jiao Tong University
Supervisor: Professor Liu Jialu (刘佳璐)

English narrative draft for author and supervisor review, 11 October 2026. The six sections follow the current university form. This is a text-first revision: the existing DOCX contains the earlier design and has not been updated. The revised direction and mechanisms are author-agreed, not newly supervisor-approved. No experimental agent results are claimed. Implementation parameters will be validated on development tasks and frozen before held-out evaluation.

# 1 Research frontier, current status, challenges and significance

## 1.1 Business-correct analytics requires applicable knowledge

Business analytics requires more than locating a table and executing a formula. The meaning of an analytical request can depend on definitions dispersed across schemas, manuals and other documentation. Relevant distinctions include the eligible population, reporting period, units, missing values, exceptions and aggregation grain. A calculation can execute successfully and produce a plausible number while answering a different business question. Reliability therefore requires both correct computation and a justified interpretation of the rules governing the requested quantity.

My professional experience in banking analytics motivates this distinction. Schemas and column descriptions provide structure, but do not necessarily explain which joins, filters and hierarchy relationships implement a business definition. For example, trade-finance limit utilisation requires an applicable definition of active limits and an appropriate treatment of umbrella arrangements. These examples illustrate the motivation; they are not measured workplace findings or established experimental rules. The research concerns data and business analytics generally and will use public data and documentation, without employer records or internal knowledge sources.

For a business adopting an analytical agent, reliability and deployment effort are connected. A system prepared for one organisation may depend on bespoke metric definitions, examples and helper functions. Moving it to another environment can require rebuilding or validating those assets. Conversely, a system that starts with only tables and documents may incur more reasoning and checking on every request. The practical objective is to understand this preparation-versus-runtime trade-off, not to promise universal deployment without adaptation. For a Master of International Business thesis, the relevant managerial questions concern knowledge reuse, implementation effort, reliability and cost-effectiveness.

## 1.2 Existing analytics systems provide the starting point

DABstep provides a public basis for studying multi-step analysis that combines structured data with documentary context [1]. Its native scoring supports final-answer comparison, but cannot by itself explain whether a failure originated in source interpretation, experience reuse or review. This study will retain original benchmark evaluation while adding separately reported mechanism diagnostics. A new benchmark search is unnecessary: the project already has an audited source-selection record and a permanently development-only example.

DataPilot is a primary conceptual reference [2]. Its technical description separates reusable assets from runtime execution, including versioned procedures, semantic definitions and executable components. A main agent can delegate competing hypotheses, and evaluation feedback supports asset promotion. This provides a precedent for reusing business knowledge rather than reasoning from scratch for every question. However, the public account does not completely specify a current-source applicability check for every retrieved procedure or the labelled split used for every update. Missing information is not evidence that such checking is absent. The thesis will study a testable reuse mechanism in its own adaptation, without claiming to repair a demonstrated defect in the original product.

DS-STAR is the second conceptual reference [3]. It combines file analysis, planning, code generation, verification and refinement. Its component ablations support the importance of analysis and verification in the evaluated system. Nevertheless, overall ablations do not measure whether a reviewer wrongly accepts a particular business interpretation. The inspected review template assesses a candidate using the question, plan, code and output; it does not explicitly require a document-grounded counterexample stage. This observation motivates a comparative review protocol, not a claim that DS-STAR checks only syntax or that all its configurations lack semantic reasoning. Original-system reproduction is distinct from a transparent adaptation.

Recent engineering results also challenge an automatic argument for large agent teams. NVIDIA describes a tool-calling runtime supported by separately prepared reusable functions and examples, with additional offline reflection [4]. This demonstrates why preparation must be part of the comparison. A prepared runtime and an agent encountering the corpus for the first time differ in more than agent count. Published leaderboard scores are contextual evidence, not controlled estimates of a multi-agent advantage. Beating the global leaderboard is not the scientific objective of this thesis.

## 1.3 Why retain a multi-agent system?

The central object will be a compact hierarchical multi-agent system: a main agent coordinates child agents with separate contexts and delegated reasoning and action. Children return observable findings and results to the coordinator. Calling a deterministic calculation tool alone does not create another agent. The architecture gives evidence handling, computation and review identifiable interfaces, making failures at those interfaces observable and permitting controlled changes. It does not establish that separate contexts are necessary or more accurate.

Research on scaling agent systems finds collaboration benefits and overhead to be task-dependent [5]. The value of coordination cannot be assumed to grow with agent count. A strong-single-agent study further shows that one agent can simulate tested homogeneous workflows and obtain comparable performance with efficiency advantages [6]. These findings require a demanding control: the single agent must receive equivalent sources, reusable assets, tools and opportunities for self-review. Where the same mechanisms can operate in one context, their value must also be compared across architectures. Improvement over an unimproved single agent would not isolate the value of delegation.

The justification for hierarchy is therefore conditional. Context separation may help manage competing evidence and expose assumptions to a distinct review procedure; it can also lose information, duplicate work and preserve correlated errors. The experiment will determine whether targeted improvements justify these costs. If a strong single agent performs equally well or better, that result will constrain the practical value of the hierarchy within the tested setting. Such a conclusion requires valid controls and adequate precision and would not establish that multi-agent systems are generally unnecessary.

## 1.4 Two distinct problems and their diagnostic basis

The first problem is inadequate use of available evidence and accumulated experience. The broader diagnostic map includes source access, retrieval, interpretation, transfer between agents and application in code. The selected intervention focuses on a narrower boundary: a retrieved procedure may be useful in its original setting but inappropriate under current documented rules. Similar questions do not necessarily share compatible populations, definitions or exceptions. A frozen bank makes this boundary assessable without introducing continuous test-time learning.

ReasoningBank provides an established precedent for retrieving distilled experience to inform later tasks [7]. Its web and software settings and changing memory differ from the proposed document-defined analytics study. This work will keep memory fixed during evaluation and test source-checked admission beyond ordinary metadata filters. It will not claim to invent experience reuse or a universal memory protocol. Useful procedures can also be excluded incorrectly, so retention matters alongside protection against inappropriate reuse.

The second problem is erroneous semantic verification. A reviewer may omit a material check, or attempt that check and reach the wrong judgement. Successful execution, plausible output and agreement between agents are insufficient evidence that the governing business definition was implemented. Review quality must therefore be measured on the same correct and incorrect candidates, independently of improvements in the solver producing them.

MAST supplies a descriptive taxonomy for multi-agent failures [8]. The study will use its insufficient-verification and incorrect-verification categories where visible traces support them. Information-transfer categories require evidence of an actual inter-agent handoff or disregard of received findings. Negative transfer from memory does not automatically map to a MAST label. An analytics-specific coding guide will record failure location and semantic dimension alongside applicable categories, retaining unknown and nonapplicable cases. Labels alone will not establish causal effects.

## 1.5 Verification precedents and contribution boundaries

Counterexample-based checking is established prior work. SQLDriller distinguishes alternative SQL interpretations using small databases and execution consistency [9]. It is the principal methodological precedent for the proposed review. Its dataset-validation setting and fallible interpretation differ from a runtime reviewer grounded in business documents. The adaptation will challenge generated analytical code using source-supported alternatives, without evaluator reference queries or answers. It will not provide a formal correctness guarantee for arbitrary Python programs.

TS-SQL demonstrates that generated executable tests are an existing refinement method [10]. Test generation itself is therefore insufficient novelty. Expected behaviours can be wrong, and reference-dependent preparation must remain separate from admissible runtime checking. Our reviewer must derive expectations from the question and permitted sources; invalid or non-discriminating tests will be recorded as inconclusive rather than successful verification.

QueryProof studies rule-gated analytics and reliability-aware evaluation [11]. It already connects semantic rules, deterministic checks, coverage and cost per correct answer. Its disclosed scaffolding and comparison limits underline the importance of equal information and a strong control. This study differs by manipulating two agent-side mechanisms separately and jointly within one hierarchy, rather than supplying a researcher-populated semantic layer. That distinction motivates an incremental empirical contribution, but does not prove global scientific priority.

Accessible implementations also provide negative evidence. FinHelm has delegation and optional verification infrastructure; its author reports a small development comparison where verification did not improve mean accuracy and increased resource use [12]. This is not independent replication or proof of general ineffectiveness. It nevertheless reinforces the need to test a specific checking procedure instead of treating an additional reviewer as an improvement by definition.

## 1.6 Research gap and significance

The bounded question is whether source-checked reuse and source-grounded counterexample review reduce their targeted failures, separately and jointly, at acceptable cost in one hierarchical analytics system. The literature establishes the components and supplies contrasting evaluation precedents. The thesis seeks controlled evidence about their adaptation, interaction and limits; it does not claim their invention or that no identical combination exists elsewhere.

The practical significance is guidance on when reusable knowledge should be admitted, when a business interpretation warrants an executable challenge, and whether these procedures justify their preparation and runtime expense. Final accuracy, review errors, coverage and full costs must be assessed together. Public experiments can inform engineering choices, but cannot establish realised staff savings, commercial value or enterprise-wide return on investment without additional evidence.

## References, in order of first appearance

These version-specific references support the draft. Engineering descriptions are distinguished from papers. New records require reconciliation in Zotero; the generated bibliography has not been manually edited. Primary links and version metadata were checked on 11 October 2026; selected-section reading scope is documented in the project literature records.

[1] Egg, Alex, Martin Iglesias Goyanes, Friso Kingma, Andreu Mora, Leandro von Werra, and Thomas Wolf. 2025. “DABstep: Data Agent Benchmark for Multi-step Reasoning.” arXiv:2506.23719v1. [Paper](https://arxiv.org/abs/2506.23719v1).

[2] Gao, Zion. 2026. “Beyond Fine-tuning: Solving DABstep's Hard Mode with Versioned Assets.” OceanBase technical article, January 9, updated October 10. [Article](https://en.oceanbase.com/blog/24781555459).

[3] Nam, Jaehyun, Jinsung Yoon, Jiefeng Chen, Raj Sinha, Jinwoo Shin, and Tomas Pfister. 2025, revised 2026. “DS-STAR: Data Science Agent for Solving Diverse Tasks across Heterogeneous Formats and Open-Ended Queries.” arXiv:2509.21825v4. [Paper](https://arxiv.org/html/2509.21825v4).

[4] Liu, Jiwei, Maximilian Jeblick, and Jack Yu. 2026. “Build an Agent That Thinks Like a Data Scientist: How We Hit #1 on DABStep with Reusable Tool Generation.” NVIDIA community technical article, March 13. [Article](https://huggingface.co/blog/nvidia/nemo-agent-toolkit-data-explorer-dabstep-1st-place).

[5] Kim, Yubin, Ken Gu, Chanwoo Park, Chunjong Park, Samuel Schmidgall, A. Ali Heydari, Yao Yan, Zhihan Zhang, Yuchen Zhuang, Yun Liu, Mark Malhotra, Paul Pu Liang, Hae Won Park, Yuzhe Yang, Xuhai Xu, Yilun Du, Shwetak Patel, Tim Althoff, Daniel McDuff, and Xin Liu. 2025, revised 2026. “Towards a Science of Scaling Agent Systems.” arXiv:2512.08296v3. [Paper](https://arxiv.org/html/2512.08296v3).

[6] Xu, Jiawei, Arief Koesdwiady, Sisong Bei, Yan Han, Baixiang Huang, Dakuo Wang, Yutong Chen, Zheshen Wang, Peihao Wang, Pan Li, and Ying Ding. 2026. “Rethinking the Value of Multi-Agent Workflow: A Strong Single Agent Baseline.” arXiv:2601.12307v1. [Paper](https://arxiv.org/html/2601.12307v1).

[7] Ouyang, Siru, Jun Yan, I-Hung Hsu, Yanfei Chen, Ke Jiang, Zifeng Wang, Rujun Han, Long T. Le, Samira Daruki, Xiangru Tang, Vishy Tirumalashetty, George Lee, Mahsan Rofouei, Hangfei Lin, Jiawei Han, Chen-Yu Lee, and Tomas Pfister. 2025, revised 2026. “ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory.” arXiv:2509.25140v2. [Paper](https://arxiv.org/html/2509.25140v2).

[8] Cemri, Mert, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt Keutzer, Aditya Parameswaran, Dan Klein, Kannan Ramchandran, Matei Zaharia, Joseph E. Gonzalez, and Ion Stoica. 2025. “Why Do Multi-Agent LLM Systems Fail?” arXiv:2503.13657v3. [Paper](https://arxiv.org/html/2503.13657v3).

[9] Yang, Yicun, Zhaoguo Wang, Yu Xia, Zhuoran Wei, Haoran Ding, Ruzica Piskac, Haibo Chen, and Jinyang Li. 2025. “Automated Validating and Fixing of Text-to-SQL Translation with Execution Consistency.” Proceedings of the ACM on Management of Data 3(3), Article 134, 28 pages. DOI: 10.1145/3725271. [Author-hosted paper](https://ipads.se.sjtu.edu.cn/zh/publications/SQLDriller.pdf).

[10] Xu, Wenbo, Haifeng Zhu, Liang Yan, Chuanyi Liu, Peiyi Han, Shaoming Duan, and Jeff Z. Pan. 2025. “TS-SQL: Test-driven Self-refinement for Text-to-SQL.” Findings of the Association for Computational Linguistics: EMNLP 2025, 2864–2889. DOI: 10.18653/v1/2025.findings-emnlp.156. [Proceedings record](https://aclanthology.org/2025.findings-emnlp.156/).

[11] Lee, Morris. 2026. “Business Truth, not SQL Accuracy: A Rule-Gated 7B Analytics Agent Outperforms a Direct-Prompted 32B Baseline.” arXiv:2608.09254v1. [Paper](https://arxiv.org/html/2608.09254v1).

[12] ZhouJiaJun2333. 2026. “FinHelm.” Software repository and evaluation log, revision 89e1546cab8fdfd9e996e8f6a6efeec933bc1be5. GitHub account attribution; no personal-name identity is inferred. [Repository](https://github.com/ZhouJiaJun2333/FinHelm/tree/89e1546cab8fdfd9e996e8f6a6efeec933bc1be5), [evaluation log](https://github.com/ZhouJiaJun2333/FinHelm/blob/89e1546cab8fdfd9e996e8f6a6efeec933bc1be5/docs/evaluation.md).

# 2 Research objectives, contents and key issues

## 2.1 Objective and research questions

The objective is to evaluate whether evidence-checked experience reuse and source-grounded counterexample review improve the reliability and cost-effectiveness of a hierarchical multi-agent analytics system. The study will diagnose both failure groups, implement the selected mechanisms, and estimate separate and joint effects against ordinary review and strong single-agent alternatives.

**RQ1:** Which observable evidence-use and verification failures occur in the research baseline, and how do the selected literature mechanisms address or leave them open?

**RQ2:** Does checking retrieved procedures against current sources reduce inappropriate reuse without excluding useful experience, and how does this affect final quality and resource use?

**RQ3:** Does source-grounded counterexample review reduce omitted semantic checks and false acceptance of incorrect interpretations, without unacceptable false rejection, inconclusive checks or cost?

**RQ4:** What are the separate and joint effects on quality and cost-effectiveness, and do they justify the hierarchy relative to similarly equipped single-agent controls? What boundaries appear under compatible knowledge, rule shifts and limited preparation?

## 2.2 Working hypotheses and research contents

H1 predicts that checked reuse will reduce admission and downstream application of inapplicable experience while retaining useful applicable procedures. Practical value requires better final quality or a favourable quality/cost trade-off, rather than a high rejection rate alone.

H2 predicts that counterexample review will reduce false acceptance on common incorrect candidates. Acceptable false-rejection and coverage trade-offs will be specified before held-out evaluation. Rejecting nearly every candidate will not support a useful improvement.

H3 predicts that the combined system will reduce incorrect final answers relative to either individual mechanism. Positive interaction and lower cost are not assumed. The combined result may be complementary, redundant or harmful; compatible experience and already-correct candidates may make extra checks unnecessary.

Research contents comprise an evidence-linked literature comparison, a failure-coding guide, a reproducible implementation, a four-condition mechanism experiment, common-candidate review diagnostics and a business-oriented cost analysis. The initial study will use one fixed hierarchy and one affordable tool-capable model. It will not train a new model, search many topologies or build an enterprise knowledge platform. Campaign size and optional robustness checks depend on measurement validity and an agreed budget.

## 2.3 Key issues

The main challenges are establishing applicability without hidden rules, generating valid discriminating fixtures, preserving strong controls, and distinguishing actual reviewer improvement from easier solver outputs. Preparation benefits must be separated from architectural effects, and statistical analysis must respect task dependence. These issues will be addressed before scaling, rather than resolved by assuming that memory or a reviewer is trustworthy.

# 3 Research methods, scheme and feasibility

## 3.1 Fixed hierarchy and implementation

The baseline will use a main coordinator and three child roles: evidence/experience worker, computational analyst and reviewer. Each child will have a separate context and tool-using loop. Explicit routing will invoke the same roles in every multi-agent condition and record messages, tools, calculations and resource use. Exact prompts, limits and correction routes will be development-validated and frozen before testing. Routing will not depend on favourable held-out results.

The selected implementation path is adaptation of the pinned FinHelm delegation engine [12]. DataPilot and DS-STAR remain conceptual anchors, not systems whose scores this adaptation reproduces. Unrestricted memory, optional delegation and default verification behaviour will be replaced by research-specific access and routing. If the engine fails offline checks, a documented fallback will be assessed before the pilot; changing implementation requires a recorded protocol revision.

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

QueryProof's WarehouseReliabilityBench [11] and the datasets in the existing AgenticData comparison audit remain secondary targets. WRB, DABench, Spider 2.0 Lite, Real-Bank and Wiki-derived tasks require exact-release, access, compatibility and scoring checks. Unavailable releases remain limitations; substitute datasets will not be described as replication. Core comparisons take priority over breadth.

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

# 4 Novelties of the proposed topic

The proposed contribution is an incremental controlled study of two specific mechanisms in hierarchical business analytics. It seeks evidence on whether checking retrieved procedures against current sources and challenging interpretations with discriminating fixtures improve reliability separately and jointly. Equal experience, documents and strong controls support comparisons without supplying gold rules or attributing unequal preparation to architecture.

A second contribution sought is an auditable connection between targeted mechanisms, MAST-informed failure evidence and final quality. Common-candidate tests distinguish reviewer improvement from better solver output. Native benchmark comparisons and separate diagnostics expose limits of transferring planted-error conclusions to ordinary tasks.

The practical contribution sought is guidance on preparation, reuse and checking effort at explicit quality and cost levels, including comparison with strong single agents. No universal memory protocol, formal guarantee, first analytics MAS benchmark or guaranteed improvement is claimed. Memory, semantic gates and counterexamples are existing methods [2,7,9–11]. The contribution rests on the controlled question, adaptation, measurement and useful boundaries, not relabelling components. Closest-work equivalence remains subject to targeted checks; equivalent prior evidence will require revising the contribution statement.

# 5 Research schedule and expected outcomes

The immediate objective is a supervisor-reviewed proposal for submission by 15 October 2026 and defense on 22 October. Next come author review of this narrative, revision, and only then insertion into the supplied template and visual inspection. Supervisor approval is required before submission; the institutional review cutoff before 20 October does not waive it. No response time or approval of this revision is assumed.

| Period | Planned work | Expected output |
|---|---|---|
| 11–15 October 2026 | Review narrative, incorporate supervisor feedback, populate/check template and obtain approval before submission | Reviewed proposal and confirmed submission |
| 16–22 October | Prepare defense explanation/slides; proposal defense | Defense feedback and agreed revisions |
| Late October | Implement minimal hierarchy and offline access/replay/accounting checks; agree model and budget | Feasibility evidence and pilot-ready development package |
| November | Diagnose traces, validate memory/fixtures, audit references, freeze controls and analysis | Frozen procedures and evaluation plan |
| December | Run feasible experiments; midterm upload by 20 December | Run evidence and honest progress report |
| January 2027 | Analyse quality, uncertainty, costs and failures; bounded justified follow-ups | Findings and boundary analysis |
| February–March | Write/revise thesis and reproducibility materials | Supervisor-reviewed thesis draft |
| 7–14 April | Final thesis/plagiarism-check submission after approval | Final submission and receipt |
| Mid-to-late May | Final defense on institutionally confirmed date | Defense and revisions |

Expected outputs are a documented baseline, frozen source/experience manifests, prompts/routes, audited references, evaluation scripts, trace/cost evidence and a thesis reporting benefits, harms and limits. Positive findings are not promised. Null effects are useful only with valid measurement and informative uncertainty; underpowered findings remain inconclusive. Optional datasets, models and comparators will be deferred before weakening the core design.

# 6 Prior experience and accomplished achievements

My banking analytics experience motivates distinguishing data access from business-correct interpretation. It supplies no experimental data or measured productivity gains. The supervisor approved the earlier title, scope and roadmap according to my report of the discussion on 23 September 2026; this revision requires review and is not automatically covered by that approval.

Preparatory work includes a public-source benchmark audit, focused literature cards, a two-problem map and a technical comparison of DataPilot and DS-STAR. The author has agreed the mechanisms and hierarchy. Selected FinHelm interfaces and an OpenDsStar fallback were inspected without installation or agent execution. Reading limits and outstanding bibliography reconciliation are recorded separately.

The source audit pinned/checksummed files and reproduced selected calculations using separate implementations. The development fee example and discriminating/non-discriminating fixtures were checked with Decimal and SQLite. This supports source and arithmetic feasibility, not natural failure prevalence, generated-test validity or treatment effectiveness. The permanently development-only example will not count as held-out evidence.

There is no completed experimental harness, pilot agent result or frozen main-study suite. The next research work is implementation, access/measurement validation, budget agreement and protocol freeze. This proposal describes planned experiments and expected artefacts without inventing results or achievements.
