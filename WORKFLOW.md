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
The project BibTeX is portable and version-controlled. Metadata checks and reading depth are
separate. The old automatic Zotero export must not overwrite it. On the author's machine,
disable that export, import/merge references.bib by DOI/arXiv ID, preserve citation keys, then
review any deliberate export diff. No local Zotero file attachment paths belong in Git.

## Official tool reference
Codex instruction discovery: https://learn.chatgpt.com/docs/agent-configuration/agents-md
Checked 23 September 2026. Workflow recommendations above are project decisions.
