# MIB thesis

**Coordinating Distributed Business Knowledge in Multi-Agent Analytics:
A Controlled Study of Shared Memory and Conflict Resolution**

Mikhail Dushkin · SJTU Antai MIB · Supervisor: Prof. Liu Jialu (刘佳璐)

The title above was supervisor-approved according to the author's 23 September report.
On 11 October the author adopts a main-agent/subagent hierarchy, source-checked
experience reuse and counterexample review, with a FinHelm-engine adaptation path.
DataPilot/DS-STAR are conceptual anchors. Revised title and scientific specifications
are in the research design; the [complete English narrative](proposal/proposal-draft.md)
was approved by the author for transfer to the university template on 14 October.
The matching [Word draft](proposal/thesis-proposal-draft.docx) is visually checked;
[review notes](proposal/proposal-review-notes.md) record open fields and checks.
No renewed supervisor approval, installed implementation or agent findings are claimed.

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

Current institutional deadlines and the supervisor-review plan are in [ROADMAP.md](ROADMAP.md)
and [requirements](requirements/README.md). Start with the active task in [STATUS.md](STATUS.md).
