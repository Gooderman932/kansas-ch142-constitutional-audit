# Evidence Register

This directory stores provenance, hashes, comparison results, and the preserved
originals themselves.

Two locations, and the distinction is the whole point:

- **`evidence/sources/`** — committed. Preserved originals of public records
  small enough to live in git. This is where anything the manifest marks
  `verified` must be, because a hash with no artifact behind it is not
  preservation.
- **`/source-documents/`** — gitignored staging for originals too large or too
  sensitive to commit. Files here do not survive a fresh clone, so the manifest
  must never point at this directory for a source it calls preserved.

## Handling sequence

1. Acquire from the official URL without editing the file.
2. Record acquisition time in UTC, final URL, filename, size, and SHA-256 in
   `source-manifest.csv`.
3. Store the original under `evidence/sources/`, or under `/source-documents/`
   if it is too large or too sensitive to commit -- and if so, say that in the
   manifest notes rather than marking it preserved.
4. Generate derivative text or images only after hashing the original.
5. Record each derivative and its parent source in the manifest.
6. Commit the manifest, the hashes, the reproducible comparison notes, and the
   preserved originals in `evidence/sources/`. Leave only the large or sensitive
   files out.
7. Verify the set at any time with `cd evidence && sha256sum -c SHA256SUMS.txt`.

The initial priority set is:

- `SRC-001`: enrolled Senate Substitute for HB 2372.
- `SRC-002`: 2026 Session Laws of Kansas, Volume 2, containing Chapter 142.
- `SRC-008`: Governor Kelly's April 8, 2026 veto message.
- `SRC-012`: stale Revisor pages, once their exact URLs are identified.
- `SRC-014`: the reported enforcement incident, once its original source is
  identified.

## Current acquisition status

- `SRC-008` is preserved in `evidence/sources/` and hashed. Re-acquired from the
  official URL on September 3, 2026; the SHA-256 reproduced byte-for-byte, which
  confirms both that the recorded hash is correct and that the Secretary of
  State's copy has not changed.
- `SRC-001` and `SRC-002` official URLs are verified, but binary-safe download
  failed in the current sandbox. The failed copies contained UTF-8 replacement
  bytes inside PDF streams and were deleted rather than entered into the
  evidence set.
- `SRC-001` versus `SRC-002` remains blocked until clean original PDFs are
  acquired. Do not infer "no enrollment error" from the separate official HTML
  rendering.
- `SRC-014` is identified and logged as a secondary-source lead. The underlying
  Olathe CAD/call record and original media remain to be obtained.
