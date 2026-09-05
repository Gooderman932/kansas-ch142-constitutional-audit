# Operations

How this repository works: what each part is for, how the parts feed each
other, and what to do in what order.

`README.md` is the index. This is the manual.

---

## 1. What this project is

**A constitutional challenge strategy for L. 2026, ch. 142.** The objective is a
merits ruling and a narrowed or amended statute. Everything here is in service
of that.

What distinguishes it from most such projects is the sequencing, and the
sequencing rests on one bet:

> One person cannot fund a statewide constitutional campaign. But one
> well-organized person can become the evidentiary infrastructure that makes
> *organizational* litigation possible — and nobody in Kansas currently has a
> complete, county-by-county dataset of how these laws are actually being
> enforced.

So the challenge is pursued **records-first**. A complaint filed before there is
a plaintiff with standing, counsel of record, and an enforcement record is worse
than no complaint: it generates adverse precedent that forecloses the next
person. The dataset is what buys the plaintiff, the counsel, and the
organizational backing — and, through Tier 3, it can produce a merits ruling
inside someone else's case without this project filing at all.

The current phase is therefore evidence production, and the near-term product is
**a dataset and the documented provenance behind it**. That dataset serves three
constituencies at once — litigators who need a record, journalists who need
counts, legislators who need facts — which is also the revenue path in
`11 § 2.4` that funds the litigation and survives it.

**Do not read the records-first posture as a decision not to litigate.** It is a
decision about *when*, *who*, and *on what record*. Tier 4 is the objective; the
tiers below it are the conditions that make Tier 4 winnable.

## 2. Two subjects, one machine

| Track | Subject |
| --- | --- |
| `ch142` | L. 2026, ch. 142 (HB 2372) — § 5 unlawful approach of a first responder, § 1 immigration detainer holds, § 9 removal of county approval over 287(g), §§ 2/3/12 fiscal and liability exposure |
| `alpr` | Automated license plate readers statewide — Flock Safety **and** the non-Flock systems |

These are deliberately **not** separate programs. The same sheriff answers both
requests, so adding the ALPR module to a ch. 142 packet costs one page and
doubles the yield. Every tracker carries a `track` column so the outputs stay
separable.

They also genuinely intersect: municipal ALPR data reaches federal agencies
through sharing chains the originating city cannot see, which is the § 1
detainer problem one layer down the stack. See `12 Part IV`.

**The failure mode for a solo operator is two half-built datasets, neither
citable.** Run one records program.

## 3. Architecture

```
ANALYSIS      11-strategic-plan-financial-political-capacity.md
              12-alpr-flock-constitutional-audit.md
                  |   why to do it, in what order, at what risk
                  v
INSTRUMENTS   KORA-requests/          the actual asks
              scripts/                markdown -> print-ready PDF
              exports/kora-pdfs/
                  |   what gets sent
                  v
DATA          trackers/*.csv          what came back, scored on a fixed rubric
                  |
                  v
EVIDENCE      evidence/               provenance, hashes, preserved originals
```

Each layer feeds only the next. Analysis decides what to ask; instruments ask
it; trackers score the answers; evidence proves the answers are what they claim
to be.

## 4. The layers

### Analysis

**`11-strategic-plan-financial-political-capacity.md`** — the ch. 142 track.
Political means, financial means, the five-tier ladder, the 90-day operating
plan, and a candid assessment. The two numbers that drive it: the House
override passed 85–38 against an 84-vote threshold, and all 125 House seats are
on the ballot November 3, 2026. The Senate is fixed until 2028.

**`12-alpr-flock-constitutional-audit.md`** — the ALPR track. Built on the
Kansas Justice Institute's petition in *Grimmett v. City of Wichita*,
No. SG-2026-CV-002760 (Sedgwick Cnty. Dist. Ct., filed July 29, 2026), read in
full. Its consequence for posture: competent counsel already filed, so the role
here is the statewide record and Tier 3 support, never a parallel suit.

Both documents end with a **verification register** separating what was read in
full from what came from secondary reporting.

### Instruments — `KORA-requests/`

| ID | Target | Asks for |
| --- | --- | --- |
| `KORA-01` | Kansas Attorney General | Statewide guidance, training, representation, claims, costs, complaints |
| `KORA-02` | County sheriff / jail / counselor | § 5 enforcement counts, detainer implementation, 287(g), fiscal/insurance/oversight |
| `KORA-03` | Any state or local agency | Vendor-neutral ALPR: contracts, policy, retention, sharing, audit logs, permits |
| `KORA-04` | Olathe Police Department | CAD, dispatch, report, video, retention for the July 11 incident (`SRC-014`) |
| `PRES-01` | Any agency holding evidence | Preservation notice — video, audio, CAD, messages, metadata |

Every template has the same skeleton: **Subject → Request (numbered, itemized) →
Format, segregation, and timing → Fees and scope → Delivery.**

