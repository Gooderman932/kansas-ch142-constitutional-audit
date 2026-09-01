# 12 — CONSTITUTIONAL AUDIT: AUTOMATED LICENSE PLATE READERS IN KANSAS

**Flock Safety and the statewide ALPR network**

Drafted September 1, 2026 · Companion to `11-strategic-plan-financial-political-capacity.md`

> **Not legal advice.** I am not a lawyer. Citations here are drawn from primary
> documents where possible and are marked for verification. Nothing has been
> Shepardized. See `DISCLAIMER.md` and the verification register at the end of
> this file.

---

## PART 0 — READ THIS BEFORE ANYTHING ELSE

### 0.1 The posture question is already answered for you

**Someone else filed first, and they filed well.**

On July 29, 2026, the Kansas Justice Institute filed *Grimmett v. City of
Wichita*, No. SG-2026-CV-002760, in Sedgwick County District Court — a petition
for declaratory and injunctive relief challenging Wichita's ~200-camera Flock
network under **Sections 15 and 20 of the Kansas Constitution Bill of Rights**.
Counsel of record are Samuel G. MacRoberts (#22781) and Jeffrey Shaw (#29767).

This resolves, for the ALPR track, the question that `11` spends Part 0 and all
of Tier 4 on. **You are not the plaintiff here and you should not try to be.**
The best-resourced ALPR case in Kansas exists, it has counsel, it has a clean
plaintiff, and it is pleaded exclusively under the state constitution.

What that leaves is the same thing `11` identified as the real asset, and the
gap is even wider here:

> KJI has Wichita. **Nobody has the other 104 counties.**

The petition itself proves the point. Its Wichita facts are excellent —
purchase contracts, City Council minutes, permitting records, Policy 804, the
transparency portal. Its statewide facts are thin, because assembling them is a
105-county records program and no one has run one. That is the hole this
project fills.

### 0.2 The conduct rule, restated for this subject

`11 § 0.1` prohibits manufactured encounters. The ALPR analogue is more concrete
and the temptation is more available, so state it plainly:

**Do not touch the cameras.** Not obstruction, not paint, not a bag, not a
zip-tied sign, not "just moving the pole." Kansas City-area agencies are already
reporting tampering and treating it as a criminal matter. Every reason from
`11 § 0.1` applies with full force, plus one specific to this track: the
*Grimmett* plaintiff's whole strength is that he is a law-abiding driver who
did nothing. A vandalism prosecution in the same news cycle is the single most
useful gift the other side could receive, and it would be attributed to the
movement, not to you.

Nor should you obscure or alter a plate. That is its own offense and it converts
you from an auditor into a defendant.

**The cameras are the subject of the audit, not its target. The records are the
target.**

---

## PART I — THE FACTUAL PREDICATE

### 1.1 What the technology actually does

Sourced from the *Grimmett* petition, which in turn sources Flock's own
trademark filings, FAQ, and product pages — i.e., these are the vendor's
representations, not an opponent's characterization:

- **Capture.** The Flock Falcon photographs *every* passing vehicle with time
  and location, 24/7, with no per-vehicle limit, and uploads to cloud storage
  (AWS) in as little as 20 seconds.
- **Vehicle Fingerprint.** Search is not limited to plate numbers. The system
  indexes make, color, state of registration, body type (coupe, hatchback,
  convertible, sedan, wagon, SUV, pickup, minivan, work van, semi, bus,
  motorcycle, golf cart, trailer, bicycle), bumper stickers, decals, roof racks,
  bike racks, **missing or covered plates**, broken taillights, and after-market
  wheels.
- **Query.** Location-based and time-based searches — "where has this vehicle
  been, and when." Convoy analysis surfaces vehicles that repeatedly travel
  together.
- **Access.** Web console plus a mobile app on any Android or iOS device,
  including real-time hot-list alerts pushed to phone and smartwatch.

The searchability point is the constitutional point. A plate reader that only
answers "was plate X here" is a very different instrument from one that answers
"show me every vehicle with a roof rack and an out-of-state plate that passed
these three intersections between 9 and 11 p.m." The second is a general
warrant with a search box.

### 1.2 Kansas deployment — what is established and what is not

| Fact | Status | Source |
| --- | --- | --- |
| Wichita: ~200 ALPRs; 191 devices in City purchase contracts | **Well documented** | *Grimmett* pet. ¶¶ 2, 74; City Council agendas/minutes Mar. 19 & Oct. 15, 2024 |
| The 191 figure is a **floor, not a ceiling** — privately purchased cameras are connected to the network | **Documented** | *Grimmett* pet. ¶¶ 69, 74; WPD Capt. Aaron Moses, Council minutes Oct. 15, 2024 |
| HOAs hold right-of-way permits for Flock cameras (Crestlake HOA, May 2024; Vickridge HOA, six cameras, July 2025); Eastborough permit discussions | **Documented** | *Grimmett* pet. ¶¶ 70–72 |
| Lowe's, Walmart, Home Depot cameras on private property shared with WPD | Alleged | *Grimmett* pet. ¶ 73 |
| WPD Policy 804: Flock data stored **at least** 30 days, indefinitely "whenever directed by a supervisor" | **Documented** | *Grimmett* pet. ¶¶ 86–88; Ex. 17 |
| Wichita's Flock contract term ends **September 30, 2026** | **Verify immediately** | Contract-tracking aggregator |
| WPD and KHP historically stored ALPR data via Houston HIDTA, six-month retention | Verify — may be dated | KLRD ALPR memo |
| Overland Park ~77 cameras; Olathe ~69 | Crowdsourced, unverified | MyTownView / DeFlock-derived |
| Topeka PD uses ~20 LPR devices, **not Flock** | Reported | KSNT |
| Lenexa uses Axon, Genetec, and Leonardo — **not Flock** | Reported | KCUR / Johnson County Post |
| KC metro area: ~1,500+ ALPRs, more than half Flock | Crowdsourced | DeFlock |
| Gardner switched its Flock cameras **off** (Aug. 20, 2026) | Reported | Johnson County Post |
| Junction City slowed its Flock expansion after metro cancellations | Reported | reporting, Aug. 2026 |

**Two methodological warnings, and they matter more than they look.**

*First: this is not a Flock audit.* Topeka and Lenexa run non-Flock ALPR. A
records program written around the word "Flock" will return "no responsive
records" from agencies that are doing exactly the same thing with Axon, Genetec,
Leonardo, Motorola/Vigilant, or Rekor gear. **Every request in this program must
be vendor-neutral and define ALPR functionally.** This is the most common
drafting error in ALPR records work and it is free to avoid.

*Second: crowdsourced camera maps are a lead source, not evidence.* DeFlock and
its derivatives are volunteer-mapped. Use them to target requests and to
cross-check agency answers. Never cite them as the count. The count comes from
purchase contracts, invoices, and permits — which is precisely why the records
program is the asset.

### 1.3 The sharing architecture — the part that breaks every containment story

The standard agency defense is "our policy limits access." The *Grimmett*
petition shows why the policy is close to irrelevant:

- Wichita shares database access with **hundreds** of other law enforcement
  agencies (pet. ¶ 89).
- Wichita gives access to **Junction City**, which in turn shares with hundreds
  of agencies including the **FBI**, the **U.S. Postal Inspection Service**,
  **Wright-Patterson Air Force Base**, a **district attorney's office in Texas**,
  and the **Alabama Department of Corrections** (pet. ¶ 10).
- Wichita would not know if Junction City passed Wichita's data onward (pet.
  ¶ 11).
