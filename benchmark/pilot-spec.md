# Proposed pilot task specification

25 September 2026. Researcher-facing design draft derived from the
[dataset audit](README.md). This is not a frozen test set or a claim that all proposed
tasks have verified answers. Source revisions and licenses are in the
[manifest](source-manifest.json). The approved V0/V2/C1/V2+C1 labels remain unchanged.

## Pilot composition

Propose 12 base tasks across six calculation families, with two distinct base queries
per family. Every base query has a consistent and a resolvable-conflict document
variant: 24 task instances. Add four matched harmless-document-change instances,
chosen across families before model runs, for 28 instances total. Unresolvable
ambiguity is a separate optional diagnostic after the initial validity checks.

| Family | Two proposed base queries | Documentary distinction | Reference method and admission gate |
|---|---|---|---|
| F1: fee quotation | Mean listed fee for a EUR 10 GlobalCard credit transaction; corresponding EUR 50 quote for another scheme | Basis-point units or null eligibility, one at a time | Decimal row calculation versus SQL aggregation; task 1273 check supports first prototype only |
| F2: eligibility sets | Fee IDs for account type R / ACI B; IDs for a second account/ACI combination | Empty-list wildcard versus empty eligibility | Set comprehension versus normalized relational membership; explicitly define derivative array semantics |
| F3: domestic volume | Domestic share of a merchant's volume; rank schemes by domestic volume | Issuer/acquirer equality versus shopper IP/issuer equality | Independent filtered sums; freeze refusal inclusion and denominator |
| F4: fraud metrics | Monthly amount-weighted fraud percentage; rank two merchant-months by that metric | Fraudulent amount versus fraudulent transaction count | Decimal numerator/denominator versus SQL; use one metric definition throughout each pair |
| F5: reporting windows | Merchant January volume; volume in a second specified calendar month | Calendar month versus rolling/30-day window | Date arithmetic versus independent SQL date bounds; fix year and endpoint conventions |
| F6: conditional fee quotations | Quote for a named account/MCC; compare mean listed quotes across schemes for a fixed profile | Specific MCC exception or account classification versus broad category | Independent eligibility then quote computation; no full merchant billing until overlap semantics are settled |

F1–F6 are proposed strata, not independent real-world enterprises. Parameter changes
within a family are related observations; document variants and repeated runs are
also dependent. Split by full task family, keeping all relatives together. Because
this is a development pilot, do not present its outcomes as held-out evidence.
The main study needs additional independent families; 12 base tasks are not a power
justification. Public dev questions used to develop references cannot later become
an unseen test set.

Task admission must establish that both rival interpretations are computable and
have different outputs, or explicitly classify the task as an invariance control.
This check is based on input semantics before any treatment runs. Record rejected
tasks and reasons. Do not select tasks because C1 or V2 performs well on them.

## Concrete prototype: F1 / credit fee quotation

Research-only ID: `dab-quote-globalcard-credit-10`. It adapts DABstep development
task 1273 and is permanently a development example. Inputs use the pinned fee file;
no payment rows or fee values change between variants.

Proposed agent-facing question, paraphrased from that development task:

> Under the supplied quotation policy, estimate the mean scheduled GlobalCard fee
> for a EUR 10 credit payment. Return the amount in EUR with six decimal places
> and identify the policy passages supporting your eligibility and rate choices.

Each variant supplies the same `fees.json`, the upstream guide, a task-local source
register, and a quotation worksheet note. The scenario documents are clearly marked
as research adaptations, not genuine Adyen policies. Include the same upstream
attribution in both packages.

**Source register, identical in both variants:** the merchant guide's field semantics
are binding for this quotation exercise. The quotation worksheet is an explanatory
draft and cannot amend the guide. Its later date does not make it authoritative.
Only listed task filters restrict eligibility; unspecified attributes remain
unconstrained. A quotation averages eligible schedule rows equally and does not
represent the merchant's actual settled bill. This resolves average weighting and
omitted-field scope without supplying an answer or a matching-row count.

**Worksheet, consistent variant:** a credit quote includes entries whose credit flag
is true and entries whose flag is null; null imposes no credit/debit restriction.
Compute each listed quote from the fixed amount plus the rate applied to EUR 10,
using the guide's rate units. Average eligible rows equally.

