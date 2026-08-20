import json
import re
import sys
from pathlib import Path
from collections import Counter

# ============================================================
# id-slang-synthetic-nlp
# Dataset Quality Validator
# ============================================================

DATASET_PATH = Path("dataset/dataset_slang_indonesia.json")
REPORT_PATH = Path("reports/dataset_quality_report.json")

REQUIRED_FIELDS = {
    "id",
    "konteks_percakapan",
    "ragam_slang",
    "sentimen_emosi",
    "lokasi_dominan",
}

ID_PATTERN = re.compile(r"^ID-NLP-(\d{3,6})$")


def normalize_text(text):
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text


def tokenize(text):
    return normalize_text(text).split()


def validate_structure(data):
    errors = []

    if not isinstance(data, list):
        errors.append("Root JSON harus berupa array/list.")
        return errors

    for index, record in enumerate(data, start=1):

        if not isinstance(record, dict):
            errors.append(
                f"Record #{index} bukan object JSON."
            )
            continue

        fields = set(record.keys())

        missing = REQUIRED_FIELDS - fields
        extra = fields - REQUIRED_FIELDS

        if missing:
            errors.append(
                f"Record #{index}: field hilang: {sorted(missing)}"
            )

        if extra:
            errors.append(
                f"Record #{index}: field tambahan: {sorted(extra)}"
            )

        for field in REQUIRED_FIELDS:

            if field not in record:
                continue

            value = record[field]

            if not isinstance(value, str):
                errors.append(
                    f"Record #{index}: '{field}' harus string."
                )

            elif not value.strip():
                errors.append(
                    f"Record #{index}: '{field}' kosong."
                )

    return errors


def validate_ids(data):

    errors = []
    ids = []

    for index, record in enumerate(data, start=1):

        record_id = record.get("id")

        if not isinstance(record_id, str):
            continue

        match = ID_PATTERN.match(record_id)

        if not match:
            errors.append(
                f"Record #{index}: ID tidak valid: {record_id}"
            )
            continue

        ids.append(int(match.group(1)))

    counter = Counter(ids)

    duplicate_ids = sorted(
        value
        for value, count in counter.items()
        if count > 1
    )

    if duplicate_ids:
        errors.append(
            f"Duplicate ID ditemukan: {duplicate_ids[:20]}"
        )

    sequence_errors = []

    if ids:

        for position, actual in enumerate(ids):

            expected = ids[0] + position

            if actual != expected:
                sequence_errors.append({
                    "position": position + 1,
                    "expected": expected,
                    "actual": actual
                })

                if len(sequence_errors) >= 20:
                    break

    if sequence_errors:
        errors.append(
            "ID tidak berurutan."
        )

    return errors, ids, duplicate_ids, sequence_errors


def duplicate_contexts(data):

    mapping = {}

    duplicates = []

    for index, record in enumerate(data, start=1):

        text = record.get("konteks_percakapan")

        if not isinstance(text, str):
            continue

        normalized = normalize_text(text)

        if normalized in mapping:

            duplicates.append({
                "record_1": mapping[normalized],
                "record_2": index,
                "context": text
            })

        else:
            mapping[normalized] = index

    return duplicates


def distribution(data, field):

    counter = Counter()

    for record in data:

        value = record.get(field)

        if isinstance(value, str):
            counter[value] += 1

    return dict(
        sorted(
            counter.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )


def repeated_openings(data):

    counter = Counter()

    for record in data:

        text = record.get("konteks_percakapan")

        if not isinstance(text, str):
            continue

        tokens = tokenize(text)

        if len(tokens) >= 5:

            opening = " ".join(tokens[:5])

            counter[opening] += 1

    return {
        phrase: count
        for phrase, count in counter.items()
        if count >= 5
    }


def build_report(
    data,
    ids,
    duplicate_ids,
    sequence_errors,
    duplicate_context_list,
    template_warnings,
    errors
):

    report = {

        "dataset": {
            "path": str(DATASET_PATH),
            "total_records": len(data),
            "first_id": (
                f"ID-NLP-{ids[0]:03d}"
                if ids else None
            ),
            "last_id": (
                f"ID-NLP-{ids[-1]:03d}"
                if ids else None
            )
        },

        "integrity": {

            "unique_ids": len(set(ids)),

            "duplicate_id_count":
                len(duplicate_ids),

            "duplicate_ids":
                [
                    f"ID-NLP-{value:03d}"
                    for value in duplicate_ids
                ],

            "sequence_error_count":
                len(sequence_errors),

            "sequence_errors":
                sequence_errors,

            "unique_context_count":
                len({
                    normalize_text(
                        record.get(
                            "konteks_percakapan",
                            ""
                        )
                    )
                    for record in data
                }),

            "duplicate_context_count":
                len(duplicate_context_list)
        },

        "distribution": {

            "sentimen_emosi":
                distribution(
                    data,
                    "sentimen_emosi"
                ),

            "lokasi_dominan":
                distribution(
                    data,
                    "lokasi_dominan"
                ),

            "ragam_slang":
                distribution(
                    data,
                    "ragam_slang"
                )
        },

        "quality": {

            "template_warning_count":
                len(template_warnings),

            "template_warnings":
                template_warnings,

            "duplicate_context_examples":
                duplicate_context_list[:50]
        },

        "validation": {

            "error_count":
                len(errors),

            "status":
                "FAIL" if errors else "PASS"
        }
    }

    return report


def main():

    print("=" * 70)
    print("id-slang-synthetic-nlp DATASET VALIDATOR")
    print("=" * 70)

    if not DATASET_PATH.exists():

        print(
            f"ERROR: Dataset tidak ditemukan: "
            f"{DATASET_PATH}"
        )

        sys.exit(1)

    try:

        with DATASET_PATH.open(
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

    except json.JSONDecodeError as error:

        print("ERROR: JSON tidak valid.")

        print(
            f"Line: {error.lineno}"
        )

        print(
            f"Column: {error.colno}"
        )

        print(
            f"Message: {error.msg}"
        )

        sys.exit(1)

    structure_errors = validate_structure(data)

    id_errors, ids, duplicate_ids, sequence_errors = (
        validate_ids(data)
    )

    duplicate_context_list = duplicate_contexts(data)

    template_warnings = repeated_openings(data)

    errors = (
        structure_errors
        + id_errors
    )

    report = build_report(
        data,
        ids,
        duplicate_ids,
        sequence_errors,
        duplicate_context_list,
        template_warnings,
        errors
    )

    REPORT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with REPORT_PATH.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            ensure_ascii=False,
            indent=2
        )

        file.write("\n")

    print()
    print(
        f"Records: {len(data)}"
    )

    print(
        f"Unique IDs: {len(set(ids))}"
    )

    print(
        f"Duplicate IDs: {len(duplicate_ids)}"
    )

    print(
        f"Duplicate contexts: "
        f"{len(duplicate_context_list)}"
    )

    print(
        f"Template warnings: "
        f"{len(template_warnings)}"
    )

    print()

    if errors:

        print(
            f"RESULT: FAIL "
            f"({len(errors)} errors)"
        )

        for error in errors[:50]:

            print(
                f"[ERROR] {error}"
            )

        sys.exit(1)

    print(
        "RESULT: PASS"
    )


if __name__ == "__main__":
    main()
