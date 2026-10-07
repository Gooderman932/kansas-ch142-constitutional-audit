# 14 — INTELLIGENCE HARVEST PROTOCOL

**How working sessions become audit findings, and audit findings become
data products.**

*Companion to `13-data-products-and-publication.md`, which covers what gets
sold and to whom. This document covers where the raw material comes from and
how it is captured before it is lost.*

---

## 0. THE PROBLEM THIS SOLVES

Most of the value produced in a long working session evaporates. A discrepancy
gets noticed, discussed, used to solve the immediate problem, and then buried
under four hundred messages. Six months later nobody can find it, nobody
remembers which version was right, and the finding — which was generalizable,
which was the actual asset — is gone.

**The immediate legal problem consumes the finding and discards the method.**

The method is the thing worth money. A single officer's inaccurate affidavit is
a defense issue in one case. **A reproducible procedure for testing any
affidavit against the issuing court's own docket is an instrument** — it works
in every county, it produces a dataset, and the dataset is the product.

This protocol is the conversion mechanism.

### 0.1 Conduct rules — these bind the whole protocol

1. **Nothing is harvested from a live criminal matter while it is pending.**
   Facts specific to an open case are quarantined under § 4. Only the
   *de-identified method* leaves quarantine before the case closes.
2. **No privileged communication is ever harvested.** Anything said to or by
   counsel is out of scope permanently, not temporarily.
3. **No third party's personal information is published.** Names that appear in
   court records incidentally — co-parties, witnesses, people who share a docket
   — are replaced with role labels before anything leaves quarantine.
4. **No encounter is manufactured to generate a finding.** This restates
   `11 § 0.1` and it governs here with full force. The audit documents what
   agencies do; it does not provoke it.
5. **Public officials acting in their official capacity, named in public court
   filings, are not anonymized** — that is the record, and naming it is the
   point. The distinction is office versus private person.

---

## 1. THE DETECTOR — WHAT COUNTS AS A FINDING

Run this against every working session. Six trigger patterns. If a passage
matches one, it is a candidate; log it.

| # | Trigger | What it looks like | Why it is worth money |
| --- | --- | --- | --- |
| **T1** | **Assertion–record divergence** | An official document states a fact; the issuing body's own records say something else | Measurable across cases. Produces an error rate. Error rates are citable |
| **T2** | **Missing statutory element** | A charging document, affidavit, or order omits an element the statute requires | Produces a defect rate per statute. Directly actionable for reform and for defense bars |
| **T3** | **Records-access friction** | A request is refused, delayed past the statutory window, over-charged, or answered with the wrong exemption | This is the core KORA/Sunshine dataset. Already monetized in `13 § 2` |
| **T4** | **Cost imposed by discretion** | A procedural choice an official was free to make differently transfers money out of a private person's pocket | Converts an abstraction into damages. Aggregates into a cost-of-practice figure |
| **T5** | **Identifier or data-integrity anomaly** | One identifier spanning records that should not share one; a record attributed to the wrong person; a system producing a muddled history | Systemic. Affects everyone the system touches, not one defendant |
| **T6** | **Notice failure → adverse outcome** | The record shows the court's own notices returned undelivered during the window in which a party was defaulted for non-appearance | Pure docket arithmetic, scrapeable at scale, and a civil-justice finding with obvious reform value |

### 1.1 The promotion test

A candidate becomes a **finding** only if all three are true:

1. **It is documented by a source you can produce** — a docket entry, a filed
   document, a dated refusal. Not a recollection, not an inference.
2. **It is reproducible in another case** — someone else, in another county,
   running the same query, could find the same kind of thing. If it is unique
   to one person's bad luck, it is a grievance, not a finding.
3. **It survives the honest-explanation test.** Write down the most charitable
   reading. If the charitable reading fully accounts for it, it is not a
   finding. Record it anyway, under `status = explained` — the explained ones
   are what make the unexplained ones credible.

**The third test is the one that protects the whole project.** An audit that
publishes only its hits is advocacy. An audit that publishes its misses is
evidence.

---

## 2. THE CAPTURE — THREE FIELDS, WRITTEN IMMEDIATELY

The moment a trigger fires, before the conversation moves on, write three
things. Nothing else. Thirty seconds.

