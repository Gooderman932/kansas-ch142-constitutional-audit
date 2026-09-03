# Kansas Constitutional Audit

A primary-source dossier and enforcement-record project on Kansas state and
local government practice. Two tracks so far:

- **ch. 142** — L. 2026, ch. 142 (HB 2372) and related measures: the 25-foot
  law (§ 5), immigration detainer holds (§ 1), and the county liability and
  287(g) provisions.
- **ALPR** — automated license plate readers in Kansas: Flock Safety and the
  non-Flock systems everyone forgets to ask about.

The thesis, stated once and true of both tracks: **nobody in Kansas has a
complete, county-by-county dataset of how this is actually being enforced.**
Building that dataset — not filing a lawsuit — is the work. It is what makes
organizational litigation possible, and it is the one asset that organizations
with money and lawyers cannot buy quickly.

## Contents

| File | What it is |
| --- | --- |
| [`11-strategic-plan-financial-political-capacity.md`](11-strategic-plan-financial-political-capacity.md) | **ch. 142.** Political means, financial means, the stress-test ladder, the 90-day operating plan, and a candid assessment |
| [`12-alpr-flock-constitutional-audit.md`](12-alpr-flock-constitutional-audit.md) | **ALPR.** The factual predicate, the legal terrain after *Chatrie*, the statutory vacuum and why the records window is closing, and the audit program |
| [`KORA-requests/`](KORA-requests/) | Draft Attorney General, county, ALPR, and incident-preservation templates; none has been sent |
| [`evidence/`](evidence/) | Source manifest, hashes, and reproducible comparison results; original source files remain gitignored |
| [`trackers/`](trackers/) | Working datasets — both tracks share one records program and one set of trackers |
| [`DISCLAIMER.md`](DISCLAIMER.md) | Scope, authorship, and verification status |

Referenced elsewhere in the dossier series and **not yet in this repository**:
`08-plaintiff-standing.md`, `09-draft-complaint-outline.md`.

## The strategy in one line, per track

**ch. 142** — Build the record, stay out of custody, get a lawyer, sell the
tooling, and move two House votes.

**ALPR** — *Grimmett* has Wichita. Take the other 104 counties, get it done
before the Legislature exempts the records, and hand it to the people already in
court.

## The stress-test ladder

Both tracks use it. Work rungs in order. Tier 5 is a prohibition, not a step.

| Tier | Activity | Risk | Window |
| --- | --- | --- | --- |
| 0 | Records saturation — one vendor-neutral packet to a widening ring of agencies | Zero | Weeks 1–8 |
| 1 | Candor probes — disavowal letters, policy-existence probes, public comment | Zero | Weeks 2–10 |
| 2 | KORA enforcement actions against the worst non-compliers | Low, conditional fee shifting | Months 2–6 |
| 3 | Support the cases that already exist — § 5 defendants; *Grimmett* | None new | Ongoing / **now** |
| 4 | Affirmative litigation — only with plaintiff, counsel, dataset, and backing | Moderate | Months 6–18 |
| 5 | Manufactured encounters (ch. 142); interfering with cameras (ALPR) | **Do not.** See `11 § 0.1`, `12 § 0.2` | — |

## Run one records program, not two

The agencies overlap almost completely — the same sheriff answers both requests.
Adding the ALPR items to a ch. 142 request packet costs one page and doubles the
output. Every tracker carries a `track` column for this reason. The failure mode
for a one-person project is two half-built datasets, neither of them citable.

## Working the trackers

Plain CSV so they open anywhere and diff cleanly in git. One row per request,
incident, probe, or agency. Keep `source_url` and `doc_sha256` populated — chain
of custody is the difference between a dataset and a pile of notes. See
[`trackers/README.md`](trackers/README.md).

## Disclaimer

I am not a lawyer and nothing here is legal advice. Every legal citation is
marked for verification and none of it has been Shepardized. Each audit document
carries its own verification register. See [`DISCLAIMER.md`](DISCLAIMER.md).
