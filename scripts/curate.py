"""Curate fictional physician records using explicit, reviewable rules."""

import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs"

SPECIALTIES = {
    "Cardio": "Cardiology",
    "Internal Med": "Internal Medicine",
    "Orthopedics": "Orthopedic Surgery",
    "Family Practice": "Family Medicine",
}

SOURCES = {
    "credentialing": {
        "record_id": "source_record_id",
        "provider_id": "provider_id",
        "first_name": "first_name",
        "last_name": "last_name",
        "specialty": "specialty",
        "location": "practice_location",
    },
    "scheduling": {
        "record_id": "record_id",
        "provider_id": "clinician_id",
        "first_name": "given_name",
        "last_name": "family_name",
        "specialty": "specialty_name",
        "location": "site",
    },
}


def load_records():
    records = []
    for source, mapping in SOURCES.items():
        with (ROOT / "data" / f"{source}.csv").open(
            encoding="utf-8-sig", newline=""
        ) as handle:
            reader = csv.DictReader(handle)
            required = set(mapping.values())
            if not required.issubset(reader.fieldnames or []):
                raise ValueError(f"Missing required columns in {source}")

            for raw in reader:
                record = {
                    field: (raw[column] or "").strip()
                    for field, column in mapping.items()
                }
                record["specialty"] = SPECIALTIES.get(
                    record["specialty"], record["specialty"]
                )
                record["source"] = source
                record["original"] = raw
                record["credentialing_status"] = (
                    raw.get("credentialing_status") or ""
                ).strip()
                record["accepting_new_patients"] = (
                    raw.get("accepting_new_patients") or ""
                ).strip()
                records.append(record)
    return records


def curate(records):
    groups = defaultdict(list)
    for index, record in enumerate(records):
        # Missing IDs remain separate; names never trigger an automatic merge.
        key = record["provider_id"] or f"UNRESOLVED-{index + 1}"
        groups[key].append(record)

    ready, review = [], []
    duplicate_count = 0

    for key, members in sorted(groups.items()):
        issues = []
        if not members[0]["provider_id"]:
            issues.append("Missing provider identifier; manual matching required.")

        values = {}
        for field in ("first_name", "last_name", "specialty", "location"):
            values[field] = sorted({r[field] for r in members if r[field]})
            if any(not r[field] for r in members):
                issues.append(f"Missing {field}.")
            if len(values[field]) > 1:
                issues.append(f"Different {field} values; review required.")

        statuses = sorted({
            r["credentialing_status"] for r in members
            if r["credentialing_status"]
        })
        acceptance = sorted({
            r["accepting_new_patients"] for r in members
            if r["accepting_new_patients"]
        })
        if len(statuses) > 1:
            issues.append("Conflicting credentialing statuses.")
        if len(acceptance) > 1:
            issues.append("Conflicting new-patient acceptance values.")
        if "Pending" in statuses and "Yes" in acceptance:
            issues.append("Pending credentials with new-patient acceptance.")

        # Count identical business records within each source.
        # All original records remain available in provenance.
        seen = set()
        for record in members:
            signature = (
                record["source"],
                tuple(sorted(
                    (k, v) for k, v in record["original"].items()
                    if k != SOURCES[record["source"]]["record_id"]
                )),
            )
            if signature in seen:
                duplicate_count += 1
            seen.add(signature)

        result = {
            "provider_id": members[0]["provider_id"] or None,
            "review_reference": key,
            **values,
            "credentialing_status": statuses,
            "accepting_new_patients": acceptance,
            "issues": issues,
            "provenance": [
                {
                    "source": r["source"],
                    "record_id": r["record_id"],
                    "original": r["original"],
                }
                for r in members
            ],
        }
        (review if issues else ready).append(result)

    return ready, review, duplicate_count


def main():
    records = load_records()
    ready, review, duplicates = curate(records)
    OUTPUT.mkdir(exist_ok=True)

    summary = {
        "input_records": len(records),
        "ready_records": len(ready),
        "review_records": len(review),
        "identical_duplicates_consolidated": duplicates,
        "synthetic_data_only": True,
    }
    for name, content in (
        ("ready_records.json", ready),
        ("review_records.json", review),
        ("summary.json", summary),
    ):
        (OUTPUT / name).write_text(
            json.dumps(content, indent=2) + "\n", encoding="utf-8"
        )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
