# Working instructions — MIB thesis

Read this file, STATUS.md, and the relevant research-design sections before work.
The repository, not chat history or memory, is the durable project record.

## Authority
Mikhail Dushkin · SJTU Antai MIB · Prof. Liu Jialu (刘佳璐).
The author reported supervisor approval of the revised title, scope and roadmap on
23 September 2026. See meetings/2026-09-23-supervisor-approval.md.
The approved title is in README.md; scientific specifications live in
proposal/research-design.md. Approval does not constitute evidence of novelty or results.

## Core question

When do independent executable verification and shared business-context alignment improve multi-agent business analytics, separately and jointly, under consistent and conflicting document-defined rules?

MAS remains the central object. Use a fixed team initially. Keep a strong single-agent control. Public tables plus documentation define the task; tables alone do not determine semantic correctness.

Primary factorial conditions preserve the original labels:
- V0: baseline MAS with ordinary execution but no additional verification/context intervention.
- V2: independent executable verification.
- C1: structured shared business context and explicit reconciliation.
- V2+C1: both interventions.
V1 (text-only critic) is an optional secondary comparator, subject to pilot budget. Do not silently rename V2 as V1.

See proposal/research-design.md for interventions, controls and evaluation. Shared-context schema is populated by agents, never with hidden gold answers. Re-running identical code is not independent verification. MAST labels describe traces; causal conclusions require controlled comparisons.

## Constraints

- Public data and code only; no proprietary/employer data and no human-subject study.
- No automatic superiority assumption for MAS or combined interventions.
- Do not claim the first business-analytics MAS benchmark or a new universal memory protocol.
- No formal protocol guarantees, live Confluence integration, broad topology search or multimodal parsing in the initial scope.
- End-October 2026 project proposal deadline; final submission around April 2027 is unconfirmed.


## Session and handoff protocol
1. Inspect `git status --short --branch` and recent commits. Fetch if network access is available.
   Do not overwrite unrelated changes or automatically reset/rebase divergent history.
2. Read STATUS.md for the active task, blockers and next action; read DECISIONS.md for rationale.
   Report the branch and starting commit when handing work between environments.
3. Make a bounded change. Use a separate branch/worktree for concurrent tasks; never let
   independent sessions edit the same checkout concurrently. Do not delegate unless asked.
4. Record substantive decisions with date and authority in DECISIONS.md. Update STATUS.md
   with delivered work, evidence/checks, blockers and a concrete next action. Replace stale
   status rather than accumulating session diaries. Do not record every routine edit as a decision.
5. Run `python3 scripts/check_repo.py` and `git diff --check`; inspect the complete staged diff.
   Commit only relevant reviewed paths. State whether commits are local, pushed, or merged.
6. Never assume another chat, Codex session or GitHub connector sees unpushed changes.
   Follow WORKFLOW.md for the short handoff prompt and conflict recovery.

## Permanent cleanliness rules
- Give each maintained fact one canonical home; link instead of copying entire documents.
- Keep scratch work in ignored `.scratch/`; never commit downloaded papers, bulk data,
  model outputs, credentials, temporary patches, editor files, or local absolute attachment paths.
- Keep irreplaceable experiment evidence outside scratch with a committed manifest and checksum.
- No empty placeholder files, speculative framework scaffolding, duplicate final/final2 drafts,
  or unused dependencies. Add directories and tooling only when they serve actual work.
- Preserve a historical artifact only when it records an approval, submission or useful source;
  clearly label it and move superseded material out of active paths. Git retains ordinary revisions.
- Delete only task-owned temporary artifacts. Preserve unrelated user modifications and report them.
- Before finishing, inspect untracked files and remove your temporary output. A known user edit
  is not permission to delete it just to obtain a clean status.

## Literature and research integrity
Zotero's `MIB Thesis` collection is the bibliography source of truth.
`literature/references.bib` is a generated, version-controlled Better BibTeX export;
never edit it manually. Edit metadata in Zotero, reconcile by DOI/arXiv ID before adding
records, preserve pinned project citation keys, and review the automatic export diff.
Keep updated must target this checkout and omit attachment paths. See WORKFLOW.md for
configuration and recovery. Never claim Zotero was synced unless confirmed.
`literature/references.md` records reading scope and metadata audit status. Metadata verification
is not full-paper reading. Pin the version supporting a scientific claim; check newer versions
before claiming a gap. Mark unverified records and do not invent authors, dates, keys or findings.
No hidden gold in model prompts, verifier tools or persistent memory. Report negative results,
timeouts, full costs and task-level uncertainty. No production or paid experiment campaign
without an agreed model/budget. Draft emails are not sent emails.

## Code review rules
Flag evaluator leakage, unequal information/resource access, pseudoreplication across variants,
post-hoc selection of favorable tasks, unverified citations and stale approval claims.
Use the design's V0/V2/C1/V2+C1 labels. A combined win alone is not evidence of interaction.
