# Improving Evidence Use and Semantic Verification in Multi-Agent Business Analytics: A Failure-Guided Controlled Study

Author: Mikhail Dushkin
Student ID: 125120990077
Programme: Master of International Business
School: Antai College of Economics and Management, Shanghai Jiao Tong University
Supervisor: Professor Liu Jialu (刘佳璐)

English narrative draft for author and supervisor review; drafted 11 October and Section 1 revised 14 October 2026. The six sections follow the current university form. This is a text-first revision: the existing DOCX contains the earlier design and has not been updated. The revised direction and mechanisms are author-agreed, not newly supervisor-approved. No experimental agent results are claimed. Implementation parameters will be validated on development tasks and frozen before held-out evaluation.

# 1 Research frontier, current status, challenges and significance

## 1.1 Why business-correct analytics requires knowledge

An analytics agent is a program that uses a language model to read sources, write and execute analysis code, and revise its work. It can produce code that runs successfully and still answer the wrong business question. Consider a request for average sales per customer. Before calculating anything, the agent must establish which customers count, which reporting period applies, and how returns or cancelled orders should be treated. Different choices can produce different, plausible answers from the same tables. Business-correct analytics therefore requires both an accurate calculation and the correct use of the knowledge defining the requested measure.

My professional experience in banking analytics motivates this problem. Tables can have clear schemas and column descriptions while the rules needed to interpret them remain in separate documents. Providing those documents makes the knowledge available, but the agent must still identify the applicable rule and implement it correctly.

This distinction also makes accuracy difficult to assess. A technical check can establish that code runs; matching an expected number can establish success on a particular task; examining the governing rules can establish whether the calculation answers the intended question. These checks address different aspects of quality. Comparing systems requires shared tasks, rules and evaluation criteria, as well as an understanding of how each system reaches its answer. This leads to existing analytics benchmarks and the systems evaluated on them.

## 1.2 What leading analytics systems show

DABstep provides a common benchmark for multi-step data analysis using tables and supporting documentation [1]. It allows different systems to be evaluated on the same questions. Final-answer accuracy is an important starting point, but does not explain why an answer is wrong or which system component needs improvement.

This study focuses on DataPilot, DS-STAR and NVIDIA Data Explorer because they are among the leading validated DABstep entries and publish technical descriptions relevant to knowledge use and checking. On 14 October 2026, NVIDIA ranked first on hard-task accuracy at 89.95%, DataPilot second at 87.57%, and DS-STAR fifth at 45.24% [2]. These are rankings on the hard subset, not a claim that these are the top three systems. Their descriptions also provide complementary starting points for this research.

DataPilot emphasises reusable knowledge: it stores versioned procedures, metric definitions and executable assets, then brings relevant assets into the current task. Its main agent can delegate competing interpretations to subagents [3]. It is an important reference for studying how previously acquired knowledge informs a new calculation.

DS-STAR divides analysis into activities including understanding files, planning, coding and verification. Its reviewer assesses whether a proposed solution is sufficient and can trigger refinement [4]. It is an important reference for studying how an analytical result is checked before delivery.

NVIDIA combines substantial preparation of reusable functions and examples with a single tool-calling agent during inference and separate offline reflection [5]. Its leading result makes it a necessary counterpoint: high accuracy does not require a large team during each query. It also shows why prepared knowledge and the cost of creating it must be considered alongside runtime behaviour.

These systems motivate the study; their leaderboard scores do not isolate the effect of agent count, memory or review. Models, tools and preparation differ. DataPilot and DS-STAR will therefore guide the research design, while controlled experiments will use one reproducible adaptation with clearly stated differences from the original systems.

## 1.3 Why study a multi-agent system?

A multi-agent system (MAS) consists of agents that coordinate their work. This study uses a hierarchy: a main agent delegates tasks to subagents with separate working conversations, or contexts. Although NVIDIA leads DABstep with a single agent during inference, a hierarchy offers two relevant opportunities.

First, an evidence worker can assess a retrieved procedure before passing it to a computational agent, keeping inapplicable instructions out of the calculation context. Second, a reviewer can read the question and sources before seeing the proposed answer, then challenge the solver's interpretation. These boundaries motivate studying knowledge use and review in MAS.

