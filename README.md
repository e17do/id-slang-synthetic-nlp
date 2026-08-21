# id-slang-synthetic-nlp

**Indonesian Casual Language & Slang Synthetic Dataset for NLP and AI**

A structured synthetic dataset of Indonesian informal language, slang, internet expressions, conversational patterns, regional/context-associated language styles, and Indonesian-English code-switching for NLP research, machine learning, and AI development.

> **Current release:** `v1.0.0`  
> **Dataset size:** **20,000 records**  
> **Primary language:** Indonesian (`id`)  
> **Data type:** Synthetic  
> **Repository:** `e17do/id-slang-synthetic-nlp`

---

## About

`id-slang-synthetic-nlp` is a structured synthetic resource focused on Indonesian informal and conversational language.

It is designed for experimentation involving:

- Indonesian slang classification;
- informal-language classification;
- sentiment and emotion experiments;
- conversational AI;
- text classification;
- slang normalization research;
- intent-related experiments;
- code-switching research;
- regional/contextual language analysis;
- data augmentation;
- Indonesian NLP experimentation;
- language-model development and evaluation.

The dataset is **synthetic** and is not intended to be a statistically representative model of all Indonesian speakers, regions, communities, or linguistic varieties.

---

## Dataset Overview

| Attribute | Value |
|---|---|
| Current version | `v1.0.0` |
| Records | **20,000** |
| ID range | `ID-NLP-0001` – `ID-NLP-20000` |
| Primary language | Indonesian (`id`) |
| Data type | Synthetic |
| Main format | JSON |
| Schema | `schema/dataset_schema.json` |
| Unique IDs | Yes |
| Validation tooling | Included |
| Quality audit | Included |
| Dataset license | See `DATASET_LICENSE.md` |
| Code license | MIT |

---

## Dataset Structure

The current release contains five core fields per record:

```json
{
  "id": "ID-NLP-0001",
  "konteks_percakapan": "Contoh kalimat percakapan kasual.",
  "ragam_slang": "contoh slang",
  "sentimen_emosi": "Positif",
  "lokasi_dominan": "Urban Indonesia"
}
```

Detailed definitions are available in `DATA_DICTIONARY.md`.

The machine-readable contract is defined in:

```text
schema/dataset_schema.json
```

---

## Linguistic Coverage

The dataset is designed to cover a range of Indonesian informal-language contexts, including:

- Indonesian internet slang;
- casual conversational language;
- social-media expressions;
- youth-oriented expressions;
- Indonesian-English code-switching;
- gaming language;
- workplace and professional casual language;
- relationship and friendship language;
- e-commerce language;
- fintech-related language;
- financial terminology;
- crypto terminology;
- creator-economy language;
- regional/context-associated language styles;
- urban Indonesian conversational patterns.

Supporting resources:

```text
linguistic_clusters/regional_clusters.json
linguistic_taxonomy/taxonomy.json
```

Coverage is not intended to imply equal representation of every region, community, generation, or domain.

---

## Example Use Cases

### NLP Classification

The dataset can support experiments involving:

- slang detection;
- informal-language classification;
- sentiment classification;
- emotion classification;
- conversational text classification.

### Conversational AI

Potential applications include systems that need to process:

- casual Indonesian;
- internet expressions;
- slang-heavy messages;
- informal conversations;
- Indonesian-English mixed language.

### Language Normalization

The dataset may be useful for research into normalization of informal Indonesian.

Example:

```text
Informal:
"Gue gak ngerti kenapa dia ghosting."

Possible normalized form:
"Saya tidak mengerti mengapa dia menghilang tanpa kabar."
```

A normalized output is application-dependent and is not asserted as the only correct transformation.

---

## Synthetic Data Notice

This is a **synthetic dataset**.

The records were generated for linguistic coverage and NLP experimentation rather than collected as direct transcripts of real-world conversations.

Therefore:

- records should not be interpreted as real conversations;
- record frequency should not be interpreted as population frequency;
- geographic/context labels do not identify a real person's location;
- synthetic examples may contain generation artifacts;
- examples may not perfectly represent how a particular community speaks;
- production users should perform independent evaluation against appropriate external or human-reviewed data.

For provenance details, see:

```text
docs/DATA_PROVENANCE.md
```

For known limitations, see:

```text
docs/KNOWN_LIMITATIONS.md
```

---

## Privacy & PII

The dataset is designed as synthetic data and is not intended to contain real private conversations or personally identifiable information.

Synthetic status is not a universal legal guarantee. Users remain responsible for their own privacy, security, legal, regulatory, and fitness-for-purpose review.

---

## Quality Control

The repository includes validation and quality-audit tooling.

Validation infrastructure includes checks related to:

