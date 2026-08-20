import json
from pathlib import Path
from collections import Counter

DATASET_PATH = Path(
    "dataset/dataset_slang_indonesia.json"
)

REPORT_DIR = Path("reports")

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

with open(
    DATASET_PATH,
    "r",
    encoding="utf-8"
) as file:
    data = json.load(file)

slang_counter = Counter()
sentiment_counter = Counter()
location_counter = Counter()

for row in data:

    slang_counter[
        row["ragam_slang"]
    ] += 1

    sentiment_counter[
        row["sentimen_emosi"]
    ] += 1

    location_counter[
        row["lokasi_dominan"]
    ] += 1

summary = {

    "total_records":
        len(data),

    "unique_slang":
        len(slang_counter),

    "unique_sentiment":
        len(sentiment_counter),

    "unique_location":
        len(location_counter),

    "top_50_slang":
        slang_counter.most_common(50),

    "top_50_sentiment":
        sentiment_counter.most_common(50),

    "top_50_location":
        location_counter.most_common(50)
}

with open(
    REPORT_DIR /
    "audit_summary.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        summary,
        file,
        ensure_ascii=False,
        indent=2
    )

print(
    "Audit complete:"
)

print(
    REPORT_DIR /
    "audit_summary.json"
)
