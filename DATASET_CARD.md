---
language:
  - id
license: mit
size_categories:
  - 10K<n<100K
task_categories:
  - text-classification
  - token-classification
pretty_name: Indonesian Casual Language & Slang Synthetic Dataset
---

# Dataset Card

## Indonesian Casual Language & Slang Synthetic Dataset

### 1. Dataset Summary

| Property | Value |
|---|---|
| Dataset name | Indonesian Casual Language & Slang Synthetic Dataset |
| Repository | `e17do/id-slang-synthetic-nlp` |
| Current release | `v1.0.0` |
| Records | **20,000** |
| Primary language | Indonesian (`id`) |
| Data type | Synthetic |
| Main format | JSON |
| Primary focus | Indonesian informal language, slang, internet expressions, conversational language |

This dataset provides structured synthetic examples of Indonesian informal and conversational language for NLP research, experimentation, model development, evaluation, and data augmentation.

### 2. Dataset Description

The dataset covers linguistic phenomena that may occur in informal Indonesian environments, including:

- slang;
- abbreviations;
- internet expressions;
- casual vocabulary;
- social-media language;
- Indonesian-English code-switching;
- community-associated expressions;
- regional/context-associated language;
- informal emotional expressions.

The dataset is **synthetic**. It is not a transcription corpus of private or real-world conversations.

### 3. Intended Uses

Potential uses include:

- slang detection and classification;
- informal-language classification;
- sentiment and emotion experiments;
- conversational-language research;
- text classification;
- data augmentation;
- Indonesian NLP experimentation;
- language-model prototyping and evaluation;
- linguistic feature analysis.

### 4. Out-of-Scope Uses

The dataset should not be treated as authoritative evidence for:

- population-level slang frequency;
- prevalence among Indonesian speakers;
- precise regional language frequency;
- a speaker's geographic location or identity;
- demographic inference;
- psychological profiling;
- real-world quotation attribution;
- historical first-use claims.

### 5. Data Composition

Each record currently contains five primary fields:

```text
id
konteks_percakapan
ragam_slang
sentimen_emosi
lokasi_dominan
```

The current release contains **20,000 records**, with identifiers spanning:

```text
ID-NLP-0001
...
ID-NLP-20000
```

Primary dataset file:

```text
dataset/dataset_slang_indonesia.json
```

Detailed field definitions are provided in:

```text
DATA_DICTIONARY.md
```

### 6. Regional and Contextual Metadata

`lokasi_dominan` represents the contextual or regional association assigned to a synthetic example.

It must not be interpreted as verified speaker origin, residence, identity, or precise geographic information.

Supporting regional information is available under:

```text
linguistic_clusters/regional_clusters.json
```

### 7. Synthetic Data Considerations

Synthetic records can be useful for controlled NLP experimentation, but they may contain artifacts that differ from naturally occurring language.

In particular:

- record frequency is not real-world frequency;
- regional labels are contextual annotations, not verified speaker locations;
- synthetic contexts may not represent all community usage;
- slang meanings can vary by context;
- language changes over time.

For production systems, users should perform independent evaluation against appropriate external or human-reviewed data.

### 8. Quality and Validation

The repository includes automated validation and quality-audit tooling.

Relevant components include:

```text
validation/
quality/
reports/
schema/
annotations/
```

Automated validation checks structural and predefined quality properties. Passing validation does not guarantee perfect linguistic naturalness or semantic correctness.

### 9. Limitations and Bias

The dataset is not intended to represent Indonesian informal language exhaustively or with equal regional, demographic, generational, or community coverage.

Synthetic generation can introduce biases related to vocabulary selection, topic distribution, template patterns, annotation conventions, and regional representation.

Users should assess these limitations for their intended application.

### 10. Privacy

The dataset is designed as synthetic data and is not intended to contain real private conversations or personally identifiable information.

Users remain responsible for their own privacy, security, legal, regulatory, and fitness-for-purpose review.

### 11. Versioning

The current release is:

```text
v1.0.0
```

Future releases should use explicit version numbers and should not silently overwrite the contents of an existing release.

Changes should be documented in:

```text
CHANGELOG.md
```

### 12. Licensing

Dataset usage is governed by:

```text
DATASET_LICENSE.md
```

Repository source code is licensed separately under:

```text
LICENSE
```

The public repository does not by itself grant rights beyond the applicable dataset license.

For commercial use, redistribution, enterprise deployment, or other licensing questions, review the applicable license and contact the project owner.

### 13. Citation

Please cite the project when using this dataset in research, benchmarks, demonstrations, or public work.

Citation metadata is provided in:

```text
CITATION.cff
```

### 14. Related Documentation

```text
README.md
DATA_DICTIONARY.md
DATASET_LICENSE.md
CHANGELOG.md
CITATION.cff
```

Technical resources:

```text
schema/
annotations/
linguistic_taxonomy/
linguistic_clusters/
validation/
quality/
reports/
```

### 15. Dataset Status

**Status:** Active Development

**Current Release:** `v1.0.0`

**Records:** **20,000**

The current release establishes the initial structured synthetic corpus. Future releases may expand coverage, annotations, formats, validation, and evaluation resources.