Their value must be tested: collaboration can add overhead [6], and a single agent can perform comparable procedures [7]. The experiment will therefore compare the hierarchy with similarly equipped single agents, measuring whether reliability gains justify the additional cost.

## 1.4 Using MAST to identify two research problems

To investigate a multi-agent workflow, it is necessary to describe where it fails. The Multi-Agent System Failure Taxonomy, or MAST, groups failures into system design, inter-agent misalignment and task verification [8]. It provides a vocabulary for examining execution traces rather than treating every wrong final answer as the same error. This study will use it to organise diagnosis, then focus on two problems relevant to business analytics.

**Problem one: available knowledge or experience is not used appropriately.** A worker may find a relevant rule but fail to pass it on; another agent may receive it but disregard it. A remembered procedure may also be applied outside its valid business scope. For example, a previous sales calculation may exclude cancelled orders, while the current measure requires a different treatment. The research will examine the wider information-use problem but intervene specifically when retrieved experience is admitted for use. ReasoningBank provides a precedent for retrieving past experience to support new tasks [9]; our question is whether its applicability should be checked explicitly against current sources.

**Problem two: review accepts an incorrect business interpretation.** There are two important cases. The reviewer may check arithmetic while omitting a required eligibility or denominator check, corresponding to incomplete verification. Alternatively, it may examine the disputed rule and wrongly approve its use, corresponding to incorrect verification. These are different targets: performing more checks does not necessarily improve the judgement made by each check.

MAST will provide the starting classification. Where its categories do not adequately distinguish recurring analytics failures, the study will propose domain-specific refinements or additional subtypes, supported by definitions and trace examples. Their contribution will be assessed through coding consistency and usefulness in identifying targets for improvement.

## 1.5 Building on existing solutions

The two proposed changes address different stages of the workflow. First, **evidence-checked experience reuse** will assess whether a retrieved procedure's conditions are supported by current documents before passing it to the computational agent. Useful compatible procedures should remain available. The question is whether this additional check improves ordinary retrieval and source use, not whether memory is beneficial in every task.

Second, **source-grounded counterexample review** will challenge a candidate interpretation with a small executable example. For instance, if two calculations treat cancelled orders differently, test data containing such an order can expose the difference. The documents determine which interpretation is correct; disagreement between calculations alone cannot do so.

SQLDriller provides a methodological precedent for using small databases to distinguish alternative SQL interpretations [10]. TS-SQL studies executable tests for refinement [11]. QueryProof connects business rules, verification and reliability-aware analytics evaluation [12]. These works establish that memory, rule checks and executable tests are existing ideas. Our contribution must come from their carefully specified adaptation and controlled evaluation.

Additional checking also needs an economic justification. FinHelm's author reports a small development comparison in which verification added cost without improving mean accuracy [13]. This does not settle the value of checking, but makes its benefit an empirical question. Detailed protocols, implementation controls and measurements are presented in Section 3.

## 1.6 Research contribution and practical significance

This thesis will investigate source-checked experience reuse and semantic counterexample review separately and together in one hierarchical analytics system. It will connect changes in final-answer quality with evidence about inappropriate reuse, omitted checks and incorrect review decisions. Strong single-agent comparisons will test whether the hierarchy adds value beyond the procedures themselves.

The practical significance is guidance for choosing how much effort to invest in knowledge preparation, reuse and checking. Better handling of documented rules could make analytical systems more useful and reduce adaptation work, but deployment across arbitrary businesses is not an objective of this study. Accuracy, coverage, preparation effort and operating cost will be reported together. The research will not claim realised productivity savings or return on investment without workplace evidence.

## References, in order of first appearance

These version-specific references support the draft. Engineering descriptions are distinguished from papers. New records require reconciliation in Zotero; the generated bibliography has not been manually edited. Primary links and version metadata were checked on 11 October 2026, with the leaderboard and selected supporting sources rechecked on 14 October; selected-section reading scope is documented in the project literature records.

