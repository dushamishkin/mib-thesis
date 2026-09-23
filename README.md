# MIB thesis

**Coordinating Distributed Business Knowledge in Multi-Agent Analytics:
A Controlled Study of Shared Memory and Conflict Resolution**

Mikhail Dushkin · SJTU Antai MIB · Supervisor: Prof. Liu Jialu (刘佳璐)

The study tests when independent executable verification and shared business-context
alignment improve multi-agent analytics using public tables and business-rule documents.
The supervisor approved the revised title, scope and roadmap according to the author's
23 September 2026 report. No pilot or empirical findings exist yet.

## Start here
1. [AGENTS.md](AGENTS.md): shared instructions for Codex, Claude Code and other assistants.
2. [STATUS.md](STATUS.md): current progress and next task.
3. [Research design](proposal/research-design.md): questions, conditions and evaluation.
4. [WORKFLOW.md](WORKFLOW.md): chats, branches, context handoffs and clean working habits.

## Project map
| Path | Purpose |
|---|---|
| [ROADMAP.md](ROADMAP.md) / [DECISIONS.md](DECISIONS.md) | Schedule and decision history |
| [literature/references.md](literature/references.md) | Reading index and metadata audit |
| [literature/references.bib](literature/references.bib) | Generated Zotero bibliography; do not edit manually |
| [literature/positioning-note.md](literature/positioning-note.md) | Contribution boundaries |
| [benchmark/README.md](benchmark/README.md) | Data audit and task construction |
| [experiments/README.md](experiments/README.md) | Run and reproducibility requirements |
| [writing/README.md](writing/README.md) | Thesis writing conventions |
| [proposal/README.md](proposal/README.md) | Current design, original template and history |
| [Approval record](meetings/2026-09-23-supervisor-approval.md) | Supervisor decision provenance |

## Checks
Requires Python 3 and Git; no external Python packages:

```bash
git config --local core.hooksPath .githooks
python3 scripts/check_repo.py
git diff --check
```

The formal project proposal is due at the end of October 2026; final completion around
April 2027 remains provisional. Start with the candidate-data audit in STATUS.md.
