# 13 — DATA PRODUCTS AND PUBLICATION

**Turning the enforcement record into a licensable, citable product**

Drafted September 5, 2026 · Operational companion to `11 § 2.4`

> **Not legal advice.** Publication decisions in Part III touch defamation,
> privacy, and records-law questions that are outside what this file can settle.
> Confirm with counsel before the first paid distribution.

---

## PART 0 — WHY THIS EXISTS BEFORE THE DATA DOES

`11 § 2.4` names the products: data licensing first, then SaaS, consulting,
grants. It does not say how a tracker row becomes a number someone will pay for
and a court will accept. That is this file.

I argued earlier that a product spec should wait until the first county tranche
came back — that the report sells on the data, and there isn't any yet. That was
wrong on timing, for one reason:

**Schema decisions cannot be made retroactively.** If the published report needs
a field, and that field was not captured when the response arrived, you cannot
add it later without re-reading every response — and for some fields, without
re-asking. Saturation is 105 counties plus municipal agencies. Getting the shape
wrong and discovering it at the end costs the year the whole plan is trying to
save.

So: lock the output shape before Tier 0 scales past the pilot. Part VI lists the
specific changes.

**What is still true:** nothing here is sellable yet. No request has been sent.
Three of four trackers are empty headers. This file describes the product the
machine is being built to produce, not a product that exists.

---

## PART I — WHAT IS ACTUALLY SELLABLE

Ranked by speed to first dollar, which is also roughly inverse to effort.

### 1. The Kansas Enforcement Report — the flagship

A periodic report: §§ 5 and 1 activity by county, ALPR deployment and sharing by
agency, and agency records-compliance scoring. Quarterly once there is a
baseline; the first edition is the baseline.

**What makes it worth money is not the counts. It is the denominator.**

"Fourteen § 5 charges statewide" is a number anyone can guess at and nobody can
cite. "Fourteen § 5 charges reported by the 31 of 105 counties that produced
responsive records, against 43 counties that responded at all and 62 that did
not, with the request text, dates, and per-agency response scoring in Appendix
B" is a number a journalist can print, a legislator can read into a committee
record, and a litigator can attach to a brief.

Nobody else can produce the second sentence. That is the entire moat, and it is
made of methodology, not effort.

### 2. Agency compliance scoring — the sleeper

The KORA response data is a product in its own right, independent of the
underlying subject matter. Which Kansas agencies answer records requests, how
fast, at what cost, claiming which exemptions.

It sells to a wider audience than the ch. 142 material — every newsroom, every
firm, every advocacy group in the state files records requests — and it is
subject-neutral, so it survives ch. 142 entirely. It is also the cheapest thing
to produce, because it is a byproduct of the tracker with no additional
collection.

**This is probably the most underrated asset in the project.** It is the piece
most likely to still be earning in 2030.

### 3. The ALPR deployment and sharing map

Per-agency: vendor, verified camera count with basis, configured retention,
sharing partners, contract term and renewal date, annual cost.

Buyers: KJI and any counsel litigating ALPR (they have Wichita and need the
rest), journalists, city councils facing a renewal vote, and national
organizations tracking the vendor. The renewal-date column alone is a
subscription trigger — a council with a decision 60 days out is a buyer with a
deadline.

### 4. Custom extracts and consulting

A single county, a single agency, a single question, on request. Higher margin,
lower volume, and it doubles as the discovery channel for what the next report
edition should contain.

### 5. The tooling

`11 § 2.4`'s platform concept. Real, but it is a software business with software
economics and a long build. It is not the first dollar and should not be treated
as one. Ship reports; let the reports tell you what the tool must do.

---

## PART II — THE PIPELINE

Three stages. The middle one does not exist yet and is the actual work.

```
COLLECTION           trackers/*.csv
                     one row per request, incident, probe, agency
                     raw, internal, includes material that will never publish
                          |
                          |  derive: aggregate, suppress, compute denominators
                          v
DERIVED              reports/<edition>/tables/*.csv
                     one row per published figure, with its denominator
                     and a pointer back to the source rows
                          |
                          |  render: prose, methodology, appendices
                          v
PUBLISHED            reports/<edition>/kansas-enforcement-report.pdf
                     licensed artifact + public methodology
```

