# Missouri Extension — Kansas CH142 Audit, Extended Slowly
7 Nov 2026 — scaffold only, no Missouri requests drafted for sending yet

## Matt's intent, as I understand it

Kansas is the pilot, not the whole point. The true intent is the similar
constitutional issues in the relevant law across states — first-responder
approach / recording laws, immigration detainer and 287(g) cooperation, and
ALPR surveillance — not Kansas for its own sake. Missouri should be added
as a second state, integrated slowly, and only when the Kansas machine is
working. Do not rush a Missouri send, and do not copy the Kansas packet
verbatim: Missouri law is similar, not identical.

## The reframe that makes this work

Make `state` a variable, not a hard-coded assumption. The Kansas repo already
does half of this: every tracker carries a `track` column (ch142 / alpr).
A Missouri extension adds a `state` column (KS / MO), a `law` column
(the specific statute or bill), and a `records_act` column (KORA / Sunshine).
The operating loop, the tier ladder, the scoring rubric, and the evidence
rules stay the same. Only the statute, the custodian, the deadline language,
and the fee rules change by state.

Do not merge the Missouri Kody case into this project. The juvenile /
termination record is sealed, and the audit is public records. Keep the
quarantine wall from Doc 14: a Missouri audit finding about a public
agency is publishable; anything from Matt's own pending matter is not
in this repo.

## Missouri equivalents — verified 7 Nov 2026

### 1. First-responder approach law — similar, not the same

**Kansas, enacted:** L. 2026, ch. 142, § 5 — unlawful approach of a first
responder, 25-foot law.

**Missouri, enacted:** § 574.207 RSMo, "Interference with a first responder,"
L. 2025, H.B. 225, effective 28 Aug 2025.
- 20 feet, not 25, after a verbal warning, with intent to impede, threaten
  physical harm, or engage in conduct with no legitimate purpose.
- Class B misdemeanor first offense, Class A misdemeanor second or subsequent.
- Express savings clause: "This section shall have no impact on an
  individual's first amendment rights, and shall not restrict the ability
  to observe or record first responders."
- That savings clause is a material difference from Kansas § 5 for any
  First Amendment comparison — do not treat the two statutes as identical.

**Missouri, pending, NOT enacted:** HBs 1868 & 3257 (2026), sponsored by
Rep. Lane Roberts (R-Joplin) and Rep. Barry Hovis (R-Whitewater).
- Would create a new offense of impeding, threatening, or harassing a first
  responder: 25 feet after an oral warning, with intent to interfere,
  threaten, or harass. Class D misdemeanor.
- Last action: 14 Apr 2026, HCS Reported Do Pass, House Crime and Public
  Safety Committee. Bill not on a House calendar, no further action found.
- Do not cite HB 1868 / 3257 as Missouri law. It is a bill, not a statute.

Sources: Missouri Revisor § 574.207; Missouri House bill pages for HB 1868;
Missouri Association of Counties Capitol Report, 10 Apr 2026.

### 2. Immigration detainers and 287(g) — Missouri is further along, by executive action

**Kansas:** ch. 142 §§ 1, 2, 3, 9 — detainer holds, state payment /
representation, and removal of county approval over 287(g).

**Missouri:** no equivalent single statute found in this check. The expansion
has been by executive order and by individual agency agreements:
- Gov. Mike Kehoe, Executive Order 25-04, 14 Jan 2025: directed the
  Department of Public Safety to enter a Memorandum of Agreement for
  Missouri State Highway Patrol troopers to undergo immigration-enforcement
  training under 287(g).
- Missouri State Highway Patrol, Task Force Model, signed 21 Mar 2025.
  Missouri Department of Corrections also has a 287(g) agreement.
- 2026 surge: 119 Missouri agencies signed onto the program just in 2026,
  per ICE data current 30 Sept 2026. As of 21 Oct 2026, Missouri had 144
  Task Force Model agreements in place, in 61 of Missouri's 114 counties.
- Examples close to Matt: Greene County Sheriff, Springfield, entered a
  287(g) Task Force Model agreement 24 Sept 2026, after previously rejecting
  it; the jail had already been housing ICE detainees since 19 Feb 2025 at
  $65 per detainee per day under a separate jail contract. Barry County
  signed 16 Sept 2026. Jasper, Christian, Stone, Lawrence, and Newton
  counties are reported to have Task Force Model agreements. St. Charles
  County Ordinance 5474 authorizes a 287(g) Task Force Model MOA.