```
WHAT WAS ASSERTED:  <the official claim, quoted, with its source document>
WHAT THE RECORD SAYS: <the contrary record, with case number and date>
WHY IT GENERALIZES:  <one sentence: what query would find more of these>
```

That third line is the whole asset. Everything before it is one case. The third
line is the instrument.

**Append the entry to `trackers/harvest-register.csv` the same day.** A finding
that lives only in a conversation does not exist.

---

## 3. THE REGISTER — `trackers/harvest-register.csv`

One row per candidate. Twenty-one columns. The schema exists so that findings
can be sorted by maturity and by product line without re-reading any of them.

| Column | Contents |
| --- | --- |
| `finding_id` | `HF-NNN`, sequential, never reused |
| `date_captured` | YYYY-MM-DD |
| `session_ref` | Which working session, by date and subject |
| `trigger` | T1–T6 |
| `jurisdiction` | State and county, or `multi` |
| `agency` | The body whose conduct or records are at issue |
| `assertion` | What was officially asserted |
| `record` | What the record shows |
| `source_doc` | The document or docket entry that proves it |
| `source_obtained` | `certified` · `copy` · `screenshot` · `not yet` |
| `evidence_id` | Link into `evidence/manifest.csv` once the source is hashed |
| `generalizes_how` | **The query that would find more** |
| `charitable_reading` | The most innocent explanation |
| `status` | `candidate` · `finding` · `explained` · `published` |
| `quarantined` | `yes` while any related matter is pending |
| `quarantine_release` | The event that lifts it |
| `product_line` | `dataset` · `instrument` · `report` · `training` · `none` |
| `reform_hook` | The statute or rule a finding would support changing |
| `est_scale` | Rough count of how many cases the query would reach |
| `next_action` | One concrete step |
| `owner` | Who does it |

---

## 4. QUARANTINE — THE WALL

Findings generated while a related matter is pending go in with
`quarantined = yes` and **do not leave the register**. Not a draft, not a
tweet, not a FOIA narrative, not a conversation with a reporter.

**What may cross the wall before release:** the contents of `generalizes_how`
— the query — stripped of every case-specific fact. The instrument is not the
case. A procedure for checking warrant affidavits against dockets reveals
nothing about any particular affidavit, and building the tool during quarantine
is the best use of the waiting period.

**What lifts quarantine:** the matter terminates. Record the date and the
disposition in `quarantine_release`. Then, and only then, the case-specific
facts become available — and at that point they are far more publishable than
they were, because a resolved matter carries an outcome.

**Why this is not caution for its own sake.** Anything published about an open
case is a statement by a party, discoverable, quotable, and usable against the
person who published it. The finding does not expire. The opportunity to ruin
your own case with it does.

---

## 5. CHAIN OF CUSTODY

Findings are only worth what their sources are worth. Use the mechanism the
repository already has — do not invent a second one.

1. **Obtain the source document.** Certified copy where a court record is
   involved; the agency's own written response where a records request is
   involved. A screenshot is a placeholder, not a source.
2. **Hash it on receipt.** `sha256sum`, recorded in `evidence/SHA256SUMS`.
3. **Register it** in `evidence/manifest.csv`: what it is, who produced it,
   the date, how it was obtained, and the request or case it came from.
4. **Store the file** under `evidence/sources/`. The hash in `SHA256SUMS` must
   reproduce against a file that is actually in the tree — a manifest entry
   pointing at a file nobody can open is worse than no entry, because it looks
   like proof and is not.
5. **Link the finding to the evidence** by writing the `evidence_id` into the
   register row.

**Verify the whole chain before any publication:** re-run the hashes, confirm
every referenced file exists, confirm every certified copy is actually
certified. A single broken link discredits an entire dataset, and the people
with the most reason to attack the dataset will check.

---

## 6. THE SWEEP — HOW THIS GETS DONE AND NOT FORGOTTEN

### 6.1 In-session (continuous)

The detector in § 1 runs while the work happens. When a trigger fires, the
three-field capture in § 2 happens immediately, in the session, before moving
on. **A finding noticed and not written down within the hour is lost** — not
because the information disappears but because by the time anyone looks for it
they no longer know it is there to look for.

### 6.2 End of session (ten minutes)

