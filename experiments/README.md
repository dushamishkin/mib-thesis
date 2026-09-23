# Experiments

No runs yet. Implement only after the data audit and budget agreement.
Core conditions: V0, V2, C1, V2+C1; strong single-agent and resource controls.
See [research design](../proposal/research-design.md) for definitions and statistical units.

Each retained run needs a manifest recording code commit, task/source versions and checksums,
model/provider/version, prompts, condition, caps, seeds where supported, repeats, timestamp,
tool/environment dependencies, failures/timeouts, tokens, latency and cost. Record actual
usage, not only caps. Preserve raw evidence and checksums in durable storage; commit compact
manifests/summaries here and keep bulk output in ignored artifacts/ or runs/.
Do not store irreplaceable evidence only in .scratch/. Document retrieval locations without secrets.
