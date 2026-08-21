# Data Dictionary — id-slang-synthetic-nlp

This document defines the machine-readable fields in the `v1.0.0` dataset.

## Dataset Scope

| Property | Value |
|---|---|
| Release | `v1.0.0` |
| Records | **20,000** |
| Data type | Synthetic |
| Primary language | Indonesian (`id`) |
| Format | JSON |
| Schema | `schema/dataset_schema.json` |

## Core Fields

| Field Name | Data Type | Required | Description | Example |
|---|---|---:|---|---|
| `id` | String | Yes | Unique record identifier following the `ID-NLP-<NUMBER>` convention. | `ID-NLP-0055` |
| `konteks_percakapan` | String | Yes | Synthetic Indonesian conversational text containing the linguistic feature represented by the record. | `Posisi gue lagi boncos parah.` |
| `ragam_slang` | String | Yes | Slang, informal expression, internet expression, abbreviation, or related linguistic feature represented by the record. | `boncos` |
| `sentimen_emosi` | String | Yes | Categorical sentiment/emotion annotation associated with the synthetic conversational context. | `Kecewa` |
| `lokasi_dominan` | String | Yes | Regional or contextual association assigned to the synthetic example. | `Binjai` |

## Field Semantics

### `id`

A stable identifier for a dataset record.

The identifier is not a linguistic feature and does not encode:

- ranking;
- quality;
- geography;
- sentiment;
- difficulty;
- importance.

Current convention:

```text
ID-NLP-0001
ID-NLP-0002
...
ID-NLP-20000
```

### `konteks_percakapan`

Synthetic conversational context.

The field exists so that an expression can be evaluated in context rather than only as an isolated token.

It may support:

- slang detection;
- text classification;
- sentiment/emotion experiments;
- conversational-language research;
- NLP experimentation.

It must not be interpreted as a quotation from a real person.

### `ragam_slang`

The target informal linguistic feature represented by the record.

It may include:

- slang;
- internet expressions;
- abbreviations;
- informal vocabulary;
- community-associated expressions;
- code-switching;
- other informal linguistic patterns.

The field should be interpreted together with `konteks_percakapan`, because an expression can have context-dependent meanings.

### `sentimen_emosi`

The annotation associated with the synthetic conversational context.

It should not be interpreted as a measured psychological state of a real person.

The `v1.0.0` release preserves its existing combined sentiment/emotion field. Future releases may separate sentiment, emotion, intent, or related dimensions through versioned schema changes.

### `lokasi_dominan`

The regional/contextual association assigned during dataset construction.

It does **not** establish:

- actual speaker location;
- residence;
- identity;
- precise geographic origin of an expression;
- prevalence within a population.

It is contextual metadata for linguistic analysis.

## Data-Type Contract

For `v1.0.0`, all five primary fields are strings:

```text
id                  → string
konteks_percakapan  → string
ragam_slang        → string
sentimen_emosi      → string
lokasi_dominan     → string
```

Consumers should validate against `schema/dataset_schema.json` rather than relying only on this summary.

## Relationship Between Fields

Conceptually:

```text
konteks_percakapan
        │
        ├── ragam_slang
        ├── sentimen_emosi
        └── lokasi_dominan
```

The conversation is the primary linguistic example. The other fields provide structured metadata about that example.

## Missing Values

Consumers should check for missing or empty values before production use.

The repository's validation tooling provides an initial structural check.

## Duplicate and Leakage Considerations

The repository includes validation for duplicate identifiers and duplicate contexts.

Users performing machine-learning experiments should additionally check:

- near-duplicate contexts;
- lexical leakage;
- repeated templates;
- train/test contamination;
- task-specific label leakage.

## Synthetic Data Interpretation

The dataset is synthetic.

Therefore:

- record counts do not represent real-world frequency;
- regional associations do not prove geographic prevalence;
- labels do not represent verified psychological states;
- examples should not be treated as real conversations;
- absence of a term does not prove that the term is unused.

## Version Compatibility

This dictionary describes `v1.0.0`.

Future releases may add fields or introduce more granular annotations. Such changes must be documented in `CHANGELOG.md` and associated with an explicit dataset version.

Consumers should validate each release against its published schema.

## Related Files

```text
README.md
DATASET_CARD.md
DATASET_LICENSE.md
CHANGELOG.md
CITATION.cff
schema/dataset_schema.json
annotations/
linguistic_taxonomy/
linguistic_clusters/
validation/
quality/
reports/
```

## Licensing

This document describes the data structure; it does not grant additional rights.

Dataset rights and conditions are defined in:

```text
DATASET_LICENSE.md
```

Repository code is governed separately by:

```text
LICENSE
```