- WPD officers serving on federal **task forces** share informally, outside
  Policy 804 entirely (pet. ¶ 89).
- The *Wichita Eagle* reported in 2022 that once shared, "Wichita police
  officials have no control over how those outside agencies use it and no way to
  flag unlawful searches," and "[o]ut-of-state agencies could use the city's
  database to enforce laws that don't exist in Wichita" (pet. ¶ 90).

That last clause is the whole ballgame for the § 1 / ch. 142 intersection — see
Part IV.

**The audit implication:** the sharing list is the highest-value single record
in this entire program. It is one document per agency, it is not investigative
material, it is hard to exempt, and it converts "our city has 12 cameras" into
"our city has contributed to a national database queried by parties we cannot
name." Request it from every agency, every time.

### 1.4 The Kansas abuse record — already established, on the record, with case numbers

You do not have to argue that ALPR systems get abused in the abstract. Kansas
has three documented cases, all in the *Grimmett* petition:

| Officer | Agency | Conduct | Outcome |
| --- | --- | --- | --- |
| Victor Heiar | Kechi PD | Used Flock to track his estranged wife; "tapped Wichita's surveillance system." Search justifications logged as `test`, `invest`, `investigation`, `ab501`, `123abv`, `****` — none flagged | Convicted, *State v. Heiar*, No. 2022-CR-001620 (Sedgwick) — K.S.A. 21-5839 (unlawful use of computers), 21-5427(a)(1) (stalking); KS-CPOST revoked certification |
| Lee Nygaard | Sedgwick PD (Chief) | Reportedly used Flock **164 times** to track an ex-girlfriend and her new boyfriend | Resigned; KS-CPOST revoked certification |
| Kyle Rector | Bonner Springs PD (Detective) | Allegedly used ALPR to track his wife and two men | Charged, 18 counts — *State v. Rector*, No. WY-2026-CR-000309 (Wyandotte) — stalking, unlawful use of computers, breach of privacy, official misconduct |

