# Dataset Data Dictionary

## Indonesian Casual Language & Slang Synthetic Dataset

This document describes the structure, fields, values, and intended interpretation of the dataset contained in:

`dataset/dataset_slang_indonesia.json`

The data dictionary is provided to make the dataset easier to understand, analyze, validate, and integrate into NLP/AI workflows.

> **Dataset version:** `v1.0.0`
> **Record count:** 20,000
> **Data type:** Synthetic
> **Primary language:** Indonesian

---

## 1. Record Structure

Each dataset record follows the following general structure:

```json
{
  "id": "ID-NLP-0001",
  "konteks_percakapan": "...",
  "ragam_slang": "...",
  "sentimen_emosi": "...",
  "lokasi_dominan": "..."
}
```

Each field has a specific purpose described below.

---

# 2. Field Reference

| Field                | Type   | Required | Description                                                                                                                  |
| -------------------- | ------ | -------: | ---------------------------------------------------------------------------------------------------------------------------- |
| `id`                 | string |      Yes | Unique identifier for the dataset record.                                                                                    |
| `konteks_percakapan` | string |      Yes | Synthetic Indonesian conversational context or sentence containing the relevant linguistic usage.                            |
| `ragam_slang`        | string |      Yes | Slang, informal expression, internet expression, abbreviation, or other informal-language feature represented by the record. |
| `sentimen_emosi`     | string |      Yes | Sentiment or emotional interpretation associated with the context.                                                           |
| `lokasi_dominan`     | string |      Yes | Dominant geographic, demographic, community, or contextual association represented by the record.                            |

---

# 3. `id`

### Type

`string`

### Example

```text
ID-NLP-0001
```

### Purpose

Provides a unique identifier for each dataset record.

The identifier is intended to make individual records easier to:

* reference;
* validate;
* track;
* compare between releases;
* report in research;
* identify during quality review.

### Current convention

The current dataset uses identifiers following the general pattern:

```text
ID-NLP-<NUMBER>
```

Example:

```text
ID-NLP-0001
ID-NLP-0002
ID-NLP-0003
...
```

The current release contains 20,000 records.

### Important

The ID should be treated as an identifier rather than as linguistic information.

The numeric portion does not represent:

* ranking;
* quality;
* geographic location;
* sentiment;
* difficulty;
* importance.

---

# 4. `konteks_percakapan`

### Type

`string`

### Purpose

Contains the synthetic conversational context in which the slang or informal expression occurs.

The context is intended to provide more information than an isolated slang word.

For example, instead of storing only:

```text
"gabut"
```

the dataset may provide a conversational context in which the expression appears.

This allows users to study slang in context rather than as isolated vocabulary.

### Potential applications

This field may be useful for:

* contextual slang detection;
* sentiment analysis;
* emotion analysis;
* intent classification;
* conversational AI;
* text classification;
* language-model experimentation;
* informal-language understanding.

### Important limitation

The context is synthetic.

It should not be interpreted as:

* a real conversation;
* a quotation from a real individual;
* a statistically representative sample of Indonesian conversation.

---

# 5. `ragam_slang`

### Type

`string`

### Purpose

Identifies the slang, informal expression, internet expression, abbreviation, or other non-formal linguistic feature represented by the record.

Depending on the record, this may include expressions associated with:

* Indonesian slang;
* internet language;
* social-media language;
* conversational abbreviations;
* youth-oriented expressions;
* informal vocabulary;
* code-switching;
* community-specific expressions;
* other informal linguistic patterns.

### Potential applications

This field can be used for:

* slang detection;
* vocabulary analysis;
* informal-language classification;
* normalization research;
* text preprocessing;
* linguistic analysis;
* NLP feature extraction.

### Interpretation

The value should be interpreted together with `konteks_percakapan`.

An expression may have different meanings depending on:

* context;
* speaker intent;
* community;
* region;
* platform;
* generation;
* surrounding words.

Therefore, `ragam_slang` should not always be treated as an independent dictionary definition.

---

# 6. `sentimen_emosi`

### Type

`string`

### Purpose

Represents the sentiment or emotional interpretation associated with the conversational context.

The field may contain sentiment-oriented or emotion-oriented labels.

The current release preserves the original annotation taxonomy of `v1.0.0`.

### Important

The current release intentionally preserves its original annotation structure.

Future releases may introduce a more formally separated taxonomy for:

```text
sentiment
emotion
intent
attitude
expression
```

Such changes should be introduced through a new dataset version rather than silently modifying the existing `v1.0.0` records.

### Interpretation

This field represents an annotation associated with the synthetic context.

It should not be interpreted as an objectively measurable psychological state of a real person.

### Potential applications

* sentiment classification;
* emotion classification;
* conversational analysis;
* text classification;
* NLP benchmarking;
* data augmentation;
* exploratory linguistic research.

---

# 7. `lokasi_dominan`

### Type

`string`

### Purpose

Represents the dominant geographic, demographic, community, or contextual association assigned to the linguistic example.

This field is intended to help represent variation in Indonesian informal language.

Possible uses include analysis of:

