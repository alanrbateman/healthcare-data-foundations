# Healthcare Data Foundations

## Turned Fragmented Physician Data Into Traceable Information

A working demonstration of business requirements, explicit data-quality rules and traceable results. Developed by Alan R. Bateman with AI assistance.

### Context and Business Challenge

Healthcare organizations can connect systems and still struggle to use the data they exchange. Physician records from credentialing and scheduling can contain inconsistent specialties, duplicates and conflicting information. This demonstration makes those concerns visible before data reaches a directory or another application.

### Actions Taken

- I framed the demonstration around physician-data problems informed by my hospital operations, implementation and enterprise healthcare software experience.
- I used AI to help draft the Python code and documentation, configured the repository, ran the workflow and confirmed the summary against expected results.
- I used explicit rules to normalize specialty labels while retaining original values and source identifiers.
- I consolidated an identical duplicate without losing either source record ID and flagged conflicting locations or credentialing concerns for review.
- I kept records with missing provider identifiers separate rather than assume that matching names represented the same physician.

### Results

| Measure | Verified result |
|---|---:|
| Fictional source records processed | 15 |
| Consolidated output records | 8 |
| Outputs passing demonstration checks | 4 |
| Outputs requiring human review | 4 |
| Identical duplicate records consolidated | 1 |
| Input records with provenance retained | 15 of 15 (100%) |

The two records without provider identifiers remain separate. Four records passing these checks does not establish clinical accuracy or production readiness. Human review and correction of flagged records are outside this version.

### Leadership and Strategic Impact

This work demonstrates how I translate a business need into explicit data requirements and evaluate whether the output is usable. It makes uncertainty visible rather than hiding discrepancies behind a clean-looking result. The same reasoning applies when business and technical teams need to agree on definitions, ownership and downstream requirements.

### Transferable Skills

Business requirements • Data quality • Source traceability • Practical AI use • Outcome verification • Communication across business and technical teams

### Explore the Demonstration

- [Credentialing input](data/credentialing.csv)
- [Scheduling input](data/scheduling.csv)
- [Data quality and review rules](docs/data-quality-rules.md)
- [Curation script](scripts/curate.py)
- [Curated records](data/ready_records.json)
- [Records requiring review](data/review_records.json)
- [Run summary](data/summary.json)

The linked JSON files are saved results from the verified run.

### Run It

In GitHub, open **Actions → Run Healthcare Data Demo → Run workflow**.

The workflow runs the Python script, displays a summary and provides downloadable results. Each run generates files in `outputs/`; it does not automatically update the saved examples linked above.

Alternatively, with Python 3.13 installed, run from the repository root:

```sh
python scripts/curate.py
```

No third-party Python packages are required.

### Scope and Development Approach

All records are fictional. This is a small portfolio demonstration, not a production interoperability platform. It uses no patient information, employer data or proprietary product code.

AI assisted development. Processing rules are explicit and deterministic; no AI model is called during execution. The current scope covers field mapping, specialty normalization, identifier-based grouping, duplicate handling, review flags and source traceability.
