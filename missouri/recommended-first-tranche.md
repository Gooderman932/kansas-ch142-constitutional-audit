# Recommended First Tranche — Missouri
7 Nov 2026 — Matt asked for the tranche that produces the highest
monetizable product, with the most accuracy and the most constitutional
preservation. This is my recommendation, with the send-ready packets
built for it.

## Recommendation

**First send, in parallel:**

1. **Greene County Sheriff — MO-02 (287(g) / detainer)**
   `20261107-GREENE-SO-SUN-001` — Email Records@greenecountymo.gov
2. **Joplin Police Department — MO-03 (ALPR)**
   `20261107-JOPLIN-PD-ALPR-001` — Records Division, 303 E. 3rd St., Joplin
3. **Missouri Attorney General — MO-01 (slow track)**
   `20261107-MOAG-SUN-001` — Email SunshineRequest@ago.mo.gov

**Hold for second step:** Joplin MO-04 (January 2026 Flock incident
investigation), MSHP MO-02/MO-03, KCPD MO-03, Jackson County MO-02.

Send-ready packets are in `missouri/ready/`:
- `ready-20261107-greene-so-sun-001.md`
- `ready-20261107-joplin-pd-alpr-001.md`
- `ready-20261107-moag-sun-001.md`

All three are marked "Final draft; ready for approval — NOT SENT."
Nothing has been sent. Matt approves the exact payload and destination
before any send, as in Kansas.

## Why this tranche wins on all three tests

### 1. Monetizable product — what can actually be sold / licensed

The monetizable product in this project is not a request. It is a citable,
primary-source dataset with a methodology, a denominator, and a hash —
the kind a newsroom, a lawyer, or an advocacy group will license or cite,
as in Kansas Doc 13.

- **Greene County 287(g) agreement:** entered 24 Sept 2026, **not available
  on ICE's database as of 2 Oct 2026**, and the Sheriff's PIO did not provide
  it when requested. The News-Leader's Sunshine request for it was still
  pending in early Oct 2026. A produced copy would be, on the public record
  checked, the **first publication of that agreement**. That is licensable:
  agreement text + model + training + money ($65/day ICE detainee housing
  since Feb 2025, plus any ICE / SCAAP reimbursement).
- **Joplin ALPR audit logs:** a single plate searched ~395 times, typically
  with "DWI" or "Warrants" and **no case number attached**, by an officer
  who accounted for roughly a quarter of the department's Flock searches.
  That is the direct test of EO 26-18 § II.3 (every query must record a
  valid active case number or specific justification). A produced log is a
  citable, quotable dataset, not a summary.
- **AG guidance (slow track):** frames both county datasets with the
  statewide § 574.207, 287(g), and EO 26-18 guidance. On its own it is not
  a dataset — it is a memo. Sent in parallel it costs nothing in time,
  because it does not block the county pilot.

The alternatives score lower on monetization:
- **AG + MSHP alone:** guidance + a statewide MOA, no county dataset,
  and both agencies are slow (AG: 78 open requests in Jan 2026; MSHP:
  July 2026 request forwarded to legal with no production schedule).
  That is a memo in 2–3 months, not a product in 2–3 weeks.
- **KCPD alone:** 12–24 week production, per KCPD's own page. A product
  that arrives in March is not a first product.
- **Greene pair alone (MO-02 + MO-03 to the same sheriff):** operationally
  simple, but Greene's ALPR vendor / deployment is **not verified** in
  Phase 1. A "no records" ALPR answer from Greene is a useful negative,
  but it is not a product. Joplin's Flock deployment **is** verified.

### 2. Accuracy — what can be verified, hashed, and cited

- **Greene:** custodian, email, address, and phone all verified from
  Greene County's own records pages. The 287(g) facts are dated and
  sourced (24 Sept 2026 agreement, $65/day, Feb 2025 housing start).
  The request asks for the agreement itself, not for a summary of it.
- **Joplin:** Flock deployment verified, misuse verified by KCUR / KRPS
  and by the department's own reported response (MSHP criminal
  investigation, monthly audits). The request asks for the policy,
  the retention setting, the sharing list, and the audit logs — all
  primary records, all hashable on ingest.
- **AG:** custodian and email verified, and the AG assigns a request
  number (e.g. 26-017) that can be tracked.
- **What is NOT in the first tranche, and why:** MSHP (custodian name
  conflict: Callahan / Drummond / Gerard Callahan, and a July 2026
  history of misdirecting an ALPR request to MoDOT), Jackson County
  Sheriff (routing not verified), and KCPD (longest production time).
  Those are Phase 3, after the pilot proves the machine.

Accuracy rule for the first report: publish only what a produced record
says, with the hash and the source URL. Crowdsourced counts (DeFlock map)
are leads only, never a published count. The Greene agreement and the
Joplin logs both meet that rule; a guidance memo does not, on its own.