- `pilot-routing.md` — verified custodian, address, portal, phone, and source URL
  for every first-tranche target, with assigned request IDs.
- `pilot-targets.csv` — the same routing as machine-readable rows.
- `ready-20260903-*.md` — county copies with recipient and requester filled in.
- `scripts/render_kora_pdfs.py` — renders the Markdown to US Letter PDFs with
  page numbers, clickable authority links, and a visible `FINAL DRAFT • NOT SENT`
  stamp, plus a combined packet. Requires `reportlab` and `pypdf`.

### Data — `trackers/`

| File | Feeds |
| --- | --- |
| `kora-response-tracker.csv` | Tier 0 scoring: business days to respond, statutory compliance, fee demanded, exemptions claimed, pages produced, whether a denial had a reasonable basis |
| `enforcement-incident-tracker.csv` | Every § 5 charge and detainer hold, with bodycam-preservation and defense-counsel fields |
| `candor-probe-tracker.csv` | Tier 1 disavowal refusals — `quoted_language` matters, because the quote *is* the evidence |
| `alpr-deployment-tracker.csv` | Per agency: vendor, camera count **and its basis**, policy, configured retention, sharing partners, contract term |

Conventions are in `trackers/README.md`. The load-bearing ones: ISO dates, blank
means unknown rather than zero, never guess a boolean, hash on ingest, and a
local path is not a source.

### Evidence — `evidence/`

- `source-manifest.csv` — one row per source: URL, retrieval time, filename,
  bytes, SHA-256, content type, and a `verification_status` of `verified`,
  `partial`, or `blocked`.
- `SHA256SUMS.txt` — verify the whole set with
  `cd evidence && sha256sum -c SHA256SUMS.txt`.
- `evidence/sources/` — **committed.** Preserved originals of public records
  small enough to live in git.
- `/source-documents/` — **gitignored** staging for originals too large or too
  sensitive to commit.

The rule that separates those last two: **a hash whose artifact is only in
gitignored staging is not preservation.** Anything the manifest marks `verified`
must be in `evidence/sources/`.

## 5. The operating loop

1. **Target.** Pick agencies; record routing in `pilot-routing.md` and
   `pilot-targets.csv`.
2. **Assign a request ID** on the `YYYYMMDD-AGENCY-TRACK-SEQUENCE` convention and
   add the tracker row **before** transmission.
3. **Send.** Save the exact outgoing payload and attachments as PDF or `.eml`,
   then hash the preserved copy.
4. **Calendar** the end of the third business day after receipt.
5. **Score** every response on the fixed rubric — days, compliance, fee,
   exemptions, production.
6. **Preserve** what comes back into `evidence/sources/`, hash on ingest, log in
   the manifest.
7. **Escalate** the worst non-compliers under K.S.A. 45-222 (Tier 2).
8. **Publish** the periodic Kansas Enforcement Report with methodology, county
   tables, and source documents.

## 6. The five-tier ladder

Both tracks use it. Ordered strictly by legal risk. Do not skip rungs.

| Tier | Activity | Risk | Window |
| --- | --- | --- | --- |
| 0 | Records saturation | Zero | Weeks 1–8 |
| 1 | Candor probes — disavowal letters, policy-existence, public comment | Zero | Weeks 2–10 |
| 2 | KORA enforcement actions | Low, conditional fees | Months 2–6 |
| 3 | Support the cases that already exist — § 5 defendants, *Grimmett* | None new | Now |
| 4 | Affirmative litigation — only with plaintiff, counsel, dataset, backing | Moderate | Months 6–18 |
| 5 | **Prohibited** | — | — |

**Tier 5 is a hard stop, not a step.** For ch. 142 it is manufacturing an
encounter to provoke a citation (`11 § 0.1`). For ALPR it is interfering with
cameras (`12 § 0.2`). The reasons are stated in full in both documents; the
short version is that a manufactured plaintiff loses, a second charge is
leverage against you in the first, and *Grimmett*'s entire strength is a
law-abiding driver who did nothing.

## 7. Design decisions that carry weight

**Vendor neutrality.** `KORA-03` defines ALPR *functionally* — any system that
automatically captures images of vehicles or plates and makes the resulting data
searchable — then names Flock, Axon, Genetec, Leonardo, Motorola/Vigilant, and
Rekor as non-limiting examples. Topeka runs non-Flock LPR; Lenexa uses
Axon/Genetec/Leonardo. A Flock-only packet returns "no responsive records" from
real ALPR operators.

**`count_basis` before any count.** Three tiers, descending:
`purchase contract` (the only basis that belongs in a published number),
`agency statement` (Wichita's own captain conceded the citywide figure mixed
City-funded devices with an unknown number of private ones), and
`crowdsourced map` (a lead source for targeting and cross-checking — never a
published count). Rows seeded from crowdsourced maps are marked `verified,no`.