**Worksheet, conflict variant:** replace only the eligibility sentence with a claim
that credit quotes include true flags only and null flags are excluded. Keep the
same document title, authority, formula, scope, currency and averaging language.
The binding guide still defines null as unrestricted. The source register supplies
the same resolution evidence to every condition. Match surrounding text length as
closely as practical and record the final document diff before freezing.

The conflict changes a document's claim while preserving the applicable rule and
correct answer. That isolates exposure to inconsistency from a simultaneous change
in the target calculation. In other families, rotate which source/date is binding
so the suite cannot be solved by always choosing the newest, oldest, first or
particular filename. Harmless-change controls retain identical computational rules.

### Researcher-only reference and scoring

The [audit script](../scripts/audit_benchmark_inputs.py) independently computes this
prototype in Python Decimal and SQLite and compares it to public development gold.
Both return EUR 0.120132. The wrong null-exclusion interpretation returns EUR 0.117667.
These are feasibility checks on the data, not outcomes from experimental agents.
The narrative rule interpretation still needs an author review before deployment.

Proposed structured response fields are `answer`, `unit`, `status` and
`supporting_passages`. For this task, success requires the correctly rounded numeric
value, EUR units, an answer status, and evidence consistent with the applicable null
semantics and rate definition. Score format compliance separately from semantic and
computational correctness. Do not accept a contradictory explanation merely because
its number happens to match. Exact six-decimal normalization is appropriate here;
do not inherit a blanket 5% tolerance.

For a resolvable task, unnecessary abstention reduces coverage. Record final incorrect
acceptance explicitly: an incorrect answer released as final remains an error even
if an earlier agent questioned it. The optional ambiguity diagnostic must instead
contain genuinely equal-authority incompatible rules and an ambiguity gold label;
it must not punish agents for declining an indeterminate calculation.

## Interventions and controls

Use the fixed team and intervention definitions in the
[research design](../proposal/research-design.md). All conditions can execute code
and see equivalent source information. C1 agents populate an initially empty schema
for metric, period, scope, units, exclusions and evidence, then reconcile conflicts.
Do not prepopulate it with the correct policy or relevant source passages.

V2 receives the question, the same source corpus, and a separately budgeted checking
attempt. Initially withhold the solver's code and final numeric answer so the checker
constructs its own interpretation and computation; subsequently compare results and
record correction attempts. Freeze the precise withholding/correction protocol before
runs. Independent implementation does not guarantee independent semantic mistakes.

Retain a strong single-agent control and extra-compute MAS control, with matched
resource ceilings and measured consumption. Six configurations over 28 instances
would mean 168 runs per repetition; this is a workload formula, not an authorized
campaign or recommended repetition count. Choose model, caps and repetitions only
after an agreed budget and a small cost calibration.

## Isolation and release boundaries

Create each agent workspace from an explicit allowlist of that task's tables,
source register and documents. Never mount the repository root, the audit download
root, gold files, scoring code, task-generator source, reference computations,
published solutions, previous transcripts or other variants. Disable external
network access for evaluated agents so public gold is not retrievable. Restrict
filesystem access at the execution boundary; `.gitignore` is not isolation.

Audit notes, this specification, the source manifest, and audit evidence contain
reference information and must stay researcher-only. Produce a separate sanitized
runtime manifest for each task. Evaluator labels and reference code stay in a
different mount/process; verifier tools receive no privileged gold access. Reset
task-local memory and scratch outputs between variants and repetitions.

Before release, preserve upstream license/attribution notices and identify every
synthetic document modification. Retain frozen corpus, task and reference hashes,
rules, tolerances and family IDs. Once experiments begin, keep irreplaceable traces
and costs outside scratch with committed manifests/checksums. A new scorer or rule
revision creates a separately named evaluation, never a silent replacement.

## Acceptance before implementation is called complete

All 12 base tasks need complete agent-facing packages, two reference computations,
an author audit of authority and calculations, applicable precision and status rules,
and checked source/variant manifests. The runtime must demonstrably block gold and
cross-task access. The current audit establishes source feasibility and one concrete
prototype; it does not satisfy those full-suite acceptance criteria yet.