The Heiar detail is the one to lead with in any testimony or briefing: **the
audit field accepted `****` as a reason and nothing flagged it.** That is not a
policy failure at the margin. It is proof the audit log was decorative. It is
also directly responsive to Flock's August 2026 announcement that it will
*begin* requiring case codes and auto-suspending abnormal accounts — an implicit
concession that until now it did neither.

Nationally, per reporting summarized by the Kansas Press Association (Aug. 14,
2026): nearly 50 officers charged or accused of unauthorized tracking of
personal contacts; six Savannah, Georgia employees fired for misuse.

### 1.5 The vendor's own August 2026 retreat

On August 14, 2026, Flock announced it would:

- cut **default retention from 30 days to 7**;
- add "Evidence Mode" for case-specific preservation;
- add "offense filtering" to control which agencies can access what;
- require **case codes** on searches by year-end; and
- **auto-suspend** users flagged for abnormal activity.

Flock reports roughly **120,000 cameras** nationally and contracts with about
**40% of U.S. police departments**. More than 50 communities across 23 states
have canceled, declined, or suspended since the start of 2026.

**Use this correctly.** It is not a win to celebrate; it is an admission to
document and a baseline to hold agencies to. Two concrete uses:

1. Every Kansas agency whose written policy still specifies 30 days or longer is
   now **out of step with its own vendor's recommendation.** That is a question
   for a city council or county commission that requires no civil-liberties
   framing at all.
2. A vendor-side default is not a legal limit. It can be changed back by
   contract or by an agency setting. Ask, in writing, for the **configured**
   retention value in the agency's own tenant — not the vendor's default.

---

## PART II — THE LEGAL TERRAIN

### 2.1 The Kansas problem, stated honestly

**Kan. Const. Bill of Rights § 15** tracks the Fourth Amendment nearly word for
word. And the Kansas Supreme Court has said it means the same thing:

- *State v. Cleverly*, 305 Kan. 598, 604 (2016) — § 15 provides "at least the
  same protections" as the Fourth Amendment *(verify)*.
- *State v. Thompson*, 284 Kan. 763, 779–80 (2007) — canvasses reasons § 15
  *could* diverge, then states that the court follows the U.S. Supreme Court's
  interpretation of the Fourth Amendment *(verify)*.
- *State v. Talkington*, 301 Kan. 453, 462 (2015) — Kansas applies both the
  *Katz* privacy test and the *Jones/Jardines* property test *(verify)*.

This is the central strategic fact of the ALPR track, and it cuts both ways.

**Against:** Kansas is not Massachusetts or New Jersey. You cannot win here by
pointing at a more protective state constitution the way *Commonwealth v.
McCarthy*, 484 Mass. 493 (2020), did under art. 14 *(verify)*. Lockstep
interpretation means a § 15 claim rises or falls with federal Fourth Amendment
doctrine — which is why the *Grimmett* petition expressly says it is bringing a
§ 15 claim only, while conceding "a Fourth Amendment analysis is pertinent"
(pet. n.99).

**For:** federal doctrine just moved, hard, in the right direction.

### 2.2 *Chatrie* changed the board in June

***Chatrie v. United States***, No. 25-112, 609 U.S. ___ (June 29, 2026) — the
Supreme Court held **6–3** (Kagan, J.) that obtaining a person's cell-phone
location data through a geofence warrant is a Fourth Amendment **search**,
notwithstanding the third-party doctrine. Individuals retain a reasonable
expectation of privacy in location history even when a third party holds it. The
Court expressly reserved probable cause and particularity for another day.
*(Verify the holding and vote against the slip opinion before citing.)*

Why it matters more for ALPR than for anything else:

- The government's best ALPR argument has always been the **third-party /
  public-exposure** package: *United States v. Knotts*, 460 U.S. 276 (1983) — no
  reasonable expectation of privacy in movements on public roads — plus
  *Smith v. Maryland*'s third-party rule. *Chatrie* narrows the second half of
  that package at the Supreme Court level, and does it for **location data
  specifically**.
