# MIB Thesis — Project Guide

Read this first, then STATUS.md at the start of each session.

## Project and current authority

Master's thesis by Mikhail Dushkin, MIB, Antai / SJTU. Supervisor: Prof. Liu Jialu (刘佳璐).
Retained title: When Analysts Become Agents: A Verification-Aware Benchmark for Multi-Agent LLM Systems in Business Analytics.

The author accepted the refined scope on 2026-09-21. Supervisor agreement is pending. Do not describe the revision as approved by the supervisor or the October proposal as already submitted.

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

## Workflow

1. Read this guide and STATUS.md.
2. Do the task, preserving unrelated user edits.
3. Update STATUS.md and append dated decisions to DECISIONS.md; distinguish author decisions, recommendations and supervisor approval.
4. Commit only reviewed task files. Never blanket-stage pre-existing changes.

## Layout and references

proposal/research-design.md is the current working design. Earlier DOCX/PDF files are historical, not current instructions. ROADMAP.md contains the revised schedule. meetings/ contains correspondence drafts and meeting records; a draft is not a sent message.

literature/references.bib is Zotero Better BibTeX auto-exported: do not edit it manually. Record newly reviewed sources and stable URLs in references.md until they are imported into Zotero. Do not label skimmed or abstract-only papers as fully read. Use existing citation keys where available; never invent keys.

Style: concise, plain language. Report limitations and null results honestly.