### 3. Constitutional preservation — what disappears if we wait

This is the decisive test, and it points to Joplin first.

- **Joplin ALPR logs are perishable.** EO 26-18 requires permanent deletion
  of non-target plate imagery within 30 days of collection. Flock's own
  published default since August 2026 is **hard deletion on a rolling
  7-day basis** (30 days before that, with existing customers keeping their
  prior setting). Audit / search logs may be retained separately from
  imagery, but that is exactly what MO-03 asks for — and the longer the
  delay, the more likely the answer is "no longer retained." Every week
  of delay risks the underlying evidence for a Fourth Amendment /
  Carpenter-style location-tracking claim and for an EO 26-18 compliance
  claim.
- **Greene 287(g) agreement is recent and still unpublished.** It was
  signed 24 Sept 2026. It is not in ICE's database. Preserve the executed
  copy now, with its model, training list, and money trail, before the
  next news cycle moves on and before a renewal / amendment replaces it.
- **AG guidance is not perishable.** It can be requested in parallel and
  allowed to take months, because it does not lose evidence while it waits.
- **Kansas, for comparison:** the Wichita Flock contract end (30 Sept 2026)
  has already passed unverified, and the Kansas first tranche is still
  unsent. The Missouri pilot should not repeat that pattern — send the
  perishable requests first.

## What the first product looks like

If all three requests produce, the first monetizable product is a
**Southwest Missouri Enforcement Report, Pilot Edition** — 3 agencies,
2 counties, 1 statewide frame:

- Greene County: 287(g) agreement text, model, trained officers,
  detainer counts by month, jail housing revenue, commission approval.
- Joplin PD: ALPR contract, policy versions, retention setting,
  sharing list, audit logs with case-number gaps counted, EO 26-18
  compliance score.
- AG: § 574.207 guidance, 287(g) coordination, EO 26-18 guidance,
  and any complaints received.

That report is licensable because it is: (a) primary-source, (b) complete
for its stated pilot scope, (c) methodologically transparent (request
text, dates, hashes, response times), and (d) comparable — the same
rubric as Kansas, so a buyer can read Kansas and Missouri side by side.

If a request comes back denied / late / incomplete, that is also product:
the denial basis, the delay in business days, and the fee demand are all
scored in the tracker, and a pattern of non-compliance is itself a
Tier 2 (KORA / Sunshine enforcement) story. Do not treat a denial as a
failed pilot.

## Cross-state comparison — scaffold

Fill this table only from produced records, not from secondary reporting.

| Question | Kansas (ch. 142) | Missouri |
| --- | --- | --- |
| First-responder approach law | L. 2026, ch. 142, § 5 — 25 ft | § 574.207 — 20 ft, Class B/A, § 4 savings clause |
| Warnings / citations / arrests, by month | KORA-02, item 2 | MO-02, item 2 |
| Detainer holds, by month | KORA-02, item 9 | MO-02, item 9 |
| 287(g) agreement + model + training | KORA-02, items 7–8 | MO-02, items 7–8 |
| 287(g) money (housing, ICE, SCAAP) | KORA-02, item 13 | MO-02, item 13 |
| ALPR contract + vendor | KORA-03, item 1 | MO-03, item 1 |
| ALPR retention setting | KORA-03, item 4 | MO-03, item 4 |
| ALPR audit logs, case-number gaps | KORA-03, item 5 | MO-03, item 5 |
| ALPR sharing list | KORA-03, item 3 | MO-03, item 3 |
| EO / guidance compliance | — (no Kansas EO found) | MO-03, items 11–12 (EO 26-18, DPS guide 30 Sept 2026) |
| Response time (business days) | K.S.A. 45-218(d), 3 days | § 610.023.3, 3 days |
| Fee demanded / paid | K.S.A. 45-219 | § 610.026, $0.10/page |
| Denial basis, item by item | K.S.A. 45-221 | § 610.021 / § 610.100, § 610.024 |

## Send checklist — before any of the three goes out

- [ ] Matt approves the exact payload and destination for each request.
- [ ] Fill `[DATE]` with the actual send date on each ready file.
- [ ] Add the tracker row **before** transmission, with request ID,
      date sent, and statutory due date (end of the 3rd business day
      after receipt, § 610.023.3).
- [ ] Greene: send to Records@greenecountymo.gov, save the sent email
      as .eml / PDF, hash the preserved copy.
- [ ] Joplin: **call the Records Division first** to confirm the email
      route; if no email is accepted, mail to 303 E. 3rd St., Joplin, MO,
      and save the mailing receipt.
- [ ] AG: send to SunshineRequest@ago.mo.gov, record the AG's assigned
      request number when it arrives.
- [ ] Calendar the 3-business-day response date for each, and the
      90-day fee-withdrawal date (§ 610.026.2) if a fee demand arrives.
- [ ] Do not send MO-04, MSHP, KCPD, or Jackson County in this tranche.
