# MIB Thesis — Project Guide

Read this first, every session. Then read STATUS.md for current state.

## What this is
Master's (MIB, Antai / SJTU) thesis by Mikhail Dushkin. Supervisor: Prof. Liu Jialu (刘佳璐).
Topic: a verification-aware benchmark for multi-agent LLM systems in business analytics.

## Core idea
Multi-agent LLM systems often don't beat single agents (MAST, arXiv:2503.13657). We build a
public-data benchmark of business-analytics tasks (which have checkable, executable ground-truth
answers), measure when multi-agent beats single, diagnose failures with the MAST taxonomy, and
test an intervention ladder:
- V0  no verification
- V1  shallow self-check (a critic agent re-reads)
- V2  grounded executable verification (re-run the SQL / recompute the metric)
- C1  structured shared context (for inter-agent misalignment)
- V2+C1  combined
Why analytics: answers are executable, so the grounded multi-level verification the MAST authors
say is missing/needed is actually feasible here. The data is the oracle.

## Hard constraints
- Public data + code only. No human subjects. No proprietary/employer data. Keep employer IP out.
- Deadline target: ~April 2027 (confirm with supervisor).

## Working protocol (this is the continuous memory)
1. Start: read CLAUDE.md + STATUS.md.
2. Do the task.
3. End: update STATUS.md (what changed, what's next). Log real decisions in DECISIONS.md with a date.
4. Commit: git add -A && git commit -m "...".
Keep STATUS.md short and current — it is the single source of truth for "where are we".

## Layout
- STATUS.md       current snapshot (read this second)
- DECISIONS.md    append-only decision log
- ROADMAP.md      July 2026 -> April 2027 plan
- literature/     references, notes, positioning note
- benchmark/      task suite + harness
- experiments/    runs, results, analysis
- writing/        thesis drafts
- proposal/       submitted proposal (docx/pdf)
- meetings/       supervisor notes
- .claude/agents/ task-specific subagents (lit-review, experiments, writing)

## Style
Concise, plain, down to earth. No filler.
