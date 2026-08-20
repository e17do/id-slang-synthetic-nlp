import json
import re
from pathlib import Path
from collections import Counter

DATASET_PATH = Path("dataset/dataset_slang_indonesia.json")
OUTPUT_PATH = Path("reports/quality_audit.json")


def normalize(text):
    text = str(text).lower().strip()
    text = re.sub(r"\s+", " ", text)
    return text


def words(text):
    return normalize(text).split()


def load_dataset():
    with DATASET_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def frequency_stats(values):
    counter = Counter(values)

    return {
        "unique": len(counter),
        "min_frequency": min(counter.values()) if counter else 0,
        "max_frequency": max(counter.values()) if counter else 0,
        "frequency_distribution": dict(
            sorted(
                Counter(counter.values()).items()
            )
        ),
        "top_50": counter.most_common(50),
        "single_occurrence": sorted(
            value for value, count in counter.items()
            if count == 1
        ),
        "over_100": sorted(
            [
                [value, count]
                for value, count in counter.items()
                if count > 100
            ],
            key=lambda x: x[1],
            reverse=True
        )
    }


def template_audit(records):
    opening_counter = Counter()
    word_count_counter = Counter()

    for record in records:
        text = record.get("konteks_percakapan", "")
        token_list = words(text)

        if token_list:
            opening = " ".join(token_list[:5])
            opening_counter[opening] += 1

        word_count_counter[len(token_list)] += 1

    repeated_openings = [
        [opening, count]
        for opening, count in opening_counter.items()
        if count >= 5
    ]

    repeated_openings.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return {
        "unique_openings": len(opening_counter),
        "repeated_openings_count": len(repeated_openings),
        "repeated_openings": repeated_openings[:100],
        "word_count_distribution": dict(
            sorted(word_count_counter.items())
        )
    }


def sentiment_stats(records):
    values = [
        record.get("sentimen_emosi", "")
        for record in records
    ]

    counter = Counter(values)

    return {
        "unique_labels": len(counter),
        "distribution": counter.most_common()
    }


def location_stats(records):
    values = [
        record.get("lokasi_dominan", "")
        for record in records
    ]

    counter = Counter(values)

    return {
        "unique_locations": len(counter),
        "distribution": counter.most_common()
    }


def slang_stats(records):
    values = [
        record.get("ragam_slang", "")
        for record in records
    ]

    return frequency_stats(values)


def dataset_stats(records):
    lengths = [
        len(words(record.get("konteks_percakapan", "")))
        for record in records
    ]

    return {
        "total_records": len(records),
        "average_word_count": (
            sum(lengths) / len(lengths)
            if lengths else 0
        ),
        "minimum_word_count": min(lengths) if lengths else 0,
        "maximum_word_count": max(lengths) if lengths else 0
    }


def main():
    print("=" * 70)
    print("INDONESIAN SLANG DATASET — QUALITY AUDIT")
    print("=" * 70)

    records = load_dataset()

    report = {
        "dataset": dataset_stats(records),
        "slang": slang_stats(records),
        "sentiment": sentiment_stats(records),
        "location": location_stats(records),
        "templates": template_audit(records)
    }

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with OUTPUT_PATH.open(
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            report,
            f,
            ensure_ascii=False,
            indent=2
        )
        f.write("\n")

    print()
    print(f"Records           : {len(records)}")
    print(
        f"Unique slang      : "
        f"{report['slang']['unique']}"
    )
    print(
        f"Unique sentiment  : "
        f"{report['sentiment']['unique_labels']}"
    )
    print(
        f"Unique locations  : "
        f"{report['location']['unique_locations']}"
    )
    print(
        f"Repeated openings : "
        f"{report['templates']['repeated_openings_count']}"
    )

    print()
    print(f"Report: {OUTPUT_PATH}")
    print()
    print("QUALITY AUDIT COMPLETED")


if __name__ == "__main__":
    main()