- ALPR is a *harder* case for the government than geofencing on one axis: a
  geofence query is retrospective and bounded to a place and time window that a
  magistrate at least sees. A standing ALPR network collects on **everyone,
  continuously, with no judicial officer in the loop at any stage.** There is no
  warrant to narrow.
- It is *easier* for the government on another axis: plates are exposed to
  public view by legal mandate, and *Knotts* is still on the books.

The honest read: *Chatrie* does not decide ALPR, but it removes the government's
cleanest doctrinal shortcut and it is four months old. Any Kansas brief, comment
letter, or testimony written after June 29, 2026 that does not engage it is
already stale.

### 2.3 The mosaic line — the cases that actually carry the argument

| Authority | Holding relevant here | Why it matters | Status |
| --- | --- | --- | --- |
| *United States v. Jones*, 565 U.S. 400 (2012) | GPS tracking = search (trespass theory); five Justices concurring on aggregation | Origin of the mosaic theory; the concurrences are the ALPR argument | Verify |
| *Carpenter v. United States*, 585 U.S. 296 (2018) | Acquiring 7 days of CSLI is a search; third-party doctrine does not extend to comprehensive location records | The controlling frame: comprehensiveness, retrospectivity, cheapness, inescapability | Verify |
| *Chatrie v. United States*, 609 U.S. ___ (2026) | Geofence location data = search despite third-party doctrine | The newest and most favorable authority | **Verify — post-dates most secondary sources** |
| *Leaders of a Beautiful Struggle v. Baltimore Police Dep't*, 2 F.4th 330 (4th Cir. 2021) (en banc) | Aerial wide-area surveillance program was a search; its **warrantless operation** violated the Fourth Amendment | Closest structural analogue: a standing, city-wide, everyone-all-the-time program. Cited in the *Grimmett* petition | Verify |
| *Commonwealth v. McCarthy*, 484 Mass. 493 (2020) | Mosaic theory applies to ALPR; four cameras insufficient, but a network could be | The only major state high-court ALPR merits decision; sets the "how many cameras" question | Verify |
| *United States v. Knotts*, 460 U.S. 276 (1983) | No REP in movements on public roads | **The government's lead case.** Answer it directly; do not pretend it isn't there | Verify |
| *Kyllo v. United States*, 533 U.S. 27 (2001) | Sense-enhancing technology not in general public use | Secondary, but useful on Vehicle Fingerprint | Verify |
| *Florida v. Jardines*, 569 U.S. 1 (2013) | Property-based baseline | Paired with *Jones* in the Kansas framework | Verify |

### 2.4 The Kansas-specific multiplier nobody is using: *Kansas v. Glover*

***Kansas v. Glover***, 589 U.S. 376 (2020) — the Supreme Court held that when
an officer runs a plate and learns the registered owner's license is revoked, he
may infer the owner is driving and has reasonable suspicion for a stop, absent
information to the contrary *(verify)*.

*Glover* was a plate check by an officer who chose to run one plate. Combine it
with a network that runs **every** plate, **continuously**, and matches against
hot lists in real time, and the doctrine does work it was never asked to do:
reasonable suspicion becomes an automated output. The volume of stops available
under *Glover* × ALPR is not a function of officer judgment at all.

This is a Kansas case, decided on Kansas facts, and it is the sharpest available
way to explain to a Kansas audience — including a sympathetic conservative
legislator — what changes when plate-checking is automated and universal. **As
far as I can tell nobody has made this argument in the Kansas ALPR debate.** It
is the most valuable original contribution available to this project on the law,
as opposed to the facts.

Two things it needs before it is usable, both of which are records questions:

1. **Hot-list composition** — what lists does each agency's system match
   against, who maintains them, and how are entries removed? *(Wisconsin
   reporting on wrongful stops from inaccurate plate data is the failure mode.)*
2. **Stop-generation data** — how many stops in agency X originated from an ALPR
   alert, and what were their outcomes? If no agency tracks this, that fact is
   itself the finding, and it is a clean, non-ideological ask of a city council.

### 2.5 Section 20 — the interesting long shot

*Grimmett* Claim Two pleads **Kan. Const. Bill of Rights § 20**: "This
enumeration of rights shall not be construed to impair or deny others retained
by the people; and all powers not herein delegated remain with the people."

