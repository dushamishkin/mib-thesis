# Benchmark work

Current phase: candidate-data audit; no dataset is selected and no tasks are implemented.
Follow [research design](../proposal/research-design.md). Start with DABstep and consider
LongDA for later transfer. Record the audit here before creating a task suite.

For each candidate establish: primary source and version; license and derivative rights;
accessible splits, tables, documentation and gold labels; source authority and rule conflicts;
10–15-task pilot feasibility; reproducible download procedure and checksums.

After selection, commit small task specifications and provenance manifests. Keep bulk data
outside Git in ignored data/. Keep evaluator gold outside the agent-visible runtime mount;
Git exclusion alone does not prevent tool access. Define split boundaries by base task family.
Do not add empty framework folders or synthetic answers before inspecting source data.
