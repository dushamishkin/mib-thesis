# Current status
Updated: 25 September 2026.

## Authority and phase
Supervisor approved the revised title, scope and roadmap, as reported by the author on
23 September. See [approval record](meetings/2026-09-23-supervisor-approval.md).
Phase: candidate-data audit delivered; pilot task construction next. End-October 2026 proposal deadline;
April 2027 completion remains provisional. Formal requirements are still pending.

## Completed
- Broad benchmark audit: 18 families screened and six leading releases inspected;
  76 source files pinned/checksummed. Selected DABstep, LongDA HERD and AgenticDataBench
  calculations reproduced with separate Python/SQL implementations against public gold.
  Recommendation, limitations and 12-base-task draft: benchmark/README.md.
  These are offline feasibility checks, not experimental agent results or a full gold audit.
- Synchronized incoming Zotero workflow changes and made repository freshness mandatory
  before each task; see WORKFLOW.md. Repository and whitespace checks pass.
- Updated research design, positioning and roadmap for the approved direction.
- Added shared agent instructions, session handoff workflow and repository hygiene checks.
- Audited the bibliography against primary metadata; see literature/references.md for coverage,
  newer-version follow-ups and any unresolved checks.
- Configured Zotero as the bibliography source of truth: 29 collection records, 18 reused
  library items and nine imports; all project keys preserved. Better BibTeX Keep updated
  exports without attachment paths. A real note change and restoration both auto-exported;
  checksums and metadata limitations are in literature/references.md. Old-path export disabled.
- Isolated historical proposals and retained the original university template.
- Offline hygiene/link/BibTeX checks pass for 29 indexed records; original archived PDF
  parses as 8 pages and the DOCX containers are readable. Commit hook supplied.

## Next task — pilot task construction
Implement the development suite specified in benchmark/pilot-spec.md. Resolve each task's
document authority and rule semantics, compute references independently, and obtain the
author's semantic/gold review. Keep runtime inputs separate from audit notes and public gold.
Acceptance: 12 fully specified base tasks with paired documents, checked reference outputs,
family IDs, frozen tolerances and verified source manifests. No model campaign yet.

## Before pilot runs
- Complete remaining literature follow-ups in literature/references.md; AgenticData v2
  and LongDA v2 selected sections were inspected during this audit, not fully replicated.
- Confirm formal proposal requirements/date, model/API budget and data suitability.
- Specify the fixed team, V2 independence, C1 schema, caps, scoring and task-level analysis.

## Evidence and blockers
No harness, pilot agent runs, intervention findings or frozen test suite yet. Data-source
recommendation is not final task admission: DABstep rule ambiguities, alternative-source
reuse/provenance and independent human gold review remain explicit gates in the audit.
Scientific novelty is a candidate supported by a targeted review, not a global priority claim. Remote publication
must be verified at handoff; local commits are not automatically visible to other sessions.

## Session handoff
Read AGENTS.md → this file → proposal/research-design.md → relevant task files.
Use `git log -1` and `git status --short --branch` for the actual revision and workspace state;
use WORKFLOW.md's handoff format. Do not embed a self-referential commit SHA here.