The theory, in the petition's own structure: unenumerated rights get the same
protection as enumerated ones; the right to be free from suspicionless
surveillance is among them; and separately, the people never *delegated* a power
of dragnet surveillance, a power so expansive it could only be conferred by
express enumeration. The Wyandotte Convention of 1859 could not have imagined
the technology, but § 20 is precisely the contingency clause the delegates wrote
for that problem (pet. ¶¶ 227–241).

**Assessment:** this is the most likely claim to be dismissed and the most
valuable one if it survives. Because § 15 is interpreted in lockstep with the
Fourth Amendment, § 20 is the only route to a Kansas-specific rule that does not
wait on the U.S. Supreme Court. Expect the City to argue § 20 is not an
independent, judicially enforceable source of rights. **Watch this ruling
closely — it is the single most consequential thing that will happen in Kansas
surveillance law in the next twelve months**, and it will happen in a district
court in Sedgwick County with almost nobody paying attention.

---

## PART III — THE STATUTORY VACUUM AND THE CLOSING WINDOW

### 3.1 Kansas has no ALPR statute

The Kansas Legislative Research Department states it flatly: **"No current
Kansas state statute addresses ALPR data or policies specifically."** *(Verify
against the current memo; confirm the publication date.)*

Consequences:

- No statutory retention cap. Retention is whatever each agency's policy says —
  WPD Policy 804 says 30 days minimum and indefinite on a supervisor's say-so.
- No audit or reporting mandate. Nobody has to tell anyone how many searches were
  run, by whom, or why. The Heiar case is what that produces.
- No restriction on interstate or federal sharing.
- No warrant requirement for historical queries.
- No purpose limitation with teeth.
- **And — critically — no categorical KORA exemption for ALPR data.**

At least 12 states have ALPR statutes (Alabama, Arkansas, California, Maine,
Maryland, Minnesota, Montana, Nebraska, New Hampshire, North Carolina, Utah,
Vermont) *(verify current list)*. Kansas is not among them.

### 3.2 The window is closing, and the trap is in the fine print

**Kansas SB 305 (2021)** would have authorized ALPR collection, limited use to
"legitimate law enforcement purpose," barred commercial sale, and required
written policies with retention periods and audit processes. It also would have
**exempted ALPR data from the Kansas Open Records Act.**

Read that again. The most likely form of Kansas ALPR "regulation" is a bill that
trades modest use limits for a **records exemption** — and the records are the
entire basis of this project and of any future litigation.

**Operational consequence, and it is the most important sentence in this
document:** the statewide records program in Part V should be run **now**, at
speed, while ALPR data and ALPR administrative records are still ordinary public
records. A 2027 statute could foreclose the dataset permanently. Records you
have are records you keep; records you did not request may become records nobody
can get.

By contrast, in 2026 **Sen. Kenny Titus (R)** offered an amendment that would
have restricted mounting ALPRs on utility poles and other structures absent a
warrant or commercial/recreational zoning — and stated that automated camera
data **would be public record subject to KORA**. *(Verify the bill number,
vehicle, and disposition.)* That is the opposite trade and it is the model to
support.

### 3.3 The 2027 ask, in order of viability

Mirroring `11 § 1.5`, and noting that ALPR has something ch. 142 does not: a
**cross-ideological coalition**. KJI is a libertarian public-interest firm; the
ACLU runs a national "Get the Flock Out" campaign; the cancellations sweeping
23 states are being voted by city councils of every political composition. This
is not a left-right issue in 2026 and should never be framed as one.

1. **A retention cap.** Seven days, matching the vendor's own new default. This
   is now the easiest ask in Kansas surveillance policy — the company already
   conceded it, so no legislator has to be first.
2. **An audit and reporting mandate.** Searches, searcher, stated reason, case
   number, and an annual public report per agency. Cheap, popular, and it makes
   every future case better. The Heiar `****` fact sells this by itself.
3. **A sharing restriction.** No out-of-state or federal sharing absent a warrant
   or a written agreement naming the recipient and purpose. This is where
   California's SB 34 lands, and it is where the ch. 142 intersection lives.
4. **A warrant requirement for historical queries** beyond a short window.
   Harder, but *Chatrie* gives it a spine.
5. **Explicitly preserve KORA coverage.** Not a headline ask — a line item you
   must defend in every draft, because it will be the thing quietly traded away.
6. **A ban.** Not viable. Do not lead with it.

---

## PART IV — WHERE THIS TRACK MEETS CH. 142

The two audits in this repository are not separate subjects. They intersect at
one point and it is a sharp one.

