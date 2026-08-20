# id-slang-synthetic-nlp

**Indonesian Casual Language & Slang Synthetic Dataset for NLP and AI**

A structured synthetic dataset of Indonesian informal language, slang, internet expressions, conversational patterns, regional language styles, and Indonesian-English code-switching for NLP research, machine learning, and AI development.

> **Current release:** `v1.0.0`
> **Dataset size:** **20,000 records**
> **Primary language:** Bahasa Indonesia
> **Data type:** Synthetic
> **Repository:** `e17do/id-slang-synthetic-nlp`

---

## 🇮🇩 Tentang Proyek

`id-slang-synthetic-nlp` adalah dataset sintetis terstruktur yang berfokus pada bahasa Indonesia informal, bahasa gaul, ekspresi internet, percakapan kasual, variasi regional, dan penggunaan bahasa campuran Indonesia–Inggris.

Dataset ini dibuat sebagai resource untuk eksperimen dan pengembangan sistem NLP/AI yang membutuhkan pemahaman terhadap bahasa Indonesia informal dan conversational language.

Beberapa area penggunaan yang ditargetkan meliputi:

* Indonesian slang classification
* sentiment analysis
* emotion classification
* conversational AI
* text classification
* slang normalization
* intent detection
* code-switching research
* regional language research
* data augmentation
* Indonesian NLP experimentation
* language-model development and evaluation

Dataset ini **bersifat sintetis** dan tidak dimaksudkan sebagai representasi statistik sempurna dari seluruh penutur, daerah, komunitas, atau variasi bahasa Indonesia.

---

## Dataset Overview

| Attribute               | Value                         |
| ----------------------- | ----------------------------- |
| Current version         | `v1.0.0`                      |
| Records                 | **20,000**                    |
| ID range                | `ID-NLP-001` – `ID-NLP-20000` |
| Primary language        | Indonesian                    |
| Data type               | Synthetic                     |
| Main format             | JSON                          |
| Schema                  | JSON Schema                   |
| Unique IDs              | Yes                           |
| Duplicate context check | Included in validation        |
| Validation tooling      | Included                      |
| Dataset license         | See `DATASET_LICENSE.md`      |
| Code license            | MIT                           |

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

### Fields

| Field                | Description                                                                          |
| -------------------- | ------------------------------------------------------------------------------------ |
| `id`                 | Unique sequential identifier for each record.                                        |
| `konteks_percakapan` | Synthetic Indonesian casual conversation or sentence.                                |
| `ragam_slang`        | Slang, internet expression, informal expression, idiom, or other linguistic feature. |
| `sentimen_emosi`     | Sentiment or emotional label associated with the context.                            |
| `lokasi_dominan`     | Dominant geographic, demographic, community, or linguistic context.                  |

The schema is defined in:

`schema/dataset_schema.json`

---

## Linguistic Coverage

The dataset is designed to cover a broad range of Indonesian informal-language contexts, including:

* Indonesian internet slang
* casual conversational language
* social media expressions
* youth-oriented expressions
* Indonesian-English code-switching
* gaming language
* workplace and professional casual language
* relationship and friendship language
* e-commerce language
* fintech-related language
* financial terminology
* crypto terminology
* creator-economy language
* regional and location-associated language styles
* urban Indonesian conversational patterns

Regional and contextual linguistic metadata is additionally represented through:

`linguistic_clusters/regional_clusters.json`

The project also maintains a linguistic taxonomy in:

`linguistic_taxonomy/taxonomy.json`

---

## Example Use Cases

### NLP Classification

The dataset can be used as a resource for experiments involving:

* slang detection
* informal-language classification
* sentiment classification
* emotion classification
* conversational intent classification
* text classification

### Conversational AI

Potential applications include experimentation with systems that need to understand:

* casual Indonesian
* internet expressions
* slang-heavy messages
* informal conversations
* Indonesian-English mixed language

### Language Normalization

The dataset may also be useful for research into transforming informal Indonesian into more standardized or normalized language.

Example:

```text
Informal:
"Gue gak ngerti kenapa dia ghosting."

Possible normalized form:
"Saya tidak mengerti mengapa dia menghilang tanpa kabar."
```

Normalization outputs are application-dependent and should not be interpreted as the only correct linguistic transformation.

---

## Synthetic Data Notice

This is a **synthetic dataset**.

The records are generated for linguistic coverage and NLP experimentation rather than collected as a direct transcription of real-world conversations.

Therefore:

* records should not be interpreted as real conversations;
* slang frequency must not be interpreted as population frequency;
* geographic labels do not identify the actual location of a person;
* synthetic expressions may contain generation artifacts;
* some expressions may not perfectly represent how a particular community speaks;
* the dataset should be evaluated against appropriate real-world or human-validated data before production use.

Synthetic data should be treated as a training or experimentation resource rather than as a definitive linguistic authority.

---

## Privacy & PII

The dataset is designed around synthetic generation and is intended to avoid real-world personally identifiable information (PII).

However, synthetic generation alone should not be interpreted as a universal legal guarantee.

Users and organizations remain responsible for conducting their own:

* privacy assessment
* security assessment
* legal review
* regulatory compliance review
* fitness-for-purpose assessment

according to their intended use and jurisdiction.

---

## Quality Control

The repository includes validation and quality-control tooling.

Current validation infrastructure includes checks related to:

* JSON/schema validity
* required fields
* ID format
* unique identifiers
* missing fields
* duplicate contexts
* dataset consistency
* annotation structure

Validation code is available under:

```text
validation/
```

Quality-audit tooling is available under:

```text
quality/
```

The project also maintains a machine-readable quality report under:

```text
reports/dataset_quality_report.json
```

### Important

Passing automated validation does **not** mean that every record is linguistically perfect.

