# Reference index and metadata audit

Updated 23 September 2026. All 29 indexed works have corresponding entries in
[references.bib](references.bib). The earlier primary-arXiv audit covered titles, authors,
first arXiv year, identifiers and observed versions; it did not verify all final venues.
All 29 project citation keys were preserved during the Zotero reconciliation.

## Ownership and synchronization
Zotero's **My Library / MIB Thesis** collection (`W5I5MZBH`) is the source of truth.
[references.bib](references.bib) is its generated Better BibTeX export: **do not edit it
manually**. Configuration, ongoing edits and recovery are in [WORKFLOW.md](../WORKFLOW.md).
Zotero Desktop 10.0.4 and local API v3 were tested successfully on 23 September 2026.
Keep updated is enabled for the current checkout; the former-path export is disabled.
The export contains no attachment paths. Settings persisted after closing and reopening Zotero;
the Desktop collection still contained 29 items and the local API responded successfully.

Reconciliation: the collection initially held two works; 18 existing library items were
added to it, and nine absent works were imported from the project BibTeX. DOI/arXiv matching
identified seven reused items; 13 others lacked identifiers and were matched by title and
authors before adding the arXiv identifiers. Two pre-existing duplicate records outside the
collection were left untouched. No existing items were deleted and no collection was replaced.
The resulting collection has 29 distinct indexed arXiv IDs. Project keys are pinned in the
native Citation Key field; 18 former library keys are retained as `ids` aliases.
Titles/authors were reconciled to the audited project metadata. Existing venue/type/date
fields were retained: exported conference editions and their publication years are **not**
a fresh verification of final publication metadata. The arXiv links and reading table below
remain the scope of the prior audit. Review venue details before submission.

Live test: temporarily prefixed the `tex.note` field of item `PKZCLZLT` with
`MIB_AUTOSYNC_TEST_20260923`. The exported note changed automatically (with BibTeX-escaped
underscores), without a manual export. Restoring the original note triggered another automatic
export and recovered the exact original file hash. The marker is absent from the final file.

- Before and restored SHA-256: `a175b1a77e4467ec1d5b589837f3d226d30ffbfd8fd7391f26d1269e06c83af8`.
- Changed SHA-256: `56f32c115d3a67f7b3215dea33e05fc2643b3432c5eedab6694291d64dd610e4`.

This verifies local Zotero-to-file synchronization, not zotero.org cloud synchronization.

Metadata verification does not mean full-paper reading. Earlier selected-section reviews
are preserved below; experiments have not been reproduced. A missing reviewed version is
explicitly unknown. Before the formal proposal, pin versions supporting substantive claims
and check final publication metadata where relevant.

## Priority follow-up
AgenticData v2, LongDA v2, AMA v4, Silo-Bench v2 and MemTX v2 need comparison with the
previously inspected material before relying on current novelty/gap claims. In particular,
the previous AgenticData-v1 ablation observation is not a verified statement about v2.
Supervisor approval does not resolve this literature-validation step.

| Citation key | Primary source | Latest observed | Previous reading scope | Follow-up |
|---|---|---|---|---|
| `cemriWhyMultiAgentLLM2025` | [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) | v3 | v3 — Selected taxonomy/intervention sections reviewed previously | Prior reading scope only; not re-read today |
| `zhuMultiAgentBenchEvaluatingCollaboration2025` | [MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents](https://arxiv.org/abs/2503.01935) | v1 | not recorded — Legacy read marker; depth/version not independently confirmed | Review latest before relying on gap claim |
| `arxiv230808155` | [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) | v2 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv230800352` | [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) | v7 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv230317760` | [CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society](https://arxiv.org/abs/2303.17760) | v2 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv230707924` | [ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924) | v5 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv240201680` | [Large Language Model based Multi-Agents: A Survey of Progress and Challenges](https://arxiv.org/abs/2402.01680) | v2 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv230514325` | [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325) | v1 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv240205120` | [More Agents Is All You Need](https://arxiv.org/abs/2402.05120) | v2 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv231001798` | [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) | v2 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv230311366` | [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | v4 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv230317651` | [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | v2 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv230503111` | [Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs](https://arxiv.org/abs/2305.03111) | v3 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv241107763` | [Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows](https://arxiv.org/abs/2411.07763) | v2 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv240105507` | [InfiAgent-DABench: Evaluating Agents on Data Analysis Tasks](https://arxiv.org/abs/2401.05507) | v3 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv240809174` | [TableBench: A Comprehensive and Complex Benchmark for Table Question Answering](https://arxiv.org/abs/2408.09174) | v2 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv210900122` | [FinQA: A Dataset of Numerical Reasoning over Financial Data](https://arxiv.org/abs/2109.00122) | v3 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv210507624` | [TAT-QA: A Question Answering Benchmark on a Hybrid of Tabular and Textual Content in Finance](https://arxiv.org/abs/2105.07624) | v2 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv230605685` | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) | v4 | — — To read; metadata only | Metadata only; not newly read |
| `arxiv250805002` | [AgenticData: An Agentic Data Analytics System for Heterogeneous Data](https://arxiv.org/abs/2508.05002) | v2 | v1 — Architecture, manual-grounded validation and experiments | Review latest before relying on gap claim |
| `arxiv260121403` | [DataCross: A Unified Benchmark and Agent Framework for Cross-Modal Heterogeneous Data Analysis](https://arxiv.org/abs/2601.21403) | v1 | v1 — Construction, framework and evaluation | Prior reading scope only; not re-read today |
| `arxiv260102598` | [LongDA: Benchmarking LLM Agents for Long-Document Data Analysis](https://arxiv.org/abs/2601.02598) | v2 | not recorded — Construction and limitations; earlier review did not pin version | Review latest before relying on gap claim |
| `arxiv260120352` | [AMA: Adaptive Memory via Multi-Agent Collaboration](https://arxiv.org/abs/2601.20352) | v4 | v1 — Methods, datasets, ablations and limitations | Review latest before relying on gap claim |
| `arxiv260301045` | [Silo-Bench: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems](https://arxiv.org/abs/2603.01045) | v2 | v1 — Task scope, failures and limitations | Review latest before relying on gap claim |
| `arxiv260624535` | [Governed Shared Memory for Multi-Agent LLM Systems](https://arxiv.org/abs/2606.24535) | v1 | v1 — Architecture, measurement scope and limitations | Prior reading scope only; not re-read today |
| `arxiv260506527` | [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527) | v1 | v1 — Task definition and limitations | Prior reading scope only; not re-read today |
| `arxiv260723929` | [MemTX: Transactional Belief Commit for Stateful Agent Memory](https://arxiv.org/abs/2607.23929) | v2 | v1 — Protocol, experiments and repair limitations | Review latest before relying on gap claim |
| `arxiv250623719` | [DABstep: Data Agent Benchmark for Multi-step Reasoning](https://arxiv.org/abs/2506.23719) | v1 | v1 — Task structure and limitations | Prior reading scope only; not re-read today |
| `arxiv180908887` | [Spider: A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL Task](https://arxiv.org/abs/1809.08887) | v5 | — — To read; metadata only | Metadata only; not newly read |
