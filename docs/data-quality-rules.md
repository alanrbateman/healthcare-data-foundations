# Data Quality and Review Rules

## Purpose

Prepare consistent physician information for downstream applications while preserving source records and making uncertainty visible.

These rules apply only to this synthetic demonstration.

## 1. Standardize field names

Map equivalent fields into a shared structure:

| Credentialing source | Scheduling source | Shared field |
|---|---|---|
| provider_id | clinician_id | provider_id |
| first_name | given_name | first_name |
| last_name | family_name | last_name |
| specialty | specialty_name | specialty |
| practice_location | site | location |

Keep source-specific fields such as credentialing status and acceptance of new patients.

## 2. Normalize specialty labels

Use an explicit mapping:

- Cardio → Cardiology
- Internal Med → Internal Medicine
- Orthopedics → Orthopedic Surgery
- Family Practice → Family Medicine

Preserve the original labels alongside standardized values.

## 3. Match records using identifiers

Use a populated, matching provider identifier to link records across sources.

Do not automatically match records by name alone. Missing identifiers require review, even when names appear identical.

## 4. Handle duplicate records

When records within one source have the same provider identifier and identical business fields, consolidate them into one representation while retaining every source record ID.

If their business fields differ, flag the discrepancy instead of silently choosing one.

## 5. Surface location discrepancies

Different locations may reflect an error or legitimate work at multiple sites.

Retain both values and flag them for review. Do not assume either source is authoritative.

## 6. Flag status inconsistencies

A pending credentialing status combined with acceptance of new patients requires review.

This is a demonstration rule, not a clinical or credentialing determination.

## 7. Preserve traceability

Each consolidated record must retain its source system and source record IDs.

Every review flag must identify the affected records and explain the issue.

## 8. Separate curated output from unresolved records

Records without unresolved issues may enter the demonstration's ready output.

Records with missing identifiers, conflicting values or status inconsistencies remain in a review output.

Passing these checks does not establish real-world clinical accuracy.
