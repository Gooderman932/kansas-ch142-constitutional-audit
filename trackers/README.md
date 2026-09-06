# Trackers

Plain CSV, one row per request / incident / probe / agency. They live in git so
the dataset has a change history, which matters when it is later cited.

| File | Feeds |
| --- | --- |
| `kora-response-tracker.csv` | Tier 0 — records saturation. The response-scoring rubric: days to respond, statutory compliance, fee demanded, exemptions claimed, records produced. |
| `enforcement-incident-tracker.csv` | Tier 3 and the Kansas Enforcement Report — every § 5 charge and § 1 detainer hold identified, by county. |
| `candor-probe-tracker.csv` | Tier 1 — disavowal letters and policy-existence probes. A refusal to disavow is the evidence; record the quoted language. |
| `alpr-deployment-tracker.csv` | The ALPR track's core asset — one row per agency: vendor, camera count and its basis, written policy, configured retention, sharing partners, contract term and renewal date. |

## Conventions

- **`track`** — `ch142` or `alpr`. Both tracks run through one records program;
  this column is what keeps them separable in the output.
- **Dates** — ISO 8601 (`2026-08-13`). Blank means unknown, not zero.
- **Booleans** — `yes` / `no` / blank for unknown. Never guess.
- **`business_days_to_respond`** — computed against K.S.A. 45-218(d)'s
  three-business-day requirement *(verify)*. Excludes weekends and state
  holidays.
- **`doc_sha256`** — hash the file on ingest, before any renaming or conversion.
  This is the chain of custody.
- **`source_url`** — where the document came from. A local path is not a source.
- **`verified`** — `yes` only when confirmed against a primary source document,
  not against reporting about it. `partial` when some fields in the row are
  verified and others are not; say which in `notes`.

Source documents themselves are gitignored (`/source-documents/`); the trackers
carry the hash and the pointer.

## On `count_basis` in the ALPR tracker

Never record a camera count without recording where it came from. The three
tiers, in descending order of usability:

1. **`purchase contract`** — countable, citable, obtained through KORA. This is
   the only basis that belongs in a published report as a number.
2. **`agency statement`** — a council minute or an officer's testimony. Good, but
   Wichita's own captain conceded the citywide figure mixed City-funded devices
   with an unknown number of private ones.
3. **`crowdsourced map`** — DeFlock and its derivatives. A **lead source for
   targeting requests and cross-checking agency answers.** Never publish it as a
   count.

The `alpr-deployment-tracker.csv` rows seeded from crowdsourced maps are marked
`verified,no` for exactly this reason.
