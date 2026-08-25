# Trackers

Plain CSV, one row per request / incident / probe. They live in git so the
dataset has a change history, which matters when it is later cited.

| File | Feeds |
| --- | --- |
| `kora-response-tracker.csv` | Tier 0 — records saturation. The response-scoring rubric: days to respond, statutory compliance, fee demanded, exemptions claimed, records produced. |
| `enforcement-incident-tracker.csv` | Tier 3 and the Kansas Enforcement Report — every § 5 charge and § 1 detainer hold identified, by county. |
| `candor-probe-tracker.csv` | Tier 1 — disavowal letters and policy-existence probes. A refusal to disavow is the evidence; record the quoted language. |

## Conventions

- **Dates** — ISO 8601 (`2026-08-13`). Blank means unknown, not zero.
- **Booleans** — `yes` / `no` / blank for unknown. Never guess.
- **`business_days_to_respond`** — computed against K.S.A. 45-218(d)'s
  three-business-day requirement *(verify)*. Excludes weekends and state
  holidays.
- **`doc_sha256`** — hash the file on ingest, before any renaming or conversion.
  This is the chain of custody.
- **`source_url`** — where the document came from. A local path is not a source.
- **`verified`** — `yes` only when confirmed against a primary source document,
  not against reporting about it.

Source documents themselves are gitignored (`/source-documents/`); the trackers
carry the hash and the pointer.