**The rule that makes it defensible:** every figure in the published report
traces to derived rows, and every derived row traces to collection rows, and
every collection row carries `source_url` and `doc_sha256`. A subscriber who
challenges a number gets the chain, not an assurance.

**Reproducibility.** The derive step must be a script, not hand-editing. When an
agency produces late — and they will, constantly — the edition regenerates
rather than being patched. Hand-patched numbers are how a citable report becomes
an uncitable one.

**Corrections.** Every edition is versioned and immutable once distributed.
Corrections ship as a new version with a changelog naming what changed and why.
The first time you silently fix a number, every prior number becomes suspect.

---

## PART III — WHAT PUBLISHES AND WHAT DOES NOT

This is the section that protects the project, and it needs deciding before
collection, because it determines what gets captured and how.

The trackers already contain material that must not be republished as-is.
`enforcement-incident-tracker.csv` holds `subject_role`, `case_number`,
`subject_counsel`, and free-text `notes` that currently name a private
individual who recorded ICE activity and an ICE officer, both sourced from
published reporting. Holding that for research is one thing. Selling it in a
commercial product is a different act with different exposure.

### The tiers

| Tier | Content | Where it goes |
| --- | --- | --- |
| **Public** | Aggregate counts, denominators, agency-level compliance scores, ALPR deployment and contract facts, methodology, request text | The report, freely quotable |
| **Licensed** | Per-incident rows with individuals removed, per-agency detail, full response timelines, exemption text | Paid tiers only, under licence terms |
| **Internal** | Names of private individuals, `subject_counsel` and `counsel_contact`, unredacted agency productions, anything `verified` is not `yes` | Never distributed. Research and litigation-support use only |

### Standing rules

1. **Agencies and officials acting officially are named. Private individuals are
   not.** A sheriff's office, a police chief, a named custodian who signed a
   denial — all publishable. A person who was stopped, warned, charged, or
   recorded something is not, absent their written consent or a strong reason
   tied to an already-public court record.
2. **Officers named in misconduct findings follow the source.** The three Kansas
   ALPR abuse cases in `12 § 1.4` are named because they are convictions,
   charges, and certification revocations already in public records — cite those
   records, not the reporting about them, and say which.
3. **`verified` gates publication.** Nothing marked `partial` or blank appears as
   a fact. It may appear as an explicitly labelled open question, which is often
   more valuable than a soft number.
4. **A pleading is a pleading.** *Grimmett* allegations are published as
   allegations, attributed to the petition by paragraph. This is already the
   repo's rule; it does not relax because someone is paying.
5. **Redaction is one-way.** Never publish a partially redacted document where
   the unredacted version is also distributed at another tier. Produce separate
   artifacts.

### Before the first paid distribution

Have counsel look at: republication of criminal case details, the ICE-observer
incident specifically, and whether the licence terms adequately disclaim
downstream use. This is a small, bounded consult and it is the natural second
conversation with whichever Kansas lawyer takes the KORA work under `11 § 2.3`.

---

## PART IV — THE METHODOLOGY BLOCK

Every edition carries this. It is not front matter; it is the product.

1. **Universe.** Which agencies were asked. Named, in a table, all of them.
2. **Instrument.** The exact request text, reproduced. Reproduce it even though
   it is long — a reader who cannot see the question cannot judge the answer.
3. **Dates.** Sent, statutory due, first response, production complete.
4. **Response accounting.** Responded / did not respond / produced records /
   denied in whole / denied in part / demanded a fee not paid. These must sum to
   the universe.
5. **Exemptions.** Which were claimed, by whom, how often, with statutory cites.
6. **Known gaps.** What is missing and why. An agency that never answered is a
   data point, not a hole.
7. **Change log.** What moved since the last edition, and what it changed.
8. **Verification standard.** State that `verified` means checked against a
   primary source document, and that crowdsourced camera maps are a lead source
   and never a published count.

Point 6 is the one most reports skip and the one that makes this one credible.
The non-responders are a finding.

---

## PART V — LICENSING AND PRICING POSTURE

**Judgment, not market data.** No comparable has been tested. Treat as a
starting position to be revised after the first ten conversations.