- JSON/schema validity;
- required fields;
- ID format;
- unique identifiers;
- missing fields;
- duplicate contexts;
- annotation structure;
- dataset consistency.

Relevant directories:

```text
validation/
quality/
reports/
```

Passing automated validation does **not** guarantee that every record is linguistically natural or semantically correct.

---

## Repository Structure

```text
id-slang-synthetic-nlp/
│
├── README.md
├── LICENSE
├── DATASET_LICENSE.md
├── DATASET_CARD.md
├── DATA_DICTIONARY.md
├── CHANGELOG.md
├── CITATION.cff
│
├── docs/
│   ├── DATA_PROVENANCE.md
│   └── KNOWN_LIMITATIONS.md
│
├── dataset/
│   └── dataset_slang_indonesia.json
│
├── annotations/
│   ├── annotation_schema.json
│   ├── generate_annotations.py
│   └── record_annotations.json
│
├── linguistic_clusters/
│   └── regional_clusters.json
│
├── linguistic_taxonomy/
│   └── taxonomy.json
│
├── quality/
│   ├── README.md
│   └── audit.py
│
├── reports/
│   └── dataset_quality_report.json
│
├── schema/
│   └── dataset_schema.json
│
└── validation/
    ├── README.md
    └── validator.py
```

---

## Versioning

The current published release is:

```text
v1.0.0
```

It contains **20,000 records**.

Future releases may add records, annotations, metadata, formats, validation, and quality improvements.

Published releases should remain identifiable and should not be silently overwritten.

All material changes should be documented in:

```text
CHANGELOG.md
```

---

## Quality and Release Practice

A future release should be treated as a versioned artifact rather than simply a larger JSON file.

Recommended release flow:

```text
Dataset update
      ↓
Schema validation
      ↓
Duplicate / consistency checks
      ↓
Quality audit
      ↓
Documentation update
      ↓
Versioned release
      ↓
Checksum / integrity verification
```

The repository includes supporting documentation for provenance and limitations.

---

## Commercial Licensing & Access

The public repository provides access to the published dataset under the terms stated in:

```text
DATASET_LICENSE.md
```

The repository's source code is licensed separately under:

```text
LICENSE
```

Access to the public repository should not be interpreted as granting rights beyond the applicable dataset license.

For commercial use, enterprise deployment, redistribution, custom datasets, or other licensing arrangements, review the applicable license and contact the project owner.

Potential future commercial offerings may include:

- larger datasets;
- extended annotations;
- domain-specific datasets;
- custom dataset development;
- production-use licensing;
- enterprise access;
- negotiated redistribution rights.

Commercial offerings are not automatically included in the public community release.

---

## Citation

If you use this dataset in research, benchmarks, demonstrations, or other public work, please provide attribution.

Citation metadata:

```text
CITATION.cff
```

Project:

**Indonesian Casual Language & Slang Synthetic Dataset**

Repository:

`e17do/id-slang-synthetic-nlp`

---

## Roadmap

### v1.x

- improved label consistency;
- expanded metadata;
- additional quality checks;
- dataset statistics;
- JSONL and Parquet distributions;
- clearer annotation documentation;
- improved regional/contextual coverage.

### v2.x and beyond

- human linguistic evaluation;
- external real-world evaluation benchmarks where appropriate and legally available;
- stronger sentiment/emotion taxonomy;
- train/dev/test benchmark resources;
- baseline NLP benchmarks;
- quality scoring;
- expanded slang normalization resources;
- broader regional and community coverage.

The project is intended to evolve through versioned releases rather than silently modifying historical releases.

---

## Documentation

| Document | Purpose |
|---|---|
| `DATASET_CARD.md` | Dataset summary, intended use, limitations, and metadata |
| `DATA_DICTIONARY.md` | Formal field definitions and data-type contract |
| `DATASET_LICENSE.md` | Dataset licensing terms |
| `docs/DATA_PROVENANCE.md` | Provenance and synthetic-data policy |
| `docs/KNOWN_LIMITATIONS.md` | Known limitations and usage cautions |
| `CHANGELOG.md` | Version history |
| `CITATION.cff` | Citation metadata |

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

---

## Disclaimer

This dataset is provided as a research and development resource.

Users are responsible for determining whether it is suitable for their intended application.

The dataset creator does not guarantee that the dataset is:

- complete;
- error-free;
- representative of all Indonesian speakers;
- representative of all Indonesian regions;
- suitable for every NLP task;
- suitable for production deployment without additional evaluation.

Production systems should undergo appropriate independent evaluation, testing, safety assessment, and legal review.

---

## Current Status

**Status:** Active Development

**Release:** `v1.0.0`

**Records:** **20,000**

The current release establishes the initial structured synthetic corpus and its supporting validation, quality, and documentation infrastructure.
