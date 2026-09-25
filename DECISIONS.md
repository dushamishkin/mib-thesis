# Decisions log (append-only, newest first)

- 2026-09-25 — Author requires work against the latest repository. Make synchronization
  mandatory before each task and after handoffs, retry sandbox-blocked fetches through the
  approval mechanism, and report unresolved freshness blockers. Procedure: WORKFLOW.md.

- 2026-09-23 — At the author's explicit request, Zotero's MIB Thesis collection becomes
  the bibliography source of truth; references.bib is a generated Better BibTeX Keep updated
  export and must not be edited manually. This supersedes today's earlier manual-BibTeX
  decision. Reuse existing library items before importing missing works; retain project keys
  and old-key aliases. Configuration and verification are in WORKFLOW.md and literature/references.md.

- 2026-09-23 — Author reports supervisor approval of the revised title, scope and roadmap.
  This supersedes pending-approval status in earlier entries; implementation/hypothesis freeze
  still follows the pilot. Record provenance in meetings/2026-09-23-supervisor-approval.md.
- 2026-09-23 — At the author's request, make repository cleanliness and portable context
  permanent: AGENTS.md is the common instruction source, STATUS.md the current handoff,
  WORKFLOW.md the operating procedure. Preserve meaningful history, not temporary duplicates.
  Use separate task chats and Git branches/worktrees as needed; chat memory is not canonical.
- 2026-09-23 — Bibliography maintenance changes from unattended Zotero export to a verified,
  version-controlled project BibTeX. Preserve existing citation keys, remove local attachment
  paths and import/merge into Zotero separately. Zotero is unavailable in this environment;
  author must disable the old auto-export before it can overwrite the curated file.

- 2026-09-22 — Author selected the proposed title “Coordinating Distributed Business Knowledge in Multi-Agent Analytics: A Controlled Study of Shared Memory and Conflict Resolution”. This supersedes the 21 September preference to retain the original title. Supervisor approval is pending; the email draft now explicitly requests agreement to the title/focus adjustment. The V0/V2/C1/V2+C1 design is unchanged.

- 2026-09-21 — Author accepted the refined scope: preserve the original title and MAS
  business-analytics focus; estimate separate/joint effects of V2 and C1 using
  document-defined rules and controlled consistent/conflicting variants. Primary
  conditions are V0/V2/C1/V2+C1; V1 and broader topology/access experiments are
  optional. Supervisor agreement remains pending. Update active project documents,
  preserve historical proposals, and prepare an email draft (not sent). The main
  experiment follows the end-October proposal rather than preceding it.


- 2026-09-21 — User confirms MAS must remain central because of supervisor interest;
  project proposal deadline is end October 2026. Literature review suggests retaining
  the original verification/context comparison and testing document-defined rules.
  This is a recommendation pending user/supervisor scope agreement, not an approved
  topic change. Remove unsupported broad "first benchmark" claims in the next draft.

- 2026-06-28 — Infrastructure: git repo in this folder + private GitHub; Markdown files as
  continuous memory; Zotero for references; Overleaf (LaTeX) for writing later; Claude Code
  subagents for lit-review / experiments / writing.
- 2026-06-28 — Reframed RQ3 to an intervention ladder (V0/V1/V2/C1/V2+C1) after supervisor
  noted verification alone may be insufficient (MAST Appendix H: +15.6% but "not a silver bullet").
- 2026-06 — Chose Option A: verification-aware benchmark for multi-agent business analytics.
  Public data only; no human subjects; no proprietary data.
- 2026-06 — Supervisor: Prof. Liu Jialu (Antai / SJTU). Proposal submitted.
