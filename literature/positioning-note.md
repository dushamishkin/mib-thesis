# Literature positioning — 23 September 2026

Supervisor-approved direction and title (author report, 23 September 2026). Targeted review, not an exhaustive systematic review. No experimental findings yet.

## Freshness caveat — updated 10 October

The [benchmark audit](../benchmark/README.md) updates selected comparisons using AgenticData
v2 and LongDA v2 and adds newer benchmark precedents. In particular, LiveSQLBench already
includes business-rule drift; that cannot be claimed as a general gap. Selected current
AMA v4, Silo-Bench v2 and MemTX v2 passages were inspected on 10 October; complete
version/implementation comparisons remain open. See [reference audit](references.md)
for reading depth.

## Position

Study the separate and joint effects of independent executable verification (V2) and shared business-context alignment (C1) in a fixed analytics MAS under consistent and conflicting document-defined rules. This refines the original intervention ladder and keeps the original MAS/business-analytics domain. The contribution sought is controlled empirical evidence and a reusable paired evaluation suite, rather than a new universal memory system.

## Closest work and the boundary of our claim

| Work | Existing contribution | Implication for our study |
|---|---|---|
| MAST, Cemri et al. (2025) | Failure taxonomy and interventions; distinguishes misalignment and verification | Reuse for descriptive diagnosis; intervention contrasts carry causal evidence |
| AgenticData, Sun et al. (2025; v2 inspected) | MAS analytics, memory and semantic validation; component ablations across five datasets | Closest competitor; combination and ablations are prior art. Inspected sections do not establish our fixed-table rule-conflict factorial; this is not an exhaustive absence claim |
| DataCross (2026) | Heterogeneous cross-modal analytical benchmark and agent framework | Adding documents/modalities is not sufficient novelty |
| LongDA (2026) | Documentation-intensive data analysis | Authors explicitly note fixed-year snapshots, untested documentation drift and final-number-focused evaluation |
| AMA, Huang et al. (2026) | Multi-agent memory construction, retrieval, judging and refreshing | Conflict-aware shared memory is prior art; evaluated mainly on conversational-memory tasks |
| Silo-Bench, Zhang et al. (2026) | Distributed algorithmic computation; communication/integration gap | Do not claim first discovery of information transfer without correct use |
| Governed Shared Memory, Margalit et al. (2026) | Provenance, supersession and propagation in shared memory | These primitives are prior art; authors explicitly report own-service evaluation without a comparator |
| STALE, Chao et al. (2026) | Implicit stale knowledge and behavioral adaptation | Memory/action mismatch is not new; authors note single conflict pairs and generated dialogue setting |
| MemTX, Li et al. (2026) | Transactional belief admission and cascading repair | General dependency repair is prior art; guarantees depend on recorded provenance and exclude environment-level replay |

Links and reading scope are in references.md. Several sources are preprints. Absence of the exact experiment in this inspected set is not proof of global priority. Differences in benchmark scores across papers do not establish architectural superiority.

## Candidate contribution

### Design comparison and novelty risk checked 10 October

Author explicitly flags the risk of a scientifically empty recombination. The current
assessment is **an incremental empirical contribution is plausible, but novelty is
not established**. Using analytics data, adding verification to memory, measuring cost,
or introducing document conflict cannot individually carry a novelty claim.

AgenticData v2 Sections 5–7.5 already address validation, feedback memory, component
ablations, complex rule interpretation and costs. AMA v4 Sections 3.3–4 address
conflict detection/refresh in memory and conversational-memory evaluation. MemTX v2
Sections 3.5 and 4–5 address provenance repair, deterministic grading, matched runners,
controls and downstream harm. Silo-Bench v2 Sections 3 and 5 address distributed
computation and failures despite communication. LongDA and LiveSQLBench already make
documentary analytics and rule changes established evaluation topics. Source summaries
and selected reading limits: [reading brief](reading-brief.md).

| Identification question | Closest inspected precedent | Proposed study's target and remaining evidence gap |
|---|---|---|
| Do validation and memory help? | AgenticData component ablations | This broad question is already studied; our protocol must distinguish independent recomputation from plan validation and task-local rule reconciliation from feedback memory |
| Do conflicts and stale knowledge matter? | AMA conflict filtering; MemTX repair | Conflict handling is prior art; our analytical rule-applicability setting needs controlled evidence, not a priority claim |
| Do agents correctly use information they receive? | Silo-Bench communication/reasoning analysis | Existing coordination failures motivate the study but are not our discovery; test the specified analytics interventions |
| Does documentary inconsistency change which checking mechanism is useful? | Document-dependent analytics plus memory/validation precedents | Estimate prespecified effects and moderation on unchanged tables; the exact comparison is not established by the passages inspected so far |
| Is combined checking complementary rather than simply extra work? | Prior combinations, ablations and cost evaluation | Test an explicit interaction with resource controls and uncertainty; a combined win or cost report alone adds little |
| Is a team worth using instead of a single agent? | Existing MAS comparisons and coordination limits | Use a strong executable single-agent control under comparable caps; report a team loss honestly |

The useful knowledge sought is a boundary condition: whether computational checking
still releases wrong answers when the governing rule is misidentified; whether explicit
rule reconciliation reduces that risk or spreads a shared mistake; whether the joint
effect exceeds its component effects at an acceptable measured cost. These are proposed
questions, not discovered mechanisms. Observable traces alone cannot establish mediation.

Write the proposal as a controlled study seeking this evidence, without a first-of-kind
claim. If a close paper already answers the same question with equivalent controls,
present it to the author and consider a transparent replication/extension or a narrower
boundary condition. Do not silently redesign the approved topic. A different dataset
or exact combination of labels is not sufficient. The bounded search and selected
sections cannot establish global absence; code/protocol comparison remains incomplete.

Estimate when computational checking and semantic alignment help individually and jointly, with matched task variants and resource controls. Distinguish failed retrieval, incorrect rule applicability, lost inter-agent information and computational errors through observable traces and diagnostic conditions. A context intervention that spreads a shared mistake or a combined intervention that is not cost-effective are legitimate possible findings.

A merely different application domain is insufficient. The experiment must establish effects or boundary conditions that are not explained by additional information, calls or weak baselines. See ../proposal/research-design.md.

## Superseded claims in the historical proposal

- Do not claim the first business-analytics MAS benchmark or absence of all prior comparisons.
- Executable verification exists in coding; analytics is not uniquely executable.
- Repeating a query does not verify its semantic correctness.
- Correctness depends on data, task specification and applicable rules; gold answers stay hidden from agents.
- MAST labels alone cannot identify causal mechanisms; combination superiority alone is not statistical synergy.

## Practical output

An auditable acceptance-test suite and cost/reliability guidance for analytics MAS. Measure wrong final answers, correct completion, clarification/abstention and resource use. No workplace productivity or ROI claim without separate evidence.