[1] Egg, Alex, Martin Iglesias Goyanes, Friso Kingma, Andreu Mora, Leandro von Werra, and Thomas Wolf. 2025. “DABstep: Data Agent Benchmark for Multi-step Reasoning.” arXiv:2506.23719v1. [Paper](https://arxiv.org/abs/2506.23719v1).

[2] Adyen and Hugging Face. “DABstep Leaderboard.” Validated submissions, hard-task accuracy ranking. Accessed October 14, 2026. [Leaderboard](https://huggingface.co/spaces/adyen/DABstep).

[3] Gao, Zion. 2026. “Beyond Fine-tuning: Solving DABstep's Hard Mode with Versioned Assets.” OceanBase technical article, January 9, updated October 10. [Article](https://en.oceanbase.com/blog/24781555459).

[4] Nam, Jaehyun, Jinsung Yoon, Jiefeng Chen, Raj Sinha, Jinwoo Shin, and Tomas Pfister. 2025, revised 2026. “DS-STAR: Data Science Agent for Solving Diverse Tasks across Heterogeneous Formats and Open-Ended Queries.” arXiv:2509.21825v4. [Paper](https://arxiv.org/html/2509.21825v4).

[5] Liu, Jiwei, Maximilian Jeblick, and Jack Yu. 2026. “Build an Agent That Thinks Like a Data Scientist: How We Hit #1 on DABStep with Reusable Tool Generation.” NVIDIA community technical article, March 13. [Article](https://huggingface.co/blog/nvidia/nemo-agent-toolkit-data-explorer-dabstep-1st-place).

[6] Kim, Yubin, Ken Gu, Chanwoo Park, Chunjong Park, Samuel Schmidgall, A. Ali Heydari, Yao Yan, Zhihan Zhang, Yuchen Zhuang, Yun Liu, Mark Malhotra, Paul Pu Liang, Hae Won Park, Yuzhe Yang, Xuhai Xu, Yilun Du, Shwetak Patel, Tim Althoff, Daniel McDuff, and Xin Liu. 2025, revised 2026. “Towards a Science of Scaling Agent Systems.” arXiv:2512.08296v3. [Paper](https://arxiv.org/html/2512.08296v3).

[7] Xu, Jiawei, Arief Koesdwiady, Sisong Bei, Yan Han, Baixiang Huang, Dakuo Wang, Yutong Chen, Zheshen Wang, Peihao Wang, Pan Li, and Ying Ding. 2026. “Rethinking the Value of Multi-Agent Workflow: A Strong Single Agent Baseline.” arXiv:2601.12307v1. [Paper](https://arxiv.org/html/2601.12307v1).

[8] Cemri, Mert, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt Keutzer, Aditya Parameswaran, Dan Klein, Kannan Ramchandran, Matei Zaharia, Joseph E. Gonzalez, and Ion Stoica. 2025. “Why Do Multi-Agent LLM Systems Fail?” arXiv:2503.13657v3. [Paper](https://arxiv.org/html/2503.13657v3).

[9] Ouyang, Siru, Jun Yan, I-Hung Hsu, Yanfei Chen, Ke Jiang, Zifeng Wang, Rujun Han, Long T. Le, Samira Daruki, Xiangru Tang, Vishy Tirumalashetty, George Lee, Mahsan Rofouei, Hangfei Lin, Jiawei Han, Chen-Yu Lee, and Tomas Pfister. 2025, revised 2026. “ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory.” arXiv:2509.25140v2. [Paper](https://arxiv.org/html/2509.25140v2).

[10] Yang, Yicun, Zhaoguo Wang, Yu Xia, Zhuoran Wei, Haoran Ding, Ruzica Piskac, Haibo Chen, and Jinyang Li. 2025. “Automated Validating and Fixing of Text-to-SQL Translation with Execution Consistency.” Proceedings of the ACM on Management of Data 3(3), Article 134, 28 pages. DOI: 10.1145/3725271. [Author-hosted paper](https://ipads.se.sjtu.edu.cn/zh/publications/SQLDriller.pdf).

[11] Xu, Wenbo, Haifeng Zhu, Liang Yan, Chuanyi Liu, Peiyi Han, Shaoming Duan, and Jeff Z. Pan. 2025. “TS-SQL: Test-driven Self-refinement for Text-to-SQL.” Findings of the Association for Computational Linguistics: EMNLP 2025, 2864–2889. DOI: 10.18653/v1/2025.findings-emnlp.156. [Proceedings record](https://aclanthology.org/2025.findings-emnlp.156/).

[12] Lee, Morris. 2026. “Business Truth, not SQL Accuracy: A Rule-Gated 7B Analytics Agent Outperforms a Direct-Prompted 32B Baseline.” arXiv:2608.09254v1. [Paper](https://arxiv.org/html/2608.09254v1).

[13] ZhouJiaJun2333. 2026. “FinHelm.” Software repository and evaluation log, revision 89e1546cab8fdfd9e996e8f6a6efeec933bc1be5. GitHub account attribution; no personal-name identity is inferred. [Repository](https://github.com/ZhouJiaJun2333/FinHelm/tree/89e1546cab8fdfd9e996e8f6a6efeec933bc1be5), [evaluation log](https://github.com/ZhouJiaJun2333/FinHelm/blob/89e1546cab8fdfd9e996e8f6a6efeec933bc1be5/docs/evaluation.md).

# 2 Research objectives, main contents and key issues to be solved

## 2.1 Research objectives

The overall objective is to improve the reliability and cost-effectiveness of hierarchical multi-agent business analytics through evidence-checked experience reuse and source-grounded counterexample review.

The specific objectives are to:

1. Classify evidence-use and verification failures using MAST, proposing analytics-specific refinements where recurring errors warrant them.
2. Establish the separate and joint effects of the two mechanisms on inappropriate reuse, review errors and final-answer quality.
3. Determine whether the improvements justify preparation and operating costs relative to the baseline MAS and strong single-agent controls.

## 2.2 Main contents

1. **Failure analysis and existing solutions.** Examine DataPilot, DS-STAR and relevant methods; diagnose baseline traces using a MAST-based coding guide.
2. **System implementation.** Adapt the FinHelm engine into a fixed hierarchy and implement the two mechanisms with controlled source and memory access.
3. **Comparative evaluation.** Run Baseline, Checked reuse, Counterexample review and Both on the same tasks, alongside strong single-agent controls. Use DABstep for native benchmark comparison and separate diagnostic cases to examine the mechanisms.
4. **Error and business analysis.** Measure reuse decisions, reviewer acceptance and rejection, final correctness, coverage, preparation effort and runtime cost; identify when the mechanisms help, fail or add unnecessary expense.

## 2.3 Key issues to be solved

- **Applicable knowledge:** determine whether a retrieved procedure is supported by current documents while retaining useful experience.
- **Meaningful verification:** construct valid test data that distinguishes business interpretations and derive expected behaviour without reference answers.
- **Credible comparison:** keep source access and prepared knowledge equivalent, measure total resource use, and assess reviewers on common candidates.
- **Useful diagnosis:** distinguish failures consistently and establish whether any proposed MAST refinement helps identify a concrete improvement target.

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

# 4 Novelties of the proposed topic

The proposed contribution is an incremental controlled study of two specific mechanisms in hierarchical business analytics. It seeks evidence on whether checking retrieved procedures against current sources and challenging interpretations with discriminating fixtures improve reliability separately and jointly. Equal experience, documents and strong controls support comparisons without supplying gold rules or attributing unequal preparation to architecture.

A second contribution sought is an analytics-specific refinement of MAST where recurring failures are insufficiently distinguished by existing categories. Proposed subtypes will have definitions and trace examples, and will be assessed for coding consistency and diagnostic usefulness. This classification will connect targeted mechanisms, failure evidence and final quality. Common-candidate tests distinguish reviewer improvement from better solver output. Native benchmark comparisons and separate diagnostics expose limits of transferring planted-error conclusions to ordinary tasks.

The practical contribution sought is guidance on preparation, reuse and checking effort at explicit quality and cost levels, including comparison with strong single agents. No universal memory protocol, formal guarantee, first analytics MAS benchmark or guaranteed improvement is claimed. Memory, semantic gates and counterexamples are existing methods [3,9,10–12]. The contribution rests on the controlled question, adaptation, measurement and useful boundaries, not relabelling components. Closest-work equivalence remains subject to targeted checks; equivalent prior evidence will require revising the contribution statement.

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