Before closing any working session, answer four questions in writing:

1. **What did we learn that is true beyond this case?**
2. **What official statement did not survive contact with the record?**
3. **What did someone refuse to give us, and under what stated authority?**
4. **What would we query if we wanted a hundred more of these?**

Every answer becomes a register row or is explicitly discarded. Four questions,
every time, no exceptions — the discipline is the entire mechanism.

### 6.3 Monthly (one hour)

- Re-read every row with `status = candidate`. Promote, explain, or kill.
- Re-read every `quarantined = yes` row. Has the release event occurred?
- Re-read every `source_obtained = not yet`. **Sources get harder to obtain
  with time, never easier.** Retention schedules run; staff turn over; systems
  are replaced.
- Count rows by `product_line`. Three or more rows sharing a line and a
  jurisdiction is a dataset with a sample size. Move it to the pipeline in
  `13 § 1`.

### 6.4 Recovery — mining sessions that were never harvested

Past working sessions can be mined retroactively, and should be. Work backward
through the transcript searching for the six trigger patterns. In practice the
highest-yield search terms are the ones that mark a correction or a surprise:

> *"that's not what the record shows" · "actually" · "correction" · "the docket
> says" · "no entry found" · "unsupported" · "they refused" · "no response" ·
> "the statute requires" · "omits" · "the fee was" · "wrong person"*

**Every correction is a candidate finding.** A correction means something
official was stated and turned out to be wrong — which is T1, which is the
single most productive trigger in the set.

---

## 7. FROM FINDING TO PRODUCT

The register feeds four product lines. These route into
`13-data-products-and-publication.md`; nothing here replaces that document.

| Line | What it is | What makes it salable | Maturity gate |
| --- | --- | --- | --- |
| **Dataset** | Structured records of a measured practice across a jurisdiction | Nobody else has counted it | ≥ 30 rows, one jurisdiction, sources hashed |
| **Instrument** | A reusable procedure plus the template that executes it | It saves a professional real hours | Run end-to-end twice, by two people, same result |
| **Report** | A finding written for a decision-maker | A named reform hook and a number attached to it | ≥ 1 dataset behind it, every source certified |
| **Training** | Teaching the instrument to people who need it | Defense bars, journalists, and advocacy orgs pay for method | Instrument mature, written as a procedure, not a story |

### 7.1 The instrument is worth more than the dataset

A dataset answers one question and ages. An instrument generates datasets
indefinitely and improves with use. **When a finding is capable of becoming
either, build the instrument first** and let the first dataset be its
demonstration.

### 7.2 Lead with the artifact

`11 § 1.3`, restated because it is the rule that most often gets ignored under
time pressure: the instrument, the dataset, and the sourced one-page table get
read. A description of what you intend to build does not. **Never approach a
funder, a reporter, or an organization with a plan when you could approach them
with a finished thing.**

---

## 8. STARTING STATE — WHAT HAS ALREADY BEEN HARVESTED

The register ships populated. Working sessions through October 7, 2026 have
been mined under this protocol and produced **nine candidate findings** across
five triggers and two states.

Three deserve note here because they are the ones most likely to become
instruments rather than one-off observations:

**HF-001 — Affidavit–docket divergence.** Six specific factual assertions in a
sworn warrant application, checked against the issuing court's own public
docket. One survived. The procedure is mechanical, the inputs are public, and
it runs in any Missouri county on Case.net. *This is the instrument with the
shortest path to maturity.*

**HF-004 — Identifier collision.** A single Offense Cycle Number appearing
across three matters that should not share one. If that is systemic rather than
a single data-entry artifact, it is a mechanism by which criminal-history
recitals in warrant applications become wrong at scale — and it would explain
HF-001 innocently, which is exactly why it must be tested rather than assumed.

**HF-006 — Notice failure preceding default.** Court-generated notices returned
undeliverable during the same window in which a party was defaulted for failing
to appear. This is pure docket arithmetic, scrapeable, and the civil-justice
finding in the set with the broadest reach.

**All findings arising from the pending Missouri matter are quarantined.** The
instruments built from them are not.

---

## 9. THE ONE-LINE VERSION

**Every time an official statement fails against the record, write down the
query that would find a hundred more of them — then build the tool that runs
it.**
