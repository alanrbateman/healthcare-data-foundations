# Healthcare Data Foundations

### Turning fragmented healthcare data into consistent, traceable information

Healthcare organizations can connect systems and still struggle to use the data they exchange. Different definitions, duplicate records and conflicting information can undermine patient access, operational decisions and confidence in the applications consuming that data.

This working demonstration brings together fictional physician records from credentialing and scheduling systems. It standardizes information, preserves its source and separates records ready for downstream use from records requiring human review.

## Why this matters

A physician directory needs more than names and contact details. Its usefulness depends on reliable specialties, locations and availability, and a clear process for resolving discrepancies.

This project demonstrates how explicit business rules can make those discrepancies visible before information reaches another application.

## Verified demonstration results

The workflow ran successfully with the following results:

| Measure | Result |
|---|---:|
| Source records processed | 15 |
| Consolidated records passing demonstration checks | 4 |
| Records requiring review | 4 |
| Identical duplicate records consolidated | 1 |

The eight output records retain provenance for all 15 input records. The two records without provider identifiers remain separate.

### Decisions illustrated

- **Standardize terminology:** Convert specialty abbreviations into consistent labels while retaining the original values.
- **Preserve evidence:** Consolidate an identical duplicate without losing either source record ID.
- **Expose uncertainty:** Flag different locations rather than assume one source is correct.
- **Identify business-rule concerns:** Flag pending credentials alongside acceptance of new patients.
- **Avoid unsupported matching:** Keep records with missing identifiers separate, even when their names match.

Four records passing these checks does not establish clinical accuracy or production readiness.

## Explore the demonstration

- [Credentialing input](data/credentialing.csv)
- [Scheduling input](data/scheduling.csv)
- [Data quality and review rules](docs/data-quality-rules.md)
- [Curation script](scripts/curate.py)
- [Curated records](data/ready_records.json)
- [Records requiring review](data/review_records.json)
- [Run summary](data/summary.json)

The linked JSON files are saved results from the verified run.

## My perspective and development approach

My background spans hospital operations, technology implementation, consulting and enterprise healthcare software sales, including physician data and provider directory solutions.

I bring that experience to framing business requirements, evaluating stakeholder needs and assessing whether technology produces useful outcomes.

This demonstration was developed with AI assistance. AI helped draft the code and documentation; I configured the repository, ran the workflow and confirmed the summary against the expected results. The processing rules are explicit and deterministic. No AI model is called during execution.

## Run it

In GitHub, open **Actions → Run Healthcare Data Demo → Run workflow**.

The workflow runs the Python script, displays a summary and provides downloadable results. Each run generates files in `outputs/`; it does not automatically update the saved examples linked above.

Alternatively, with Python 3.13 installed, run from the repository root:

`python scripts/curate.py`

No third-party Python packages are required.

## Scope

All records are fictional. This is a small portfolio demonstration, not a production interoperability platform. It uses no patient information, employer data or proprietary product code.

The current scope covers field mapping, specialty normalization, identifier-based grouping, duplicate handling, review flags and source traceability. Human review and correction of flagged records are outside this version.