* regional linguistic variation;
* urban vs. broader Indonesian usage;
* community-associated language;
* contextual variation;
* regional slang research.

### Important limitation

`lokasi_dominan` should **not** be interpreted as precise geographic metadata about a real person.

It does not establish:

* a speaker's actual location;
* a user's home address;
* a person's identity;
* a precise geographic origin of an expression.

The field represents the contextual or regional association used when constructing the synthetic record.

---

# 8. Relationship Between Fields

The fields are intended to be interpreted together.

A simplified conceptual relationship is:

```text
konteks_percakapan
        │
        ├── ragam_slang
        │
        ├── sentimen_emosi
        │
        └── lokasi_dominan
```

The conversational context provides the main linguistic example.

The other fields provide structured metadata describing different aspects of that example.

---

# 9. Example Interpretation

Consider a hypothetical record:

```json
{
  "id": "ID-NLP-0001",
  "konteks_percakapan": "Gue lagi gabut banget, ada yang mau mabar?",
  "ragam_slang": "gabut",
  "sentimen_emosi": "Positif",
  "lokasi_dominan": "Urban Indonesia"
}
```

This can be interpreted as:

* `id` identifies the record;
* `konteks_percakapan` provides the synthetic conversational example;
* `ragam_slang` identifies the informal expression;
* `sentimen_emosi` provides the associated annotation;
* `lokasi_dominan` provides the contextual/regional association.

The example should not be interpreted as a real quotation.

---

# 10. Data Type Expectations

The current dataset expects all five primary fields to be represented as strings.

Example:

```text
id                  → string
konteks_percakapan  → string
ragam_slang         → string
sentimen_emosi      → string
lokasi_dominan      → string
```

Applications consuming the dataset should validate these assumptions before processing.

---

# 11. Missing or Empty Values

Consumers should verify the dataset for missing or empty values before production use.

The repository includes validation tooling intended to detect structural problems.

See:

```text
validation/
```

and:

```text
quality/
```

An application should not assume that a future dataset version will necessarily preserve exactly the same field set.

---

# 12. Duplicate Context

The dataset includes validation intended to identify duplicate conversational contexts.

Duplicate detection is useful because repeated contexts can affect:

* model training;
* evaluation;
* statistical analysis;
* dataset diversity.

Users performing their own machine-learning experiments should still perform task-specific duplicate and leakage checks.

---

# 13. Synthetic Data Considerations

All records should be treated as synthetic examples.

This has several implications.

### Do not use the dataset as:

* a census of Indonesian slang;
* a frequency study of Indonesian speakers;
* evidence of actual regional prevalence;
* a psychological dataset;
* a source of real user conversations.

### The dataset may be useful as:

* an NLP experimentation resource;
* a synthetic training resource;
* a data augmentation resource;
* a classification benchmark candidate;
* a linguistic exploration resource;
* a prototype-development dataset.

---

# 14. Recommended Processing

For exploratory NLP work, a typical workflow may be:

```text
Load dataset
    ↓
Validate schema
    ↓
Check missing values
    ↓
Check duplicates
    ↓
Inspect label distribution
    ↓
Create task-specific split
    ↓
Train / evaluate model
    ↓
Compare against appropriate real-world data
```

The repository's validation tools can be used as an initial structural check.

---

# 15. Recommended Train/Test Practice

The dataset is not intended to prescribe a single train/test split.

For machine-learning experiments, users should create a task-specific split appropriate to their objective.

Recommended considerations include:

* avoiding duplicate contexts across splits;
* avoiding obvious lexical leakage;
* maintaining reasonable label distribution;
* preserving relevant linguistic diversity;
* documenting the random seed;
* documenting the split ratio;
* keeping an untouched evaluation set when possible.

For serious benchmarking, an external or human-reviewed evaluation set is recommended.

---

# 16. Version Compatibility

The data dictionary describes the `v1.0.0` dataset structure.

Future versions may introduce:

* additional fields;
* more detailed annotations;
* normalized text;
* separate sentiment and emotion fields;
* confidence scores;
* quality scores;
* linguistic categories;
* additional regional metadata.

Such changes should be documented in `CHANGELOG.md`.

Applications should therefore avoid assuming that future releases will be byte-for-byte or schema-for-schema compatible.

---

# 17. Related Files

The following repository files provide additional information:

```text
README.md
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

---

# 18. Data Usage and Licensing

The data dictionary does not grant additional rights to use the dataset.

Dataset usage is governed by:

```text
DATASET_LICENSE.md
```

The source code is governed separately by:

```text
LICENSE
```

Users should review the applicable license before using the dataset for research, commercial development, redistribution, or derivative works.

---

# 19. Summary

The dataset is structured around five primary fields:

```text
id
konteks_percakapan
ragam_slang
sentimen_emosi
lokasi_dominan
```

Together, these fields provide a structured representation of synthetic Indonesian informal-language examples.

The current release prioritizes preservation of the original 20,000-record dataset while providing supporting documentation, validation, and tooling around the data.

Future releases may add richer annotations without modifying the integrity of the current `v1.0.0` release.
