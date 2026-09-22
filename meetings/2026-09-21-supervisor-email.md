# Email draft — scope refinement and roadmap

Status: draft, updated 22 September 2026, not sent. Recipient: Prof. Liu Jialu. No email address has been assumed.

Subject: Proposed thesis title and scope refinement — October proposal

Dear Professor Liu,

Following our earlier discussion and a further literature review, I would like to propose a refinement of my thesis, “When Analysts Become Agents: A Verification-Aware Benchmark for Multi-Agent LLM Systems in Business Analytics.” The study would continue to focus on multi-agent systems in business analytics, with a more specific emphasis on how agents share and reconcile business knowledge.

To reflect this focus, I would like to propose the following title:

“Coordinating Distributed Business Knowledge in Multi-Agent Analytics: A Controlled Study of Shared Memory and Conflict Resolution”

The original plan compared verification and structured shared context, including their combination. This remains the core of the study and follows your observation that verification alone may be insufficient. The refinement is to evaluate these mechanisms on analytics tasks where structured data must be interpreted using business rules in documents—for example, metric definitions, applicability periods and product-specific exceptions.

This would allow us to examine a practical failure: agents may execute a calculation successfully while using the wrong business definition. The main question would be: when do independent executable verification and shared business-context alignment improve MAS reliability, separately and jointly?

The literature review suggests that the original broad novelty claim should be revised. AgenticData already combines multi-agent analytics, documentation, memory and plan validation; DataCross addresses heterogeneous data analysis; and recent memory research covers conflict handling. I therefore propose a more focused empirical contribution: a controlled comparison of verification and context alignment under consistent and conflicting business rules, with executable reference answers, failure analysis and cost measurements. I would not claim a new general-purpose memory architecture or the first MAS analytics benchmark.

The initial experiment would keep the agent team fixed and compare four conditions: baseline, executable verification, shared-context alignment, and their combination. A strong single-agent baseline and resource controls would help interpret the results. All data and code would be public; no proprietary employer data or human-subject study would be required.

My proposed roadmap is:

- Late September: agree on the refinement and audit candidate datasets and the closest literature.
- Early to mid-October: build 10–15 pilot tasks with controlled rule variants, implement the core comparisons, and assess feasibility and cost.
- Late October: incorporate your feedback and submit the project proposal by the required deadline.
- November–January: expand and freeze the task suite, run the main experiments, and analyse failures and robustness.
- February–March: complete the thesis draft, revise it with your feedback, and prepare the defence.
- Around April 2027: final submission and defence, subject to confirmation of the university schedule.

The pilot would test the design rather than assume that the combined intervention will perform best. I believe this refinement preserves the original direction while making the contribution more precise and useful for evaluating business-analytics MAS.

Would you be comfortable with this adjustment to the title and focus of the thesis? The study would retain the original verification and shared-context comparison, while examining it in a more specific business setting. I would also appreciate your feedback on the proposed roadmap.

Best regards,
Mikhail Dushkin

---
Selected references for the discussion:

- Cemri et al. (2025), Why Do Multi-Agent LLM Systems Fail? https://arxiv.org/abs/2503.13657
- Sun et al. (2025), AgenticData: An Agentic Data Analytics System for Heterogeneous Data. https://arxiv.org/abs/2508.05002
- DataCross (2026), A Unified Benchmark and Agent Framework for Cross-Modal Heterogeneous Data Analysis. https://arxiv.org/abs/2601.21403