- A Missouri Sunshine request in Greene County for the 287(g) agreement was
  reported still pending in early Oct 2026 — the same "agreement not in
  ICE's database, not produced on request" pattern the Kansas packet is
  built to test.

That makes Missouri a *better* 287(g) dataset than Kansas in one respect:
the agreements are numerous, recent, and county-by-county, and the question
is the same — who signed, under which model, what training, what detainer
practice, what money.

### 3. ALPR / Flock — Missouri has no comprehensive statute, but has a governor's order

**Kansas:** no comprehensive ALPR statute; the audit is built on *Grimmett*
and on the records window closing before the Legislature exempts the records.

**Missouri:** also no comprehensive ALPR statute in force.
- Pending reform bill: HB 3192 (St. Louis lawmaker) would limit ALPR use
  to criminal investigations with reasonable suspicion and to missing- /
  endangered-person cases, bar general surveillance and immigration
  enforcement, and require data destroyed within 30 days unless tied to an
  active investigation. Not enacted — do not cite it as law.
- Gov. Kehoe executive order, Sept 2026: new guidelines for state agencies
  and state-funded law enforcement — most license-plate / vehicle data
  deleted within 30 days, vendors barred from selling, sharing, or
  commercializing Missouri-generated data, use restricted to legitimate
  criminal-justice and lifesaving purposes, oversight and accountability,
  and a ban on AI facial-recognition technology used alongside ALPRs.
- Joplin: a Joplin police officer was fired in early 2026 for misusing
  Flock data, and an activist review found a single license plate had been
  searched 395 times. Joplin is in Jasper / Newton counties — Matt's area.
- Crawford County Sheriff gave Flock Safety notice of material breach and
  intent to terminate on 8 Oct 2026 (7 ALPRs in the county).
- Missouri Press Association: ALPR data held by a public agency is a public
  record; a body cannot claim it has not retained a record because it was
  stored in a third-party database.

### 4. Records law — KORA vs. Missouri Sunshine Law

| | Kansas (KORA) | Missouri (Sunshine Law) |
| --- | --- | --- |
| Act | K.S.A. 45-215 et seq. | Chapter 610, RSMo |
| Response deadline | K.S.A. 45-218(d): act by end of 3rd business day | § 610.023.3: respond as soon as possible, no later than end of 3rd business day after receipt |
| What the deadline is | Duty to act, not duty to complete | Same — response, not necessarily completed production; delay must state detailed cause and earliest availability |
| Fees | K.S.A. 45-219: reasonable, not exceeding actual attributable cost | § 610.026: up to $0.10/page for standard pages, plus average hourly clerical duplication rate; research at lowest-cost capable staff |
| Denial | Item-by-item statutory basis, segregation | Written grounds citing the specific provision, due within 3 business days on request; § 610.024 segregation |
| Third-party storage | — | § 610.029: a body cannot contract to store public records in a way that makes inspection harder; records created / maintained by private contractors under agreement are public records |
| Enforcement | K.S.A. 45-222, burden on agency, conditional fees | § 610.027: Attorney General, county prosecutor, or civil action |

The 3-business-day clock is the same in both states, so the Kansas
tracker rubric (days to respond, compliance, fee, exemptions, production)
transfers directly. The fee ceiling does **not** transfer: Kansas templates
default to $25; Missouri fees are per-page + clerical rate, so a Missouri
template needs a Missouri fee ceiling and the same "notify before exceeding"
language, re-priced.

## Missouri pilot — suggested, not sent

Start small, as in Kansas. Three counties first, all with a live reason:

1. **Jasper County (Joplin / Carthage)** — Matt's case county; Joplin PD
   Flock misuse firing in early 2026; Joplin is also the Roberts (HB 1868)
   district. Sheriff, Joplin PD, and county commission.
2. **Greene County (Springfield)** — 287(g) Task Force Model signed
   24 Sept 2026; ICE detainee housing at $65/day since Feb 2025; a
   Sunshine request for the agreement was already reported pending.
3. **Jackson County / Kansas City, or St. Louis County** — large ALPR
   deployment, large detainer volume, and a contrast to the small-county
   pilots. Pick one, not both, for the first tranche.

Statewide, in parallel: Missouri Attorney General (Sunshine guidance,
§ 574.207 training / guidance), Missouri State Highway Patrol (287(g)
Task Force Model, ALPR), and Missouri Department of Corrections (287(g)).