`11` documents ch. 142 § 1 (immigration detainer holds) and § 9 (removal of
county commission approval over 287(g) agreements). This audit documents a
statewide vehicle-location database that Kansas municipalities share with
**hundreds** of agencies including federal ones, over which the originating city
retains **no control and no visibility** (*Grimmett* pet. ¶¶ 10–11, 89–90), and
into which WPD task-force officers feed informally, outside their own policy.

The *Wichita Eagle*'s line — "[o]ut-of-state agencies could use the city's
database to enforce laws that don't exist in Wichita" — is the same structural
problem as § 1, one layer down in the stack. A Kansas city with no 287(g)
agreement and no position on immigration enforcement may nonetheless be
supplying the location data on which a detainer-generating stop is built.

**Three questions that belong in every records request in both programs:**

1. Does the agency's ALPR sharing list include any federal agency — DHS, ICE,
   CBP, HSI, FBI, USPIS, a JTTF, or a DoD installation? Name each.
2. Has any ALPR query been run by, or at the request of, a federal immigration
   authority, and is that logged in a way the agency can produce?
3. For agencies with a 287(g) agreement or that honor detainers under ch. 142
   § 1: was ALPR data used in any stop, hold, or transfer?

If the answer to any of these is "we don't know" — and for most agencies it will
be, because the sharing architecture is designed so they don't — that is a
finding, and it is a finding a county commission can act on under the budget and
insurance levers in `11 § 1.4`.

---

## PART V — THE AUDIT PROGRAM

Same ladder as `11 Part III`. Same rule: do not skip rungs, do not reach Tier 5.

### TIER 0 — RECORDS SATURATION (zero risk) · Weeks 1–8

Vendor-neutral ALPR request packet. Define the subject functionally — *any
system that automatically captures images of vehicles or license plates and
makes them searchable* — and name Flock, Axon, Genetec, Leonardo,
Motorola/Vigilant, and Rekor as examples without limiting to them.

**Request, per agency:**

| # | Record | Why it matters |
| --- | --- | --- |
| 1 | All vendor contracts, quotes, invoices, purchase orders, renewals | The camera count floor. Contracts are not investigative records |
| 2 | The written ALPR policy, all versions, with adoption dates | Establishes whether a policy exists at all — a Tier 1 finding either way |
| 3 | **The complete list of agencies with which data is shared, in both directions** | *The single highest-value record in this program* |
| 4 | Configured retention setting in the agency's own tenant, not the vendor default | Tests the agency against Flock's new 7-day recommendation |
| 5 | Audit logs / search logs, aggregate: number of searches, by user, with stated reasons, redacted as needed | The Heiar record shows what these contain |
| 6 | Any MOU, task-force agreement, or data-sharing agreement with a federal agency | The ch. 142 intersection |
| 7 | Right-of-way permits for camera placement, including to private parties and HOAs | Wichita's HOA permits were found this way |
| 8 | Council/commission agenda items, minutes, and staff reports on ALPR acquisition | Establishes whether there was ever a public vote |
| 9 | Hot-list sources and the process for adding/removing entries | Feeds the *Glover* argument (§ 2.4) |
| 10 | Any record of stops or arrests originating from an ALPR alert | If not tracked, that is the finding |

**Sequence:** (1) Wichita + KHP + KBI + 5 pilot counties → (2) the 25 largest
agencies by population → (3) all 105 counties plus every municipal PD over
5,000 population.

**Expect** exemption claims under K.S.A. 45-221(a)(10) (criminal investigation
records) for items 5 and 10, and possibly 3. Items 1, 2, 7, and 8 are
administrative and hard to withhold. Structure the request so a bad exemption
claim on one item does not swallow the rest — separately numbered items, and an
express request for segregation and for a written statement of the specific
exemption per item.

**Output:** the statewide ALPR deployment and sharing dataset. *This is the
asset.* Track it in `trackers/alpr-deployment-tracker.csv`.

### TIER 1 — CANDOR PROBES (zero risk) · Weeks 2–10

- Policy-existence probes: does a written ALPR policy exist? Agencies with
  cameras and no policy are the story.
- Retention probes: does the configured value match the vendor's new 7-day
  recommendation, and if not, why?
- Federal-sharing disavowal letters: *will you state in writing that no federal
  immigration authority has queried or received your ALPR data?* A refusal to
  answer is the evidence.
- Public comment at city councils and county commissions — the same free podium
  as `11 § 1.4`, and here the fiscal frame is even cleaner: this is a recurring
  subscription line item with a renewal date.

