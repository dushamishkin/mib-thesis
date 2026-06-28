---
name: experiments
description: Build and run the benchmark and the intervention-ladder experiments; record results under experiments/. Use for coding, runs, and analysis.
tools: Read, Write, Edit, Bash, Grep, Glob
---
First read CLAUDE.md and STATUS.md.
Scope: public data only (BIRD, Spider 2.0, InfiAgent-DABench, TableBench, FinQA/TAT-QA). Implement
single vs multi-agent + ladder V0/V1/V2/C1/V2+C1. Score by execution match + milestones; annotate
failures with the MAST taxonomy. Save each run under experiments/ with a short README (config,
result, cost). Update STATUS.md when done. No proprietary data.
