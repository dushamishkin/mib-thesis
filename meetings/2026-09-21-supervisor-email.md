# Email draft — revised topic, title and roadmap

Status: revised 22 September 2026; draft, not sent. Recipient: Prof. Liu Jialu.

Subject: Proposed thesis topic refinement and roadmap

Dear Professor Liu,

After reviewing the literature further, I would like to ask whether you would be comfortable with a revised title and a more focused research direction for my thesis:

“Coordinating Distributed Business Knowledge in Multi-Agent Analytics: A Controlled Study of Shared Memory and Conflict Resolution.”

The proposed topic is how a team of LLM agents combines business knowledge distributed across structured data and unstructured documents, and how it handles conflicting interpretations when producing an analytical result.

For example, a sales database may contain transactions, a company wiki may define revenue, and a separate policy document may specify exceptions for particular products or reporting periods. A presentation may still contain an older definition. One agent could analyse the transactions, another interpret the documentation, and a third review the result. Each agent may understand its own source, yet the team can still produce an incorrect answer if an exception is lost during communication or incompatible definitions are used in different steps.

The central research question would therefore be: under what conditions do shared memory and explicit reconciliation of business rules help a multi-agent team produce correct, consistently grounded analytical results?

This refines the original emphasis on verification. The initial proposal asked whether checking outputs could improve MAS reliability. The revised focus also examines whether agents establish and maintain a common understanding of what should be calculated. Executable verification remains an important experimental component: it allows us to test whether checking calculations is sufficient, or whether it needs to be combined with better coordination of business context. This develops the shared-context intervention already included in our earlier plan and follows your observation that verification alone may be insufficient.

Recent work makes this refinement necessary. AgenticData already combines multi-agent analytics with documentation, memory and plan validation, while DataCross studies analysis across heterogeneous sources. Research on MAS memory also addresses conflicting and outdated information. I therefore propose an empirical contribution: a controlled evaluation of when these mechanisms help in document-grounded business analytics, rather than claiming the first analytics MAS benchmark or a new general-purpose memory architecture.

The initial study would use a fixed agent team and public tables accompanied by documents defining metrics, validity periods and exceptions. Matched tasks would contain either consistent rules or conflicts that can be resolved from the available evidence. I would compare a baseline MAS, independent executable verification, structured shared context with explicit rule reconciliation, and their combination. A diagnostic subset would compare shared versus distributed access to the same source information. Strong single-agent and resource controls would help distinguish coordination effects from additional computation.

The intended practical output is a reproducible evaluation suite and guidance on when an analytics MAS needs stronger checking, better context coordination, or both. Evaluation would cover answer correctness, application of business rules, failure patterns and cost. No proprietary employer data would be required.

My proposed roadmap is:

- Late September: agree on the revised scope and title, and select candidate public data.
- Early to mid-October: construct 10–15 pilot tasks and test the core experimental conditions.
- Late October: incorporate your feedback and submit the project proposal.
- November–January: expand the evaluation suite, run the main experiments and analyse the results.
- February–March: complete and revise the thesis and prepare for the defence.
- Around April 2027: final submission and defence, subject to confirmation of the university schedule.

Would this adjustment to the topic and title be acceptable to you? I would appreciate your feedback on both the research focus and the proposed roadmap before finalising the October proposal.

Best regards,
Mikhail Dushkin

---
Selected references:

- AgenticData: https://arxiv.org/abs/2508.05002
- DataCross: https://arxiv.org/abs/2601.21403
- MAST: https://arxiv.org/abs/2503.13657
