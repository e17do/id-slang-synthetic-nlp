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

REQUIRED_FIELDS = {
    "id",
    "konteks_percakapan",
    "ragam_slang",
    "sentimen_emosi",
    "lokasi_dominan",
}

ID_PATTERN = re.compile(r"^ID-NLP-(\d{3,6})$")


def normalize_text(text):
    """Normalize text for duplicate / near-duplicate detection."""
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text


def tokenize(text):
    """Simple whitespace tokenizer."""
    return normalize_text(text).split()


def similarity_score(a, b):
    """
    Jaccard similarity based on word sets.
    Used as a lightweight near-duplicate detector.
    """
    a_tokens = set(tokenize(a))
    b_tokens = set(tokenize(b))

    if not a_tokens or not b_tokens:
        return 0.0

    intersection = len(a_tokens & b_tokens)
    union = len(a_tokens | b_tokens)

    return intersection / union


def validate_json_structure(data):
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
                f"Record #{index}: field tambahan tidak diizinkan: {sorted(extra)}"
            )

        for field in REQUIRED_FIELDS:
            if field not in record:
                continue

            if not isinstance(record[field], str):
                errors.append(
                    f"Record #{index}: '{field}' harus berupa string."
                )

            elif not record[field].strip():
                errors.append(
                    f"Record #{index}: '{field}' tidak boleh kosong."
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

    # Duplicate ID
    counts = Counter(ids)

    duplicates = [
        value for value, count in counts.items()
        if count > 1
    ]

    if duplicates:
        errors.append(
            f"Duplicate ID ditemukan: {duplicates[:20]}"
        )

    # Sequential ID
    if ids:
        expected = list(range(ids[0], ids[0] + len(ids)))

        if ids != expected:
            for position, (actual, wanted) in enumerate(
                zip(ids, expected),
                start=1
            ):
                if actual != wanted:
                    errors.append(
                        f"ID tidak berurutan pada posisi #{position}: "
                        f"ditemukan ID-NLP-{actual:03d}, "
                        f"seharusnya ID-NLP-{wanted:03d}"
                    )
                    break

    return errors


def validate_exact_duplicates(data):
    errors = []

    fields_to_check = [
        "konteks_percakapan",
    ]

    for field in fields_to_check:

        normalized_values = {}

        for index, record in enumerate(data, start=1):
            value = record.get(field)

            if not isinstance(value, str):
                continue

            normalized = normalize_text(value)

            if normalized in normalized_values:
                errors.append(
                    f"Duplicate {field}: "
                    f"record #{normalized_values[normalized]} "
                    f"dan #{index}"
                )
            else:
                normalized_values[normalized] = index

    return errors


def detect_near_duplicates(data, threshold=0.85, max_reports=100):
    warnings = []

    texts = []

    for index, record in enumerate(data, start=1):
        text = record.get("konteks_percakapan")

        if isinstance(text, str):
            texts.append((index, text))

    # Lightweight O(n²) comparison.
    # Suitable for moderate datasets.
    # For very large datasets this should later be replaced
    # with MinHash / locality-sensitive hashing.
    for i in range(len(texts)):
        index_a, text_a = texts[i]

        for j in range(i + 1, len(texts)):
            index_b, text_b = texts[j]

            score = similarity_score(text_a, text_b)

            if score >= threshold:

                warnings.append(
                    f"Near-duplicate kandidat: "
                    f"record #{index_a} dan #{index_b} "
                    f"(similarity={score:.2f})"
                )

                if len(warnings) >= max_reports:
                    return warnings

    return warnings


def detect_repeated_templates(data):
    warnings = []

    first_patterns = Counter()

    for record in data:
        text = record.get("konteks_percakapan")

        if not isinstance(text, str):
            continue

        tokens = tokenize(text)

        if len(tokens) >= 5:
            pattern = " ".join(tokens[:5])
            first_patterns[pattern] += 1

    repeated = [
        (pattern, count)
        for pattern, count in first_patterns.items()
        if count >= 5
    ]

    for pattern, count in sorted(
        repeated,
        key=lambda x: x[1],
        reverse=True
    ):
        warnings.append(
            f"Template pembuka berulang {count}x: '{pattern} ...'"
        )

    return warnings


def generate_statistics(data):
    sentiment_counter = Counter()
    location_counter = Counter()
    slang_counter = Counter()

    for record in data:
        sentiment_counter[
            record.get("sentimen_emosi", "")
        ] += 1

        location_counter[
            record.get("lokasi_dominan", "")
        ] += 1

        slang_counter[
            record.get("ragam_slang", "")
        ] += 1

    return {
        "total_records": len(data),
        "unique_ids": len({
            record.get("id")
            for record in data
        }),
        "unique_contexts": len({
            normalize_text(
                record.get("konteks_percakapan", "")
            )
            for record in data
        }),
        "sentiment_distribution": dict(sentiment_counter),
        "location_distribution": dict(location_counter),
        "top_slang": slang_counter.most_common(20),
    }


def main():

    print("=" * 70)
    print("id-slang-synthetic-nlp DATASET VALIDATOR")
    print("=" * 70)

    if not DATASET_PATH.exists():
        print()
        print(f"ERROR: Dataset tidak ditemukan:")
        print(f"       {DATASET_PATH}")
        sys.exit(1)

    # --------------------------------------------------------
    # Load JSON
    # --------------------------------------------------------

    try:
        with DATASET_PATH.open(
            "r",
            encoding="utf-8"
        ) as file:
            data = json.load(file)

    except json.JSONDecodeError as error:
        print()
        print("ERROR: JSON tidak valid.")
        print()
        print(f"Line   : {error.lineno}")
        print(f"Column : {error.colno}")
        print(f"Message: {error.msg}")
        sys.exit(1)

    except Exception as error:
        print()
        print(f"ERROR saat membaca dataset: {error}")
        sys.exit(1)

    print()
    print(f"Dataset : {DATASET_PATH}")
    print(f"Records : {len(data)}")

    # --------------------------------------------------------
    # Structural validation
    # --------------------------------------------------------

    errors = []

    errors.extend(
        validate_json_structure(data)
    )

    errors.extend(
        validate_ids(data)
    )

    errors.extend(
        validate_exact_duplicates(data)
    )

    # --------------------------------------------------------
    # Warnings
    # --------------------------------------------------------

    near_duplicates = detect_near_duplicates(data)

    template_warnings = detect_repeated_templates(data)

    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    statistics = generate_statistics(data)

    # --------------------------------------------------------
    # Output
    # --------------------------------------------------------

    print()
    print("-" * 70)
    print("STATISTICS")
    print("-" * 70)

    print(
        f"Total records      : "
        f"{statistics['total_records']}"
    )

    print(
        f"Unique IDs         : "
        f"{statistics['unique_ids']}"
    )

    print(
        f"Unique contexts    : "
        f"{statistics['unique_contexts']}"
    )

    print()
    print("Sentiment:")
    for label, count in sorted(
        statistics["sentiment_distribution"].items(),
        key=lambda x: x[1],
        reverse=True
    ):
        print(f"  - {label}: {count}")

    print()
    print("Lokasi:")
    for location, count in sorted(
        statistics["location_distribution"].items(),
        key=lambda x: x[1],
        reverse=True
    )[:20]:
        print(f"  - {location}: {count}")

    # --------------------------------------------------------
    # Errors
    # --------------------------------------------------------

    print()
    print("-" * 70)
    print("VALIDATION")
    print("-" * 70)

    if errors:

        print()
        print(f"FAILED: {len(errors)} error ditemukan.")

        for error in errors[:100]:
            print(f"  [ERROR] {error}")

        if len(errors) > 100:
            print(
                f"  ... dan {len(errors) - 100} error lainnya."
            )

        sys.exit(1)

    print()
    print("PASS: Struktur dasar dataset valid.")

    # --------------------------------------------------------
    # Warnings
    # --------------------------------------------------------

    if near_duplicates:
        print()
        print(
            f"WARNING: {len(near_duplicates)} "
            "kandidat near-duplicate ditemukan."
        )

        for warning in near_duplicates[:20]:
            print(f"  [WARNING] {warning}")

    else:
        print()
        print("PASS: Tidak ditemukan near-duplicate signifikan.")

    if template_warnings:
        print()
        print(
            f"WARNING: {len(template_warnings)} "
            "pola template berulang ditemukan."
        )

        for warning in template_warnings[:20]:
            print(f"  [WARNING] {warning}")

    else:
        print()
        print("PASS: Tidak ditemukan template pembuka berulang.")

    # --------------------------------------------------------
    # Final result
    # --------------------------------------------------------

    print()
    print("=" * 70)

    if errors:
        print("RESULT: FAIL")
        sys.exit(1)

    if near_duplicates or template_warnings:
        print(
            "RESULT: PASS WITH WARNINGS"
        )
    else:
        print("RESULT: PASS")

    print("=" * 70)


if __name__ == "__main__":
    main()