| Tier | Who | What they get | Posture |
| --- | --- | --- | --- |
| **Public** | Anyone | Headline figures, methodology, the fact that the dataset exists | Free. This is marketing, and it is what makes the report citable |
| **Newsroom** | Per-outlet | Full report, county tables, quotable with attribution | Priced to be an easy yes for a small outlet — the KPA/KAB channel matters more as reach than as revenue |
| **Institutional** | Firms, advocacy orgs, policy shops | Full report plus licensed-tier data, custom extracts on request | The revenue tier |
| **Litigation support** | Counsel of record | Everything licensable, plus declarations on collection methodology and chain of custody | Highest. This is expert-adjacent work and should be priced as such |

**Three structural notes:**

- **Never paywall the methodology.** The public tier must include it. Free
  methodology is what makes the paid numbers trustworthy, and it is what gets
  the report cited by people who did not buy it — which is the entire top of the
  funnel.
- **Give it to the coalition free.** `11 § 1.3` says lead with the artifact and
  ask for nothing. That is not in tension with selling it. ACLU of Kansas, KPA,
  KAB, and KJI get it free; that is customer development and coalition-building
  in one move, and those organizations are the reference customers everyone else
  checks with.
- **The dataset is the asset; the report is a view of it.** Licence access, not
  ownership. Do not sell the underlying tables outright to anyone at any price.

**On the Four-State Interior Finishes Cost Report:** that precedent is the
reason to believe this works — same operator, same structure, revenue already
proven once. Whatever pricing and packaging worked there is better evidence than
anything in this table. Use it.

---

## PART VI — SCHEMA CHANGES TO MAKE BEFORE SATURATION

Concrete, small, and each one is expensive to add later.

**1. Add `publication_tier` to every tracker.** Values: `public`, `licensed`,
`internal`. Set it at row creation, not at publication time. Without this, every
report edition requires re-adjudicating every row by hand.

**2. Add `track` to `alpr-deployment-tracker.csv`.** The other three trackers
have it. Consistency matters when the derive step is a script.

**3. Add `contacted` to the KORA tracker** — or a universe table. Right now a
row exists only once a request is sent. The denominator needs the agencies that
were *in scope*, including any that were skipped and why. Without this the
response-rate figure cannot be computed honestly.

**4. Add `response_accounting` as a controlled vocabulary** on the KORA tracker,
with exactly the Part IV point-4 values. `response_type` is currently free text;
free text does not aggregate.

**5. Add `edition_first_published` to every tracker.** Which report edition first
carried this row. Makes the change log generate itself.

**6. Add `redaction_state`** to the incident tracker: `none`, `agency_redacted`,
`self_redacted`. Publication decisions depend on it.

None of these changes the request templates. All of them change what the
responses get scored into, which is why they land before the tranche, not after.

---

## PART VII — CANDID ASSESSMENT

**What this is worth.** The enforcement report is a niche product in a
one-state market with maybe a few dozen genuine institutional buyers. It is not
a business on its own. It is a revenue line that pays for the records program,
establishes the project as the citable source, and — most importantly —
functions as the artifact that gets meetings with organizations that have
litigation budgets. Judged only on revenue it will look disappointing. Judged on
what it buys, it is the highest-leverage thing here.

**The compliance-scoring product is the one that could outgrow the project.** It
is subject-neutral, the audience is every records requester in Kansas, and the
same method ports to any state with an open-records act. If something here
becomes a real business, it is that, not the ch. 142 material.

**The biggest risk is publishing too early.** A first edition with a thin
denominator — twelve counties, four responses — is worse than no edition,
because it establishes the project as a source of weak numbers and you only get
one first impression with a newsroom. Hold the first edition until the response
base can carry the claims. `11 Part IV` puts it at weeks 7–12; that was written
before the pilot went out and should be treated as an ambition, not a deadline.

**The second-biggest risk is the product eating the project.** Reports have
deadlines and customers; litigation support does not, until suddenly it does.
`11 Part V` already names scope as the main threat to a one-person operation.
Adding a publication schedule adds a third demand alongside two audit tracks.
If something has to give, it is the report cadence — quarterly can become
semi-annual without damaging the asset. The dataset is what matters.

**Narrowest statement:** the denominator is the product, the methodology is the
moat, the compliance data is the sleeper, and none of it is worth anything until
the responses come back.