**Modules priced separately.** `KORA-02` and `KORA-03` can travel together, but
the custodian is asked to process and price them separately so one burdensome or
disputed item cannot delay the other.

**Ask for records, not answers.** Existing records only — never questions or
newly created summaries. Native electronic records with metadata. Rolling
production and itemized estimates. Item-by-item statutory basis for withholding,
and segregation of open from closed. No confidential sources, tactical details,
or victim PII.

**Nothing is sent on autopilot.** Every draft carries a `Status:` line. Every
rendered PDF is stamped `FINAL DRAFT • NOT SENT`. Transmission is an external
legal communication and requires reviewing the exact outgoing payload and
destination first.

## 8. Legal spine

Checked against the Kansas Revisor on September 3, 2026. Confirm current law,
procedure, and case interpretation with Kansas counsel before filing anything.

| Statute | What it gives you |
| --- | --- |
| K.S.A. 45-218 | Agency must **act on** a request by the end of the third business day; a delay response must state detailed cause and earliest availability |
| K.S.A. 45-219 | Copy charges limited to reasonable fees not exceeding actual attributable cost |
| K.S.A. 45-220 | Governs procedure; bars delay or denial on a technicality |
| K.S.A. 45-221 | Discretionary closures; requires separating open from closed information |
| K.S.A. 45-222 | Civil enforcement, **burden on the agency**, and the fee standard |

Two standards that are easy to overstate, so state them precisely:

- **45-218(d) is a duty to act, not a duty to complete.** Three business days to
  respond; a large production can take longer.
- **45-222 fees are conditional and the test is conjunctive.** A prevailing
  plaintiff recovers costs and reasonable attorney fees only where the denial was
  **not in good faith *and* without a reasonable basis in fact or law.** This is
  meaningfully harder than "no reasonable basis" alone. Plan on conditional fee
  shifting, not fee shifting.

And the constraint that shapes the whole funding model: a pro se litigant
generally cannot recover attorney fees under 42 U.S.C. § 1988
(*Kay v. Ehrler*, 499 U.S. 432 (1991) — verify). Pro se litigation is a cost
center, not a funding strategy.

## 9. Verification discipline

Nothing in this repository has been Shepardized. The rules:

- Every citation is marked for verification. `DISCLAIMER.md` itemizes the
  statutory ones; each audit document carries its own register.
- **A pleading is not a finding.** Paragraph cites to the *Grimmett* petition are
  accurate to that document, which is a party's allegations sourced largely to
  Wichita's own contracts, minutes, permits, and policy — but still allegations.
- **Secondary reporting is a lead.** `SRC-014` is logged `partial` for exactly
  this reason: the underlying Olathe CAD/call record has not been obtained.
- **`verified` means checked against a primary source document**, not against
  reporting about it. Use `partial` when some fields in a row are verified and
  others are not, and say which in `notes`.

## 10. Current state

**Real:** both audit documents; the *Grimmett* petition read in full; the KORA
packet with verified custodian routing; the rendered PDFs; `SRC-008` (Governor
Kelly's April 8, 2026 veto message) preserved and hash-verified.

**Not yet:** **no request has been sent.** `SRC-001` (enrolled HB 2372) and
`SRC-002` (Session Laws Vol. 2) are `blocked` — official URLs verified, but
binary-safe download failed and the corrupted copies were deleted rather than
hashed. Three of the four trackers are empty headers.

**The dataset does not exist yet. The machine that builds it does.**

## 11. Open items before the first send

**Routing and documents disagree on portioning.** `pilot-routing.md` splits
Cherokee, Shawnee, and Wyandotte into a sheriff request (operational: § 5,
detainers, 287(g)) and a separate clerk/UG request (fiscal, insurance,
commission, oversight), each with its own request ID — that is why there are ten
routing entries but seven rendered documents. The `ready-*` copies and PDFs are
single combined documents addressed to all custodians at once.

Sending the combined document to both custodians works, but it contradicts the
routing plan, guarantees each custodian sees items it does not hold, and invites
"no responsive records" noise and inflated fee estimates on the half that is not
theirs. Resolve it one way or the other before sending: either split the
documents to match the routing, or simplify the routing to "same document, two
custodians." The two files should not disagree.

**Time-sensitive, from `12 Part VI`:** Wichita's Flock contract term is reported
to end September 30, 2026. That came from a contract aggregator, not the
contract. Verify it, and verify whether it auto-renews or requires an
affirmative Council vote — those are different opportunities and only one has a
deadline.

**Also unresolved:** acquire clean originals for `SRC-001` and `SRC-002`;
recover the exact URLs for `SRC-012`; obtain the Olathe record behind `SRC-014`.

---

*Not legal advice. See `DISCLAIMER.md`.*
