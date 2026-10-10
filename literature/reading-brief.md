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

The next pass should compare the closest studies on independent checking, shared
context, conflict manipulation, equal information/resources, interaction analysis and
semantic acceptance. Unknown entries remain unknown. Prioritise AgenticData and the
relevant current memory/conflict papers already flagged in references.md. Bring material
changes to the author with evidence. A source supporting our motivation may also narrow
our novelty; both uses belong in the review.
