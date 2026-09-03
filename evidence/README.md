# Evidence Register

This directory stores publishable provenance, hashes, and comparison results.
Original source files belong under `/source-documents/`, which is gitignored.

## Handling sequence

1. Acquire from the official URL without editing the file.
2. Record acquisition time in UTC, final URL, filename, size, and SHA-256 in
   `source-manifest.csv`.
3. Store the original under `/source-documents/`.
4. Generate derivative text or images only after hashing the original.
5. Record each derivative and its parent source in the manifest.
6. Commit the manifest, hashes, and reproducible comparison notes, not the large
   source files.

The initial priority set is:

- `SRC-001`: enrolled Senate Substitute for HB 2372.
- `SRC-002`: 2026 Session Laws of Kansas, Volume 2, containing Chapter 142.
- `SRC-008`: Governor Kelly's April 8, 2026 veto message.
- `SRC-012`: stale Revisor pages, once their exact URLs are identified.
- `SRC-014`: the reported enforcement incident, once its original source is
  identified.

## Current acquisition status

- `SRC-008` is preserved and hashed.
- `SRC-001` and `SRC-002` official URLs are verified, but binary-safe download
  failed in the current sandbox. The failed copies contained UTF-8 replacement
  bytes inside PDF streams and were deleted rather than entered into the
  evidence set.
- `SRC-001` versus `SRC-002` remains blocked until clean original PDFs are
  acquired. Do not infer "no enrollment error" from the separate official HTML
  rendering.
- `SRC-014` is identified and logged as a secondary-source lead. The underlying
  Olathe CAD/call record and original media remain to be obtained.
