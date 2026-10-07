# Copyright, Ownership, and Licensing

**© 2026 Matthew Preston Goodman. All rights reserved.**

This repository and its contents are **proprietary and confidential** except
where this document says otherwise. No license is granted by the act of
receiving, reading, cloning, or being given access to this repository.

---

## 1. WHAT IS OWNED HERE

### 1.1 Protected by copyright

Copyright protects **original expression** — the way something is written,
selected, arranged, or coded. In this repository that means:

| Material | Status |
| --- | --- |
| Every `.md` document — the strategic plan, the audits, the protocols, the operations manual | **Owned. All rights reserved** |
| The KORA request templates and the letter templates | **Owned. All rights reserved** |
| The scripts in `scripts/` | **Owned. All rights reserved** |
| The tracker **schemas** — the choice of columns, their definitions, the scoring rubrics | **Owned**, as original selection and arrangement |
| Published reports, instruments, and training material derived from any of the above | **Owned. All rights reserved** |

### 1.2 NOT protected by copyright — and this matters commercially

**Facts are not copyrightable.** *Feist Publications, Inc. v. Rural Telephone
Service Co.*, 499 U.S. 340 (1991), holds that facts and data, however much
effort went into collecting them, are not protected. A compilation of facts
receives only "thin" protection, and only for the originality of its selection
and arrangement — never for the underlying facts themselves.
*(Verify against current authority before relying on this in a contract
dispute.)*

Applied here:

- **A camera count is a fact.** So is a response time, a fee charged, an
  exemption cited, a docket entry, a date.
- **Records obtained from a government agency** under KORA, the Missouri
  Sunshine Law, or any equivalent are generally public records. Obtaining a copy
  does not create ownership of it. Judicial opinions, statutes, and other
  government edicts are in the public domain.
- A third party who independently gathers the same facts owes nothing.

**So the commercial protection is not copyright in the numbers.** It is:

1. **Contract** — license terms agreed before access, which bind the
   counterparty whether or not the data is copyrightable.
2. **The instrument** — the procedure, the templates, and the code, which *are*
   copyrightable expression.
3. **Curation, currency, and chain of custody** — a sourced, hashed, verified,
   continuously updated dataset is worth paying for even when a competitor is
   legally free to rebuild it, because rebuilding it costs more than the
   license.
4. **Being first and being citable.**

Anyone who tells you the copyright notice alone protects the dataset is wrong,
and building a business on that assumption is how the business fails.

### 1.3 Third-party and public material

This repository stores and references material it does not own:

- **Government records** obtained under open-records law. Reproduced as public
  records; no ownership claimed.
- **Court filings**, including the *Grimmett* petition. Public records of a
  public proceeding; no ownership claimed. A pleading states one party's
  allegations and is not a finding.
- **News reporting** cited as a secondary source. Quoted briefly with
  attribution; copyright remains with the publisher. **Do not reproduce a
  substantial portion of any article in a distributed product.**
- **Crowdsourced data** such as DeFlock. Used as a lead source only, under
  whatever terms its publisher sets. Never published as a count.

Entries in `evidence/manifest.csv` record provenance for exactly this reason.
**Before any paid distribution, re-check the provenance of every included
item.** A single third-party asset distributed without the right to do so can
contaminate an entire product.

---

## 2. PROPRIETARY AND CONFIDENTIAL

The following are **proprietary and not for distribution** in any form:

- Everything marked `Internal` in the publication tiers of
  `13-data-products-and-publication.md` § II.
- Every row in `trackers/harvest-register.csv` marked `quarantined = yes`, and
  every fact specific to any pending legal matter, **until the matter
  terminates and the quarantine is released under
  `14-intelligence-harvest-protocol.md` § 4**.
- Names of private individuals, counsel contacts, and unredacted agency
  productions.
- Any draft, working note, or analysis not yet marked `verified = yes`.

**Access to this repository does not authorize redistribution of anything.**

### 2.1 The one deliberate exception: published methodology

`13-data-products-and-publication.md` commits to a **licensed artifact with a
public methodology**. That is intentional and it is not a mistake in this
notice. An audit whose method is secret is not an audit — nobody can check it,
so nobody should believe it.

**Publishing the method does not surrender the dataset, the reports, the
templates, or the code.** Methodology is published so the findings are credible;
everything else is licensed.

---

## 3. HOW TO OBTAIN A LICENSE

No license exists until it is in writing and signed. Direct inquiries to the
copyright holder.

### 3.1 Contemplated license classes

These are the intended shapes, not offers, and none is in force until executed:

| Class | Who | What it conveys |
| --- | --- | --- |
| **Public** | Anyone | The published methodology, the summary findings, and anything expressly released. Attribution required. No redistribution of underlying rows |
| **Journalistic / non-commercial** | Reporters, researchers, non-profits | Access to specified derived data for a named project, with attribution and no redistribution |
| **Commercial** | Firms, vendors, consultancies | Negotiated per engagement. Term-limited, non-exclusive, non-transferable, no sublicensing |
| **Litigation support** | Counsel of record in a specific matter | Use confined to that matter, under the terms of the engagement |

### 3.2 Terms that belong in every license

Because copyright will not carry the weight (§ 1.2), the contract has to:

1. Define the licensed material by **edition and version**, not by description.
2. Prohibit **redistribution, resale, sublicensing, and bulk extraction**.
3. Prohibit **training machine-learning models** on the licensed material
   without separate written permission.
4. Require **attribution** in the agreed form.
5. State that the data is provided **as is**, with the verification status
   disclosed, and disclaim warranties (§ 4).
6. Set a **term**, a **renewal**, and what happens to the data at termination.
7. Name the **governing law and venue**.

**Have a lawyer draft the actual agreement.** The list above is what to brief
them with, not a substitute for them.

---

## 4. NO WARRANTY

This material is provided **as is**, without warranty of any kind, express or
implied, including any warranty of accuracy, completeness, currency, fitness
for a particular purpose, or non-infringement. Verification status is disclosed
on the face of each document and in the `verified` column of each tracker. See
`DISCLAIMER.md`.

---

## 5. NOTICE BLOCK FOR DISTRIBUTED PRODUCTS

Place this on the first page of every report, dataset, instrument, or deck that
leaves the project:

```
© 2026 Matthew Preston Goodman. All rights reserved.
Edition <N>, released <DATE>. Licensed material — not for redistribution.

Not legal advice. The author is not an attorney. No attorney-client
relationship is created by this document.

Government records reproduced herein are public records; no ownership is
claimed in them. Facts are not subject to copyright. Rights are asserted in
the selection, arrangement, analysis, and expression of this document and in
the methodology and instruments used to produce it.

Provided as is, without warranty. Verification status for every figure is
stated in the methodology section and traceable to the source manifest.
```

Keep it on one page and keep it legible. A notice nobody can read protects
nothing.
