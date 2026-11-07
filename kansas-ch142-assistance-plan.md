# Kansas CH142 Constitutional Audit — Assistance Plan
7 Nov 2026 — review-only on the zip Matt uploaded, plus work I did in this turn

## What this app/project actually is

Not a SaaS app like Lead-Pro. It is a records-first constitutional-challenge
strategy for Kansas L. 2026, ch. 142 (Senate Substitute for HB 2372), plus a
second track on automated license plate readers (ALPR / Flock Safety).

- **ch. 142:** the 25-foot law (§ 5, unlawful approach of a first responder),
  immigration detainer holds (§ 1), county liability and 287(g) provisions.
- **ALPR:** Flock Safety and the non-Flock systems — Topeka (non-Flock),
  Lenexa (Axon / Genetec / Leonardo), and others a Flock-only request would miss.

The thesis, from the README: nobody in Kansas has a complete, county-by-county
dataset of how this is actually being enforced. Building that dataset is what
buys a plaintiff, counsel, and organizational backing a real challenge needs.

The work is ordered by a five-tier ladder. Tier 0 is records saturation,
Tier 1 is candor probes, Tier 2 is KORA enforcement, Tier 3 is supporting
cases that already exist (§ 5 defendants; *Grimmett v. City of Wichita*),
Tier 4 is affirmative litigation only with plaintiff, counsel, dataset, and
backing. **Tier 5 is prohibited:** do not manufacture an encounter to provoke
a § 5 citation, and do not interfere with cameras.

This is research / advocacy, not legal advice. Nothing in the repo has been
Shepardized, per its own DISCLAIMER.md. A Kansas lawyer should review anything
before filing.

## Status right now — verified from the zip and Gmail

- **Requests sent: 0. Responses received: 0. Denied: 0. Late: 0. Incomplete: 0.**
  Every KORA template and every ready copy is marked `Final draft; not sent`.
  The PDFs are stamped `FINAL DRAFT • NOT SENT`.
- **Gmail check, 7 Nov 2026:** I searched for KORA, Flock, Grimmett, Olathe,
  and for mail from sedgwick.gov, jocogov.org, snco.us, wycosheriff.org, and
  cherokeecounty-ks.gov since 1 Aug 2026. **No KORA reply and no agency reply
  was found.** The only KORA hit was a 17 Aug 2026 self-send from Matt to
  himself with Cherokee County / Brady-notice attachments, body empty — not a
  KORA response.
- **Trackers:** `kora-response-tracker.csv` is headers only — empty.
  `candor-probe-tracker.csv` is headers only — empty.
  `enforcement-incident-tracker.csv` has 1 row: the 11 July 2026 Olathe
  incident (KS-20260711-OLATHE-001), status `partial`, secondary report only.
  `alpr-deployment-tracker.csv` has 9 seeded rows (Wichita, Junction City,
  KHP, KBI, Topeka, Lenexa, Overland Park, Olathe, Gardner), most `verified,no`.
  `harvest-register.csv` has 3 candidate findings (HF-007, HF-008, HF-009),
  none yet obtained.
