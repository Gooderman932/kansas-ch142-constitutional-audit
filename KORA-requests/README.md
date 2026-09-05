# KORA Request Packet

Draft templates for the first records-saturation tranche. These are working
documents, not legal advice, and none has been sent.

## Packet map

| ID | Target | Purpose |
| --- | --- | --- |
| `KORA-01` | Kansas Attorney General | Statewide implementation, training, guidance, representation, claims, and reporting under L. 2026, ch. 142 |
| `KORA-02` | County sheriff / jail / counselor | Local section 5 enforcement, immigration-detainer implementation, 287(g), fiscal exposure, and record-retention rules |
| `KORA-03` | Any state or local law-enforcement agency | Vendor-neutral ALPR contracts, policy, retention, sharing, audit logs, permits, and ALPR-originated enforcement |
| `KORA-04` | Olathe Police Department | Underlying CAD, call, report, video, and retention records for the July 11 incident identified as SRC-014 |
| `PRES-01` | Agency holding incident evidence | Case-specific preservation notice for video, audio, CAD, dispatch, messages, and associated metadata |

The verified first-tranche recipients, delivery routes, and assigned request IDs
are in [`pilot-routing.md`](pilot-routing.md) and
[`pilot-targets.csv`](pilot-targets.csv).

County-specific review copies:

- [`ready-20260903-cherokee-county.md`](ready-20260903-cherokee-county.md)
- [`ready-20260903-johnson-county.md`](ready-20260903-johnson-county.md)
- [`ready-20260903-sedgwick-county.md`](ready-20260903-sedgwick-county.md)
- [`ready-20260903-shawnee-county.md`](ready-20260903-shawnee-county.md)
- [`ready-20260903-wyandotte-county.md`](ready-20260903-wyandotte-county.md)

These copies have recipient and requester details filled in. They remain marked
`Final draft; not sent` and must not be transmitted until the exact outgoing
payload and destination are approved.

`KORA-02` and `KORA-03` are separate modules. They can be sent together, but
ask the custodian to process and price them separately so one disputed or
burdensome item does not delay the other.

## Before sending

1. Replace every bracketed field.
2. Confirm the target agency's custodian and submission procedure. K.S.A.
   45-220(b) allows a written request but generally does not permit an agency to
   insist on a particular form.
3. Set a fee ceiling you can actually approve. The templates default to $25.
4. Create a unique request ID and add the row to
   `trackers/kora-response-tracker.csv` before transmission.
5. Save the exact sent message and attachments as a PDF or `.eml`, then hash the
   preserved copy.
6. Calendar the end of the third business day after receipt. Under K.S.A.
   45-218(d), that is the deadline to act on the request, not necessarily to
   complete a large production.
7. Record every response, estimate, installment, denial, and cited exemption in
   the tracker.

## Request-ID convention

Use:

`YYYYMMDD-AGENCY-TRACK-SEQUENCE`

Examples:

- `20260903-KSAG-CH142-001`
- `20260903-CHEROKEE-SO-CH142-001`
- `20260903-JUNCTIONCITY-PD-ALPR-001`

## Guardrails

- Request existing records, not answers to questions or newly created
  summaries.
- Ask for native electronic records with metadata when reasonably available.
- Ask for rolling production and itemized estimates.
- Require an item-by-item statutory basis for withholding and segregation of
  open material from closed material.
- Do not ask an agency to reveal confidential sources, active tactical details,
  or personally identifying victim information. Accept lawful redaction while
  preserving the right to challenge categorical withholding.
- Do not send a preservation notice unless a specific incident, date range, and
  agency are known.
- Transmission is an external legal communication. Review the completed draft
  and recipient list before sending.

## Authority checked for these templates

- [K.S.A. 45-218](https://www.ksrevisor.gov/statutes/chapters/ch45/045_002_0018.html)
  requires action as soon as possible and no later than the end of the third
  business day after receipt; a delay response must give a detailed cause and
  the earliest availability date.
- [K.S.A. 45-219](https://www.ksrevisor.gov/statutes/chapters/ch45/045_002_0019.html)
  limits copy charges to reasonable fees not exceeding actual attributable
  costs.
- [K.S.A. 45-220](https://www.ksrevisor.gov/statutes/chapters/ch45/045_002_0020.html)
  governs request procedures and bars delay or denial based on a technicality
  unless the requested records cannot be determined.
- [K.S.A. 45-221](https://www.ksrevisor.gov/statutes/chapters/ch45/045_002_0021.html)
  lists discretionary closure provisions and requires separation of open and
  closed information.
- [K.S.A. 45-222](https://www.ksrevisor.gov/statutes/chapters/ch45/045_002_0022.html)
  provides civil enforcement, places the burden on the agency to sustain its
  action, and states the attorney-fee standard.