### TIER 2 — KORA ENFORCEMENT (low risk, fee-bearing) · Months 2–6

Identical mechanics to `11 § 2.3`. File on the worst non-compliers.
K.S.A. 45-218(d)'s three-business-day response requirement and K.S.A. 45-222's
fee provision apply here exactly as they do to the ch. 142 program *(verify
both)*. Run one records program, two subjects; the enforcement leverage is
shared.

### TIER 3 — SUPPORT THE EXISTING CASE (no new risk to you) · **Start now**

This is the highest-value rung on the ALPR track and it is available immediately.

- **Offer the statewide dataset to KJI.** Same approach as `11 § 1.3`: not a
  request for help, an offer of a product. *Grimmett* is a Wichita case; the
  City will argue Wichita's program is bounded and controlled. A verified
  statewide sharing map is the direct rebuttal, and no one else is building one.
  Contacts are in the petition signature block.
- **Watch the § 20 ruling** (§ 2.5 above) and get the order the day it issues.
- **Find ALPR-derived criminal cases.** Any Kansas prosecution where the stop or
  the identification traces to an ALPR alert is a vehicle for a suppression
  motion, and a suppression motion is a merits ruling paid for by someone else's
  case. Offer the research to defense counsel free.
- **Watch *State v. Rector*** (WY-2026-CR-000309) — an active prosecution that
  will generate testimony about how the audit logs actually work.

### TIER 4 — INDEPENDENT AFFIRMATIVE LITIGATION · **Probably never, and that is fine**

The conditions from `11` (named plaintiff, counsel of record, dataset,
organizational backing) all apply, plus one more specific to this track:
**a reason why *Grimmett* is not already the vehicle.** If a second Kansas ALPR
case is worth filing, the reason will be a different defendant — a county
sheriff, KHP, or a city that shares with federal agencies — and it will be filed
by an organization, not by you.

### TIER 5 — INTERFERING WITH CAMERAS

**Do not.** See § 0.2.

---

## PART VI — THE POLITICAL AND COUNTY LAYER

The ALPR track has a lever the ch. 142 track does not, and it is the reason this
audit is worth running on a short clock:

**These are contracts, and contracts expire.**

Every Flock deployment is a subscription with a renewal date and a line in a
municipal budget. A city council that will not debate surveillance policy in the
abstract has to take a recorded vote to spend the money. That is the entire
mechanism behind 50+ cancellations across 23 states since January, and it is
already working in Kansas: **Gardner switched its cameras off on August 20,
2026**; Junction City slowed its expansion.

**The immediate item:** Wichita's Flock contract term is reported to end
**September 30, 2026** — under thirty days out. *Verify this against the contract
documents in the record before acting on it, and verify the renewal mechanism:
does it auto-renew absent action, or does it require an affirmative Council
vote?* Those are different opportunities and only one of them has a deadline.
Either way, a renewal decision made while *Grimmett* is pending is a public
meeting where the Council must say, on the record, what it thinks of a program a
court has been asked to enjoin.

**The standing county/city ask** — no civil-liberties framing required:

1. What is the annual cost, and what is the renewal date?
2. How many cameras, and how many are privately owned but connected to our feed?
3. Who else can query our data? Produce the list.
4. What is our configured retention, and why isn't it the vendor's recommended
   seven days?
5. How many searches were run last quarter, by whom, and for what stated reason?
6. Who audits that, and when did they last do it?
7. How many stops originated from an ALPR alert, and how many were wrong?

Question 3 is the one that ends the meeting. Almost no Kansas agency can answer
it, and the inability to answer is the finding.

---

## PART VII — CANDID ASSESSMENT

**Most likely outcome.** *Grimmett* survives in part or is dismissed on standing,
appeals, and takes two to four years. The § 20 claim is dismissed. Meanwhile the
contract-cancellation wave does more practical work than the litigation:
individual Kansas cities switch cameras off, retention defaults drop to seven
days, and the 2027 or 2028 Legislature passes a modest bill — which, if nobody
is watching the fine print, quietly exempts ALPR data from KORA and closes the
window this project depends on.

**Where the real value lands.** Same as `11`, more so. Nobody has the statewide
Kansas ALPR deployment and sharing map. KJI has Wichita and needs the rest.
Journalists have crowdsourced dots on a map and need contracts. Legislators
drafting a 2027 bill have anecdotes and need counts. The dataset is the asset,
it serves three constituencies at once, and it is a paid product under
`11 § 2.4` on day one.