- **Evidence:** only SRC-008 (Governor Kelly's 8 Apr 2026 veto message) was
  verified and preserved. SRC-001, SRC-002, and SRC-012 were `blocked`;
  SRC-014 was `partial`. **That changed in this turn — see below.**

## What I fixed / acquired in this turn

**SRC-001 and SRC-002 are now acquired cleanly — they were blocked before.**

- SRC-001, enrolled Senate Substitute for HB 2372:
  `evidence-attempt/SRC-001-direct.pdf` — 128,261 bytes, 12 pages, PDF 1.4,
  SHA-256 `4975de74e2f21bb37a27394da455b0b9f496cbf7e361fd5cf63fc3a3a8d374f6`
  Verified by text: "Senate Substitute for HOUSE BILL No. 2372 … creating
  the crime of unlawful approach of a first responder…"
  The first URL in the manifest returns an HTML viewer, not the PDF. The
  working download is
  `https://www.kslegislature.gov/b2025_26/bills/download/?apn=b2025_26/year2/ready_for_publication/hb_2372/hb2372_enrolled.pdf`
- SRC-002, 2026 Session Laws of Kansas, Vol. 2:
  `evidence-attempt/SRC-002-session-laws-vol2.pdf` — 7,061,665 bytes,
  1,098 pages, PDF 1.4,
  SHA-256 `529e5127d1a56bf362f59af861e62486a231db88c5514021c6f2c260adf2ee54`
  Verified: "CHAPTER 142 / Senate Substitute for HOUSE BILL No. 2372" at
  text line 10679, and the Secretary of State authentication dated 1 July 2026.

These two files are in `workspace/kansas-ch142-review/evidence-attempt/`.
I did **not** edit your repo zip. To make them count as preservation, they
need to be copied into the repo's `evidence/sources/`, and the manifest
updated — see `evidence-manifest-update.md` in this folder, which has the
exact rows ready to paste.

## Inventory — what is ready to send, and what is not

### Templates (5)
| ID | Target | Status |
| --- | --- | --- |
| KORA-01 | Kansas Attorney General | Final draft; not sent |
| KORA-02 | County sheriff / jail / counselor | Draft; not sent, `[REQUEST_ID]` / `[DATE]` still blank |
| KORA-03 | Any agency, vendor-neutral ALPR | Draft; not sent, `[REQUEST_ID]` / `[DATE]` still blank |
| KORA-04 | Olathe Police Department, 11 July incident | Final draft; not sent |
| PRES-01 | Any agency holding incident evidence | Draft; not sent |

### First tranche — 10 routing entries, 7 rendered PDFs
From `KORA-requests/pilot-routing.md` and `pilot-targets.csv`, all dated
3 Sept 2026, requester Matthew P. Goodman, reply malcolmgoodmen@gmail.com,
mailing 8681 SE 71st, Baxter Springs, KS 66713, fee ceiling $25 by default.

| Request ID (routing) | Agency | Delivery |
| --- | --- | --- |
| 20260903-KSAG-CH142-001 | Kansas Attorney General | Certified mail, call (785) 296-2215 first — no KORA inbox published |
| 20260903-OLATHE-PD-CH142-001 | Olathe Police Dept. | Online portal + mailed parallel copy |
| 20260903-CHEROKEE-SO-CH142-001 | Cherokee County Sheriff | Mail / hand delivery, no email published |
| 20260903-CHEROKEE-CLERK-CH142-001 | Cherokee County Clerk | Email Shelby.Robinson@cherokeecounty-ks.gov, cc rebecca.brassart@cherokeecounty-ks.gov |
| 20260903-JOHNSON-SO-CH142-001 | Johnson County Sheriff | Email SHR-Recordrequests@jocogov.org |
| 20260903-SEDGWICK-FIO-CH142-001 | Sedgwick County FIO (Jennifer Scriven) | Email kora-fio@sedgwick.gov or county form; include physical mailing address |
| 20260903-SHAWNEE-SO-CH142-001 | Shawnee County Sheriff | Email SNSORecordsRequests@snco.us, use Sheriff's form |
| 20260903-SHAWNEE-CLERK-CH142-001 | Shawnee County Clerk / Dept. of Corrections | County form — **needs_routing_confirmation** |
| 20260903-WYANDOTTE-SO-CH142-001 | Wyandotte County Sheriff | Email oru@wycosheriff.org + NextRequest mirror |
| 20260903-WYANDOTTE-UG-CH142-001 | Unified Government, Wyandotte / KCK | NextRequest portal |

Rendered PDFs in `exports/kora-pdfs/`: KORA-01 AG, KORA-02 for Cherokee,
Johnson, Sedgwick, Shawnee, Wyandotte, KORA-04 Olathe, and the combined
`KORA-Request-Packet-All-Seven.pdf`.

## Problems to fix before anything is sent — in order

1. **Routing and documents disagree on splitting.** Routing splits Cherokee,
   Shawnee, and Wyandotte into a sheriff request (operational) and a separate
   clerk / UG request (fiscal, insurance, commission, oversight), each with
   its own request ID — 10 routing entries but 7 documents. The ready copies
   are single combined documents addressed to all custodians at once.
   Sending the combined document works, but each custodian sees items it
   does not hold, which invites "no responsive records" noise and inflated
   fee estimates. Decide one way or the other before sending: split the
   documents to match the routing, or simplify the routing to "same document,
   two custodians."
2. **Request IDs do not match on three ready copies.** Cherokee ready says
   `20260903-CHEROKEE-CH142-001` (routing has `-SO-` and `-CLERK-` versions).
   Shawnee ready says `20260903-SHAWNEE-CH142-001` (routing has `-SO-` and
   `-CLERK-`). Wyandotte ready says `20260903-WYANDOTTE-CH142-001` (routing
   has `-SO-` and `-UG-`). Johnson and Sedgwick match. Fix the IDs so the
   tracker, the letter, and the PDF all agree — otherwise responses cannot be
   logged cleanly.
3. **Everything is 65 days stale.** All ready copies are dated 3 Sept 2026;
   today is 7 Nov 2026. Re-verify every custodian, email, portal, and phone
   before sending — routing was verified 3 Sept, not today. Update the date
   on each letter to the actual send date, and re-check the fee ceiling ($25).
4. **Shawnee Clerk routing is still unconfirmed.** The pilot-targets row is
   marked `needs_routing_confirmation`: the adult jail is not operated by
   the Sheriff, and detention items need to go to the Department of
   Corrections through the Clerk unless the Clerk names a custodian.
5. **Wichita Flock contract deadline has passed.** The repo flags it as
   time-sensitive: the contract term was reported to end 30 Sept 2026, from
   a contract aggregator, not the contract. That date is now past. Verify
   whether it auto-renewed or required an affirmative Council vote, and
   whether a renewal / new contract now exists to request.
6. **The 3 Nov 2026 House election has passed.** The strategic plan (11 § 2)
   rested on all 125 House seats being on the ballot 3 Nov 2026, with the
   override having passed 85–38 against an 84-vote threshold. Check the
   election outcome before relying on the "move two House votes" line.
7. **SRC-012 and SRC-014 are still open.** SRC-012: exact Revisor URLs not
   yet recovered. SRC-014: Olathe CAD / call record and original media not
   yet obtained — KORA-04 is the instrument for that, and PRES-01 should
   only go out for a specific incident, date range, and agency.
8. **No tracker rows exist yet.** Per the repo's own operating loop, add the
   tracker row **before** transmission, with the request ID, date sent, and
   statutory due date (end of the third business day after receipt, K.S.A.
   45-218(d) — a duty to act, not a duty to complete).

## Response log — how I will log it for you

File: `kora-response-log.csv` in this folder. One row per request, using
the same columns as `trackers/kora-response-tracker.csv`, pre-filled with
the 10 routing entries, all `NOT SENT` today.

When a reply arrives, I will score it on the repo's fixed rubric:
- **Received** — date first response, business days to respond
- **Late** — no action by end of the third business day after receipt
- **Denied** — denial basis stated? reasonable basis in fact or law?
- **Incomplete** — partial production, missing items, no segregation of
  open from closed, no item-by-item exemption basis
- **Fee** — fee demanded, fee paid, itemized estimate, over the $25 ceiling?
- **Production** — pages produced, date production complete, documents
  hashed on ingest and preserved with source URL

Escalation under K.S.A. 45-222 is Tier 2 only, and fees are conditional:
a prevailing plaintiff recovers only where the denial was **not in good
faith *and* without a reasonable basis** — conjunctive, harder than
"no reasonable basis" alone. Do not plan on fee shifting.

## Every area I can assist with — and what I will / will not do

1. **Drafting requests** — I can draft, split, and re-date the KORA
   letters, fill bracketed fields, and render updated PDFs with the
   existing `scripts/render_kora_pdfs.py` (needs reportlab + pypdf).
   I will not send anything without you approving the exact outgoing
   payload and destination first. That is the repo's own guardrail, and
   sending is an external legal communication.
2. **Email / mail / portal sends** — I can prepare Gmail drafts for the
   email-routed requests (Johnson, Sedgwick, Cherokee Clerk, Shawnee
   Sheriff, Wyandotte Sheriff), with the PDF attached, for you to approve
   and send. Mail and portal submissions (AG certified mail, Olathe portal,
   NextRequest, county forms) need you — I cannot mail a letter or click
   through a government portal for you, but I can prepare the exact
   text and the filing checklist for each one.
3. **Logging received / denied / late / incomplete** — I can watch Gmail
   for replies, read them, score them on the rubric above, update the
   tracker and the log, hash and preserve productions, and calendar the
   3-business-day due date for each request. Tell me when a reply arrives
   outside Gmail (mail, portal, phone), and I will log that too.
4. **Evidence acquisition** — I can acquire clean public-source PDFs, as
   I did for SRC-001 and SRC-002 in this turn, verify them by text and
   hash, and update the manifest. Still open: SRC-012 URLs, SRC-014
   Olathe record (needs KORA-04), and verifying the Wichita Flock
   contract end / renewal.
5. **ALPR deployment tracker** — I can fill the seeded rows from KORA
   responses (vendor, camera count **and its basis**, policy, retention,
   sharing, contract term), and flag crowdsourced counts as lead-only,
   never as a published count.
6. **Candor probes (Tier 1)** — I can draft disavowal / policy-existence
   probes to the AG and sheriffs, and log quoted language verbatim — the
   quote *is* the evidence.
7. **Enforcement incidents (Tier 3)** — I can log § 5 charges and detainer
   holds by county, with bodycam-preservation and defense-counsel fields,
   and keep the Olathe incident at `partial` until the CAD record arrives.
8. **Data products / publication (Doc 13)** — I can help build the Kansas
   Enforcement Report tables once responses exist, with methodology,
   denominators, and source documents. Nothing publishes until the
   schema changes in 13 Part VI land (trackers must capture what the
   report needs, before saturation).
9. **Intelligence harvest (Doc 14)** — I can log candidate findings to
   `harvest-register.csv` with `generalizes_how`, and keep quarantined
   rows out of this repo entirely while any related matter is pending.
10. **Commercial / funding** — Doc 11 § 2.4 has a revenue path (licensable,
    citable report) that funds the litigation. I can help price and
    package that once there is a dataset — there is no dataset yet, so
    do not sell it yet.

## Recommended next step — your call

Do not send all 10 at once until items 1–3 above are resolved. The
cleanest first send is the smallest, most verifiable tranche:

- **First:** KORA-01 to the Attorney General (certified mail, after the
  (785) 296-2215 routing call), plus KORA-04 to Olathe (portal + mailed
  copy) — these two are single-recipient, no split problem.
- **Second:** the five county pilots, after the split-vs-combined decision
  and the ID fixes, starting with Johnson and Sedgwick (their IDs already
  match, and both are email-routed).

Tell me which tranche you want first, and whether you want me to:
(a) split the Cherokee / Shawnee / Wyandotte documents to match the
routing, or (b) keep them combined and simplify the routing. I will
draft the corrected letters for your approval before anything is sent.