Automated validation verifies structural and selected quality properties. Human linguistic evaluation and real-world benchmarking are planned as future quality improvements.

---

## Repository Structure

```text
id-slang-synthetic-nlp/
│
├── README.md
├── LICENSE
├── DATASET_LICENSE.md
├── CHANGELOG.md
├── CITATION.cff
├── .gitignore
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

Dataset releases use explicit version numbers.

### Current release

`v1.0.0`

This release contains the initial structured synthetic corpus with **20,000 records**.

Future releases may include:

* expanded datasets
* improved annotations
* additional metadata
* improved taxonomy
* human validation
* benchmark datasets
* additional formats
* improved regional coverage
* improved linguistic quality controls

Significant changes should be documented in:

`CHANGELOG.md`

Released versions should remain identifiable and should not be silently overwritten.

---

## Roadmap

The long-term goal is to develop this project into a high-quality Indonesian informal-language resource suitable for research and commercial AI/NLP development.

Planned improvements include:

### v1.x

* improved label consistency
* expanded metadata
* improved dataset statistics
* additional quality checks
* JSONL and Parquet distributions
* clearer annotation guidelines
* improved documentation

### v2.x

* human linguistic evaluation
* real-world evaluation benchmark
* stronger sentiment/emotion taxonomy
* train/dev/test splits
* baseline NLP benchmarks
* quality scoring per record
* improved slang normalization resources
* expanded regional and community coverage

### Future Commercial Releases

Potential commercial editions may provide additional capabilities such as:

* larger datasets
* commercial training rights
* production-use licensing
* extended annotations
* custom domain coverage
* custom dataset generation
* private datasets
* enterprise support
* negotiated redistribution rights
* specialized Indonesian NLP datasets

Commercial features are not automatically included in the public community release.

---

## Commercial Licensing & Access

The public repository does **not automatically grant commercial rights to the dataset**.

The dataset and source code are licensed separately.

### Code

Repository code is licensed under the MIT License.

See:

`LICENSE`

### Dataset

Dataset-specific rights are governed by:

`DATASET_LICENSE.md`

Commercial use may require a separate commercial license.

Examples of commercial use include:

* training a commercial AI model;
* fine-tuning a production model;
* incorporating the dataset into a commercial product;
* using the dataset for a paid AI/NLP service;
* internal enterprise model development;
* redistributing the dataset as part of a commercial product;
* creating a commercial derivative dataset where this dataset is a material component.

If you are interested in **commercial access, enterprise usage, licensing, custom datasets, extended annotations, or collaboration**, please contact the project owner.

### Contact

**Project owner:** `e17do`

**GitHub:**
https://github.com/e17do

**Repository:**
https://github.com/e17do/id-slang-synthetic-nlp

For licensing or commercial inquiries, please open an issue in the repository or contact the project owner through GitHub.

> A dedicated business email may be added to this section in a future release.

---

## Community / Research Use

Researchers, students, developers, and organizations are encouraged to inspect and experiment with the public repository according to the applicable dataset license.

If you use the dataset in:

* research
* publications
* benchmarks
* models
* demonstrations
* derivative research

please provide appropriate attribution and cite the project.

See `CITATION.cff`.

---

## Citation

If you use this dataset in research, publications, models, benchmarks, or derivative work, please cite the repository using the included `CITATION.cff`.

Project:

`e17do/id-slang-synthetic-nlp`

Title:

**Indonesian Casual Language & Slang Synthetic Dataset for NLP and AI**

---

## Limitations

This project has several important limitations.

1. The dataset is synthetic rather than a direct collection of naturally occurring conversations.
2. It should not be treated as a statistically representative corpus of Indonesian speakers.
3. Regional labels represent linguistic/contextual association and should not be interpreted as precise geographic identification.
4. Slang and informal language evolve rapidly.
5. Some labels and linguistic categories may be revised in future releases.
6. Automated validation cannot guarantee linguistic naturalness.
7. Production systems should be evaluated against appropriate real-world and human-reviewed data.
8. Users are responsible for assessing legal, privacy, safety, and regulatory requirements for their own applications.

---

## Contribution

Contributions are welcome when they improve the quality, reproducibility, documentation, or usefulness of the project.

Contributions should preserve:

* schema integrity
* unique identifiers
* dataset provenance
* reproducibility
* privacy-conscious practices
* linguistic quality
* documentation quality
* clear versioning

Before submitting a dataset-related change, contributors should run the available validation tools.

---

## License Summary

| Component       | License / Terms                       |
| --------------- | ------------------------------------- |
| Repository code | MIT License                           |
| Dataset         | `DATASET_LICENSE.md`                  |
| Schema          | Subject to repository licensing terms |
| Annotations     | Dataset-specific terms                |
| Documentation   | Repository licensing terms            |

**Dataset rights are separate from software/code rights.**

Please read `DATASET_LICENSE.md` before using the dataset.

---

## Project Status

**Status: Active Development**

`id-slang-synthetic-nlp` is an evolving Indonesian NLP data project.

The current `v1.0.0` release establishes the initial 20,000-record synthetic corpus and its supporting schema, annotation, taxonomy, validation, and quality infrastructure.

Future releases will focus on stronger linguistic validation, more consistent annotation, real-world evaluation, benchmarking, and commercial-grade dataset packaging.

---

## Contact / Licensing Inquiries

For questions regarding:

* commercial licensing
* enterprise access
* dataset usage
* custom dataset development
* custom annotations
* research collaboration
* partnership
* data licensing

please contact:

**e17do**

GitHub:
https://github.com/e17do/id-slang-synthetic-nlp

GitHub profile:
https://github.com/e17do

A dedicated business contact email: aljawi.fm@gmail.com