Do not pick all 114 counties. The Kansas failure mode — two half-built
datasets, neither citable — applies across states too.

## Instruments to build (slowly, in this order)

1. **MO-01 — Missouri Attorney General.** Sunshine request for § 574.207
   guidance / training, 287(g) coordination, ALPR guidance, and any
   complaints / enforcement. Mirror KORA-01, re-cited to Chapter 610.
2. **MO-02 — County sheriff / jail.** Sunshine request for § 574.207
   enforcement counts, detainer holds, 287(g) agreement + model + training,
   jail housing / SCAAP money, fiscal / insurance. Mirror KORA-02, with
   Missouri fee language.
3. **MO-03 — ALPR agency module.** Vendor-neutral, as in KORA-03: contracts,
   policy, retention (30-day Kehoe order vs. vendor default), sharing,
   audit logs, permits. Add the Kehoe executive-order question: how the
   agency complied, and whether vendor data was sold / shared / commercialized.
4. **MO-04 — Incident module.** Only for a specific, dated incident with a
   named agency — e.g. the Joplin Flock misuse. Do not send a preservation
   notice without a specific incident, date range, and agency.
5. **Trackers:** add `state`, `law`, and `records_act` columns to
   `kora-response-tracker.csv` (rename in practice to a response tracker
   that covers both acts), and to the ALPR and enforcement trackers.
   Keep `track` (ch142 / alpr) — in Missouri the ch142 track becomes
   "first-responder / detainer / 287(g)" under Missouri law, not Kansas
   ch. 142. Do not label Missouri rows as ch. 142.

## Phased integration — slow, as Matt asked

- **Phase 0 (now):** this scaffold only. No Missouri letters drafted for
  sending, no requests sent, no tracker rows added.
- **Phase 1:** verify the Missouri statutes and bill status against the
  Missouri Revisor (revisor.mo.gov) and the House bill pages, and verify
  the Kehoe ALPR executive order text and the Kehoe 287(g) EO 25-04 text.
  Confirm the Joplin, Greene, and Jackson / St. Louis custodians and
  Sunshine submission routes.
- **Phase 2:** draft MO-01, MO-02, MO-03 for the three pilot counties,
  for Matt's approval of the exact payload and destination, as in Kansas.
  Add tracker rows before transmission.
- **Phase 3:** send the Missouri pilot, log responses on the same rubric,
  and build the first cross-state comparison table: 20 ft vs. 25 ft,
  Class B/A vs. Class D, savings clause present vs. absent, detainer
  practice, 287(g) model, ALPR retention and sharing.
- **Phase 4 (later):** only then consider a wider Missouri ring, and only
  then consider a third state. Do not scale Missouri before Kansas Tier 0
  has produced its first responses.

## What stays Kansas-only, for now

- The Kansas KORA packet, its request IDs, its $25 fee ceiling, and its
  K.S.A. citations. Do not reuse them in Missouri.
- The *Grimmett* Tier 3 support role. Missouri has no equivalent single
  ALPR case identified in this check; do not invent one.
- The Kansas strategic plan's House-vote math (85–38, 84-vote threshold,
  3 Nov 2026 election). Missouri's legislature, governor, and election
  calendar are different, and need their own plan.

## Sources checked 7 Nov 2026

- Missouri Revisor, § 574.207 RSMo — Interference with a first responder.
- Missouri House, HB 1868 bill details — HCS Reported Do Pass, 14 Apr 2026.
- Missouri Association of Counties, Capitol Report Week 13, 10 Apr 2026 —
  HB 1868 / HB 3257 testimony.
- Missouri Attorney General, Sunshine Law FAQs — § 610.023.3, 3 business days.
- News-Leader, 2 Oct 2026 — Greene County 287(g) Task Force Model, 24 Sept 2026.
- Cassville Democrat, 3 Nov 2026 — Barry County 287(g), 144 TFMs statewide,
  61 of 114 counties.
- Flip the Flock, Missouri — no comprehensive ALPR statute; HB 3192 pending.
- Missouri Press Association / MOPress, 2 Oct 2026 — ALPR data is a public
  record; Kehoe executive order, Sept 2026; § 610.029.
- Three Rivers Publishing — Crawford County Flock termination notice, 8 Oct 2026.

All of the above are research, not legal advice. Missouri citations need
verification against the Missouri Revisor and, before any filing, review by
Missouri counsel.
