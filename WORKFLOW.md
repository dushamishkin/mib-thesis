# Working across chats, Codex and editors

## Recommended arrangement
Use one project workspace for the thesis and separate bounded task chats: research/data audit,
implementation, analysis, and writing as needed. Keep a coordination chat for decisions and
supervisor feedback. This is an organizational recommendation, not a claim that every product
shares live files or chat context. One task can stay in one chat while useful; do not make an
endless conversation or repeated compaction the project's only memory.

Git is the shared state. Chats are working discussions. Before switching chats, compacting,
changing tools or finishing a milestone, save decisions and progress in the repository.
Compaction can help a running conversation, but does not publish local changes or guarantee
that a new session knows every earlier decision.

## Canonical context map
| Question | File |
|---|---|
| What is this project? | README.md |
| How must assistants work? | AGENTS.md |
| What is done, blocked and next? | STATUS.md |
| Why did we choose this? | DECISIONS.md |
| What exactly is being tested? | proposal/research-design.md |
| What is the schedule? | ROADMAP.md |
| What supports our claims? | literature/references.md and references.bib |
| What did the supervisor approve? | meetings/2026-09-23-supervisor-approval.md |

Do not mirror these files into multiple chat attachments as independent editable masters.
If a session cannot read GitHub/local files, give it a snapshot with the branch and commit,
then reconcile its output into the repository before starting dependent work.

## Start a session
Repository freshness is required before each new task and when resuming after a handoff.
Run `git fetch --prune` before reading project context. If sandbox permissions block Git
metadata writes, retry through the available approval mechanism; do not silently skip fetch.
For a clean master checkout, run `git merge --ff-only origin/master`. For an existing task
branch, inspect both its upstream and origin/master and reconcile relevant incoming changes
without discarding local work. Re-read any changed instructions and status after updating.
If synchronization remains blocked, report the actual error and revision; do not claim the
checkout is current or begin work that depends on unseen updates. Fetch again before
publication or handoff to detect concurrent remote changes. Never reset, force-push, or
automatically stash user changes to satisfy freshness.

For a clean local checkout, fetch and fast-forward its intended branch. If it diverges or
contains uncommitted work, inspect and preserve that work before merging. Start a task branch
from the current master. Open the repository root in Codex/your editor. Codex discovers
AGENTS.md; in tools without automatic discovery explicitly ask the assistant to read it.
CLAUDE.md is only an adapter to the same rules. No custom plugin or model pin is required.
Only Python 3 and Git are needed for current repository checks; no experiment runtime exists yet.

A ready-to-paste task prompt:

```text
Repository: https://github.com/dushamishkin/mib-thesis
Branch: <branch>; expected starting commit: <sha>
Read AGENTS.md and STATUS.md, then the relevant research-design sections.
Task: <one concrete outcome>
Acceptance criteria: <what must be demonstrably complete>
Relevant files: <paths>
Constraints: <task-specific limits; do not repeat the whole design>
Inspect the actual checkout and preserve unrelated changes. Update canonical records,
run checks, and report commit, checks, blockers, next action and publication state.
```

## Finish / transfer / compact
1. Save results, sources and methodological decisions in their canonical files.
2. Replace stale STATUS.md entries and record substantive decisions with authority/date.
3. Run `python3 scripts/check_repo.py` and `git diff --check`; review changed and untracked files.
4. Commit only relevant paths, publish through an authorized route, and verify the remote revision.
5. Send a short handoff: branch + commit; completed outcome; checks; unresolved questions;
   next concrete action; whether pushed/merged. A patch is a fallback, not a second master copy.

Do not have concurrent writers in the same checkout. If parallel work is explicitly requested,
use separate branches/worktrees and disjoint file ownership; reconcile shared status and
bibliography during integration. Neither shared repository access nor shared project membership
is a substitute for this handoff.

## Automatic local gate
On each clone, enable the committed pre-commit hook once:

```bash
git config --local core.hooksPath .githooks
```

The hook runs the offline repository check and staged whitespace check before commits.
It does not install dependencies, call models or access the network. Hooks are not activated
by cloning alone; each environment must configure them. Review both staged and working-tree
changes if partially staging files. The checks do not replace scientific review.

## Bibliography ownership
Zotero → Better BibTeX → `literature/references.bib` → reviewed Git commit.
Zotero's **My Library / MIB Thesis** collection (`W5I5MZBH`) is the source of truth.
The BibTeX is generated: never edit it manually, including in remote/cloud checkouts.
Request metadata corrections in Zotero when Desktop is unavailable; do not import the
whole generated file back into the library.

On the author's machine, export the collection as **Better BibTeX**, select **Keep updated**,
and target `literature/references.bib` in the active checkout. Automatic export is **On Change**
with a five-second delay. Export notes and attachment files are off; Better BibTeX's
**Fields to omit from export** includes `file` (a global export preference). DOI and URL are
both included. The obsolete export to the former project directory is disabled, retained
for recovery. These local settings are not installed by cloning this repository.

Before adding a paper, search the collection and the entire library by DOI/arXiv ID.
If identifiers are absent, inspect title and authors before importing. Add an existing item
to the collection rather than duplicating it. Pin the project citation key in Zotero's
Citation Key field; legacy keys retained in `tex.ids`/exported `ids` are provenance aliases
and are not guaranteed to resolve in classic BibTeX citation commands.

Make changes in Zotero, wait for automatic export, review its diff, run the repository
checks and commit the generated file with related index updates. Keep reading scope in
literature/references.md. Do not infer full-paper reading or verified venue metadata from
successful synchronization. See that index for the migration audit and live-change test.

Keep one authoritative export destination: do not enable auto-export into concurrent
worktrees. If the checkout moves, re-register Keep updated at the new location and disable
the old destination. Before switching branches or restoring an older generated file, pause
the export; reconcile changes in Zotero and resume afterward. Resolve bibliography conflicts
in Zotero and regenerate, rather than hand-merging the generated file. Automatic export
requires Zotero Desktop to be running; it does not push Git or prove zotero.org cloud sync.

## Official tool reference
Codex instruction discovery: https://learn.chatgpt.com/docs/agent-configuration/agents-md
Checked 23 September 2026. Workflow recommendations above are project decisions.
