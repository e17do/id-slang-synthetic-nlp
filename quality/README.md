# Quality Audit Module

The `quality/` directory contains the linguistic quality assurance system for **id-slang-synthetic-nlp**.

Unlike `validation/`, which verifies JSON structure and schema integrity, this module evaluates the linguistic quality of the dataset.

---

## Purpose

The quality audit answers questions such as:

- Is the dataset linguistically diverse?
- Are sentence templates repeated too often?
- Is slang coverage balanced?
- Are sentiment labels overly fragmented?
- Is regional language distribution healthy?
- Does the dataset resemble natural Indonesian social-media language?

---

## Audit Categories

| Module | Purpose |
|---------|---------|
| Slang Coverage | Measure unique slang diversity and frequency |
| Template Audit | Detect repetitive sentence structures |
| Sentiment Audit | Evaluate emotional label distribution |
| Regional Audit | Measure geographic and demographic balance |
| Naturalness Audit | Detect synthetic generation artifacts |

---

## Output

Future audit reports will be stored in:

```text
reports/
├── dataset_quality_report.json
├── slang_statistics.json
├── sentiment_statistics.json
└── regional_statistics.json
```

These reports are generated automatically and should not be edited manually.

---

## Difference Between Validation and Quality

| Validation | Quality Audit |
|------------|---------------|
| JSON syntax | Linguistic diversity |
| Required fields | Template repetition |
| Duplicate IDs | Slang richness |
| Sequential IDs | Natural sentence variation |
| Schema compliance | Regional balance |

---

## Quality Philosophy

A larger dataset is **not automatically a better dataset**.

This project prioritizes:

1. Natural language diversity
2. Minimal template repetition
3. Broad slang coverage
4. Regional linguistic representation
5. Reproducible quality evaluation

Every future dataset release should pass both **Validation** and **Quality Audit** before publication.