**What is different from the ch. 142 track, and better.** The coalition is
already bipartisan and already winning votes in city councils. The vendor has
publicly conceded the retention argument. The Supreme Court moved in your
direction ten weeks ago. There is competent counsel already litigating. The
facts are documentary rather than testimonial. Not one of those things is true
of ch. 142.

**What is different, and worse.** The doctrine is genuinely unsettled and
*Knotts* is real. Lockstep § 15 interpretation caps how much a Kansas court can
do. Police support is stronger and better organized than on ch. 142, because
ALPR clears cases and agencies can point to specific recoveries — engage that
honestly, per `11 § 1.6`, or lose the room.

**The biggest risk on this track is not the State. It is scope.** Two audits, one
person. The failure mode is a half-built ch. 142 dataset and a half-built ALPR
dataset and neither one citable. **Run one records program covering both
subjects, on one calendar, in one tracker.** The agencies overlap almost
completely — the same sheriff answers both requests — and the marginal cost of
adding ALPR items to a ch. 142 request packet is one page.

**The narrowest, truest statement of this track:** *Grimmett* has Wichita. Take
the other 104 counties, get it done before the Legislature exempts the records,
and hand it to the people already in court.

---

## VERIFICATION REGISTER

Nothing below has been Shepardized. Confirm before use in any filing, testimony,
or published report.

**Primary source obtained and read in full:**
- *Grimmett v. City of Wichita*, No. SG-2026-CV-002760 (Sedgwick Cnty. Dist. Ct.,
  filed July 29, 2026), Petition for Declaratory Judgment, 42 pp., Exs. 1–17.
  Retrieved from kansasjusticeinstitute.org. **Paragraph cites in this document
  are to that petition and are accurate to it — but the petition is a party's
  pleading, not a finding of fact.** Its factual allegations must be independently
  verified before this project repeats them as established.

**Requires verification before use:**

| Item | Why |
| --- | --- |
| *Chatrie v. United States*, No. 25-112, 609 U.S. ___ (June 29, 2026) — holding, vote, author | Post-dates most secondary sources; read the slip opinion |
| *Kansas v. Glover*, 589 U.S. 376 (2020) — exact holding and its limits | The § 2.4 argument depends on stating it precisely |
| *Cleverly*, *Thompson*, *Talkington* — the lockstep § 15 rule | Taken from the petition's characterization; read the cases |
| *McCarthy*, *Leaders of a Beautiful Struggle*, *Knotts*, *Carpenter*, *Jones*, *Jardines*, *Kyllo* | Standard cites, unverified here |
| K.S.A. 45-218(d), 45-222, 45-221(a)(10) | Current text and standards |
| KLRD ALPR memo — publication date; the "no Kansas statute" statement; the WPD/KHP Houston HIDTA six-month retention detail | The HIDTA detail may be years out of date |
| Kansas SB 305 (2021) — that it would have exempted ALPR data from KORA | This drives the whole timing argument in Part III. **Verify first.** |
| Sen. Kenny Titus 2026 amendment — bill number, vehicle, disposition | Reported secondhand |
| Wichita Flock contract end date of September 30, 2026, and the renewal mechanism | From an aggregator. **Most time-sensitive item in this document** |
| The 12-state ALPR statute list | Changes every session |
| Camera counts for Overland Park (~77), Olathe (~69), KC metro (~1,500) | Crowdsourced; lead source only, never cite as a count |
| Gardner shutoff (Aug. 20, 2026); Junction City slowdown; Topeka non-Flock LPR; Lenexa Axon/Genetec/Leonardo | Single-source local reporting |
| Flock's August 14, 2026 policy changes; 120,000 cameras; ~40% of U.S. departments; 50+ cancellations in 23 states | Vendor announcement plus trade reporting |
| *State v. Heiar*, No. 2022-CR-001620 (Sedgwick); *State v. Rector*, No. WY-2026-CR-000309 (Wyandotte); Nygaard certification revocation | Case numbers from the petition; pull the dockets |

**Sources consulted for this document:** the *Grimmett* petition (Kansas Justice
Institute); Kansas Reflector, July 31, 2026; Reason, July 31, 2026; KCUR,
Aug. 1, 2026; the Sentinel; Kansas Press Association, Aug. 14, 2026; Johnson
County Post, Aug. 20 and June 30, 2026; Axios Kansas City, Aug. 25, 2026; KSNT;
KSN; Kansas Legislative Research Department, *Automated License Plate Readers*;
DeFlock and derivative crowdsourced maps.
