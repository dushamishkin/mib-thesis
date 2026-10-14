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

# 3 Research methodology

## 3.1 Controlled experimental design

The study will use a **controlled experiment with a 2 × 2 factorial design**, supported by analysis of recorded agent actions and messages. Two mechanisms will be switched on or off: checking retrieved experience against current sources, and reviewing calculations through semantic counterexamples. The four combinations will show what each mechanism changes separately and what happens when they are used together.

Each version will solve the same tasks using the same underlying model, documents, prepared knowledge and agent roles. Resource limits will be comparable, and actual consumption will be measured. This design tests changes to the analytical workflow rather than comparing unrelated systems with different preparation. Development tasks will be used to test the implementation and set limits; evaluation tasks will be kept separate and will not be used to tune the system.

## 3.2 System and proposed changes

A main agent will coordinate three subagents: an evidence worker, a computational analyst and a reviewer. The evidence worker examines documents and reusable procedures; the analyst performs the calculation; the reviewer assesses the proposed solution. The ordinary system can already consult sources, execute code and correct mistakes.

The study adds two procedures:

- **Evidence-checked experience reuse.** Before a retrieved procedure reaches the analyst, the evidence worker checks whether its conditions match the current documents. Supported procedures are passed on; contradicted or unresolved procedures are withheld, while ordinary document-based analysis remains available. For example, a procedure for handling cancelled orders should be reused only when the current reporting rules support that treatment.
- **Source-grounded counterexample review.** The reviewer first reads the question and documents without the proposed answer. After inspecting the solution, it constructs a small test case that distinguishes a disputed interpretation from a source-supported alternative. If two calculations treat cancelled orders differently, a test containing such an order can expose the difference. The documents determine the correct treatment. An invalid or inconclusive test is not counted as a successful check.

Reusable knowledge will be prepared from permitted development material and held fixed during evaluation. Correct answers and researcher-written test solutions will remain outside the agents' access. The reviewer will generate its own tests rather than receive the explanatory examples used in this proposal.

## 3.3 Comparisons

The experiment will compare four versions of the same MAS:

| Version | Checked experience reuse | Counterexample review |
|---|---|---|
| Baseline | Off | Off |
| Checked reuse | On | Off |
| Counterexample review | Off | On |
| Both | On | On |

“Off” retains ordinary source use and review; the baseline is not prevented from rejecting an unsuitable procedure or detecting a mistake. All four versions use the same starting knowledge and retrieval rules.

Strong single-agent controls will perform ordinary analysis and analysis with both added procedures. They will receive equivalent information, tools and resource allowances. This will show whether an improved hierarchy offers a practical advantage over a similarly equipped single agent. Additional ordinary checking under matched budgets will be examined on a bounded sample where feasible.

## 3.4 Tasks and diagnostic cases

DABstep will provide the primary benchmark comparison using its original tasks and scoring [1]. Separately reported diagnostic cases will examine suitable and unsuitable prior knowledge, changed rule applicability, and correct and incorrect candidate calculations. Deliberately introduced errors will test specific mechanisms; they will not be counted as evidence of how frequently those errors occur naturally.

To evaluate review itself, every reviewer version will assess the same fixed set of candidate solutions. This avoids attributing easier solver outputs to a better reviewer. Local references will be audited before testing; numerical disagreement alone will not establish which business interpretation is correct.

WarehouseReliabilityBench [12] and the datasets identified in the existing AgenticData comparison audit remain secondary targets, subject to release access and task suitability. Original benchmark results and modified diagnostic cases will stay separate. Task-level comparisons require task-level reference evidence; aggregate-only benchmark scores will be reported as such.

## 3.5 Quality, failure analysis and business value

Evaluation will cover three areas:

1. **Final-answer quality.** Measure final-answer correctness, incorrect answers delivered, the share of tasks answered, and failures or timeouts.
2. **Targeted failures.** Measure admission of unsuitable experience, retention of useful procedures, omitted checks, incorrect approvals and rejection of correct solutions. Examine recorded actions and messages using MAST [8], proposing analytics-specific refinements where recurring failures warrant them.
3. **Cost-effectiveness.** Record model/tool expenditure, tokens, completion time, preparation and adaptation effort, including unsuccessful attempts and corrections.

Results will be compared task by task, with repeated runs to assess variability. Related task variants will be analysed together rather than treated as independent observations. Effect estimates will include uncertainty. The analysis will assess whether using both mechanisms adds value beyond their individual effects, without assuming that the combination is better.

The business analysis will compare quality at similar budgets and cost at similar quality levels. It will report cost per correct answer and preparation-cost scenarios for different query volumes, with human effort recorded separately in hours. These scenarios will inform adoption decisions without claiming measured workplace savings or return on investment.

## 3.6 Implementation and feasibility

The implementation will adapt the FinHelm delegation engine [13], drawing on DataPilot and DS-STAR as conceptual references. It will not be presented as reproduction of their leaderboard systems. Before paid experiments, offline checks will verify that agents remain separated, cannot read evaluation answers, and produce usable execution and cost records. Benchmark scoring access will also be confirmed.

A development pilot will establish workable task numbers, repetition counts, checking limits and an affordable model within an agreed budget. These settings will be fixed before evaluation. The initial study will use one hierarchy and one model, reducing optional dataset breadth before weakening the core comparisons. No agent experiments have yet been completed.

# 4 Novelties of the proposed topic

The study aims to make three contributions:

1. **Evidence on two proposed improvements.** Test whether checking retrieved procedures against current documents and testing disputed business interpretations on small datasets reduce errors, separately and together. Compare the results with ordinary review and strong single-agent controls.
2. **A more useful classification of analytics failures.** Apply MAST to knowledge-use and review errors. Where its categories need more detail, propose subtypes with clear definitions and examples, and test whether they help classify errors consistently.
3. **Practical guidance on quality and cost.** Identify when the added procedures improve answers enough to justify their preparation and operating costs, and when simpler approaches are preferable.

The contribution is the evidence about these methods' benefits, costs and limits in business analytics. Memory reuse, rule checks and executable tests already exist [3,9,10–12]; the study does not claim to invent them.

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
