# Dataset Card

## Indonesian Casual Language & Slang Synthetic Dataset

---

## 1. Dataset Summary

**Name:** Indonesian Casual Language & Slang Synthetic Dataset

**Repository:** `e17do/id-slang-synthetic-nlp`

**Current Version:** `v1.0.0`

**Number of Records:** 20,000

**Primary Language:** Indonesian (`id`)

**Data Type:** Synthetic

**Primary Domain:** Indonesian informal language, slang, conversational language, and related linguistic expressions.

This dataset is designed as a structured resource for research, experimentation, data augmentation, and development of NLP and AI systems that need to process Indonesian informal and conversational language.

---

## 2. Dataset Description

Indonesian language used in informal environments can differ substantially from formal written Indonesian.

Examples may include:

* slang;
* abbreviations;
* internet expressions;
* casual vocabulary;
* conversational patterns;
* social-media language;
* Indonesian-English code-switching;
* community-associated expressions;
* regional language variations;
* informal emotional expressions.

This dataset provides synthetic examples intended to represent a range of these phenomena in structured form.

Each record combines a conversational context with metadata describing the associated slang or informal expression, sentiment/emotion annotation, and dominant contextual or regional association.

---

## 3. Motivation

The project was created to provide an accessible structured resource for experimentation with Indonesian informal language.

Many NLP resources focus primarily on formal Indonesian text. However, real-world AI systems frequently encounter informal language through:

* social media;
* messaging;
* online communities;
* gaming;
* customer communication;
* creator platforms;
* e-commerce;
* workplace communication;
* online discussions.

The project aims to make Indonesian informal-language experimentation easier while maintaining clear documentation about the synthetic nature and limitations of the data.

---

## 4. Intended Uses

The dataset may be useful for:

### NLP Research

* slang classification;
* informal-language classification;
* sentiment analysis;
* emotion classification;
* text classification;
* linguistic analysis;
* vocabulary analysis.

### AI Development

* conversational AI experiments;
* data augmentation;
* model prototyping;
* fine-tuning experiments;
* language understanding research;
* Indonesian-language model evaluation.

### Linguistic Research

* Indonesian informal-language exploration;
* slang categorization;
* regional/contextual variation analysis;
* code-switching research;
* informal communication research.

### Education

* NLP demonstrations;
* student projects;
* classroom experiments;
* Indonesian computational-linguistics exercises.

---

## 5. Out-of-Scope Uses

The dataset should not be treated as an authoritative source for:

* population-level linguistic statistics;
* prevalence of slang among Indonesian speakers;
* precise regional language frequency;
* demographic inference;
* identification of real individuals;
* psychological profiling;
* identification of a person's geographic location;
* real-world quotation attribution.

The dataset should also not be used as the sole source of truth for high-impact or safety-critical decisions.

---

## 6. Data Collection and Generation

The current dataset is synthetic.

The records were generated and structured for NLP experimentation rather than collected as a direct transcription of real-world conversations.

The project uses structured fields and supporting annotation/taxonomy resources to organize the generated records.

The repository includes supporting tooling for:

* schema validation;
* annotation;
* quality auditing;
* linguistic taxonomy;
* regional/contextual clustering.

Relevant project directories include:

```text
annotations/
linguistic_taxonomy/
linguistic_clusters/
quality/
validation/
schema/
reports/
```

---

## 7. Data Composition

Each record currently contains five primary fields:

```text
id
konteks_percakapan
ragam_slang
sentimen_emosi
lokasi_dominan
```

### `id`

Unique identifier for the record.

### `konteks_percakapan`

Synthetic conversational context containing the relevant informal-language usage.

### `ragam_slang`

The slang, informal expression, abbreviation, internet expression, or related linguistic feature represented by the record.

### `sentimen_emosi`

Sentiment or emotional annotation associated with the context.

### `lokasi_dominan`

Dominant geographic, demographic, community, or contextual association assigned to the example.

For detailed field definitions, see:

`DATA_DICTIONARY.md`

---

## 8. Dataset Size

The current `v1.0.0` release contains:

**20,000 records**

The record identifiers span the current dataset range:

```text
ID-NLP-0001
...
ID-NLP-20000
```

The dataset is distributed as a structured JSON file.

Primary dataset:

```text
dataset/dataset_slang_indonesia.json
```

---

## 9. Synthetic Data Considerations

Because the dataset is synthetic, users should consider the following:

1. Synthetic examples may not perfectly reproduce naturally occurring language.
2. The frequency of an expression in the dataset does not represent its real-world frequency.
3. Regional associations do not establish actual geographic usage rates.
4. Synthetic contexts may contain linguistic patterns that are uncommon or artificial.
5. Slang evolves over time and may become outdated.
6. Some expressions may have multiple meanings depending on context.
7. Annotation quality should be evaluated according to the intended downstream task.

For production systems, the dataset should ideally be evaluated against appropriate real-world or human-reviewed data.

---

## 10. Linguistic Diversity

The dataset aims to cover multiple forms of Indonesian informal communication.

Potential linguistic areas include:

* casual Indonesian;
* internet slang;
* social-media language;
* youth-oriented expressions;
* gaming terminology;
* workplace casual language;
* relationship/friendship expressions;
* e-commerce terminology;
* financial and fintech language;
* creator-economy terminology;
* cryptocurrency terminology;
* Indonesian-English code-switching;
* regional/context-associated language.

Coverage is not intended to imply equal representation of every Indonesian region, demographic group, community, or linguistic variety.

---

## 11. Regional Information

The `lokasi_dominan` field provides contextual or regional association.

It should not be interpreted as precise geographic metadata.

In particular, it does not establish:

* the location of a real speaker;
* the residence of a person;
* the identity of a person;
* the exact origin of an expression.

Regional information is provided primarily to support linguistic and contextual experimentation.

Additional regional organization is available under:

```text
linguistic_clusters/regional_clusters.json
```

---

## 12. Annotation

The current dataset contains annotation information associated with the conversational context.

The primary annotation field is:

```text
sentimen_emosi
```

The current release preserves the original annotation structure of `v1.0.0`.

Future releases may introduce more granular annotation dimensions, such as:

* sentiment;
* emotion;
* intent;
* attitude;
* register;
* linguistic function.

Such changes should be introduced through versioned releases rather than silently modifying the current dataset.

---

## 13. Data Quality

The repository includes automated validation and quality-audit tooling.

Validation may include checks related to:

* schema compliance;
* required fields;
* ID structure;
* unique identifiers;
* duplicate contexts;
* missing values;
* dataset consistency.

Relevant directories:

```text
validation/
quality/
reports/
```

Automated validation should not be interpreted as proof that every record is linguistically natural or semantically correct.

Automated checks primarily evaluate structural and predefined quality properties.

---

## 14. Known Limitations

The current release has several limitations.

### Synthetic Nature

The dataset is synthetic and therefore may contain generated expressions that do not perfectly correspond to naturally occurring conversations.

### Annotation Limitations

Annotations may contain ambiguity because sentiment and emotion can depend heavily on context.

### Regional Limitations

Regional associations should not be interpreted as comprehensive representations of Indonesian regional language.

### Temporal Limitations

Slang changes rapidly. Expressions that are common today may become less common or change meaning over time.

### Coverage Limitations

The dataset should not be considered an exhaustive representation of Indonesian informal language.

### Validation Limitations

Automated validation cannot replace expert or human linguistic review.

---

## 15. Bias and Representation

Synthetic generation can introduce biases related to:

* generation patterns;
* topic distribution;
* vocabulary selection;
* regional coverage;
* demographic assumptions;
* annotation conventions.

Users should evaluate these factors before applying the dataset to downstream systems.

A model trained on this dataset may reproduce or amplify patterns present in the synthetic data.

For applications where fairness or demographic performance is important, additional evaluation using appropriate real-world datasets is recommended.

---

## 16. Privacy

The dataset is designed as synthetic data and is not intended to contain real personal conversations or personally identifiable information.

However, users should not assume that synthetic data automatically eliminates all legal or privacy considerations.

Organizations remain responsible for conducting appropriate:

* privacy reviews;
* security reviews;
* legal reviews;
* regulatory assessments;
* risk assessments.

---

## 17. Recommended Evaluation

For serious NLP development, users are encouraged to evaluate models using data outside the training dataset.

A recommended workflow is:

```text
Synthetic Dataset
        ↓
Training / Experimentation
        ↓
Model
        ↓
External Evaluation Dataset
        ↓
Human or Real-World Validation
        ↓
Production Assessment
```

Evaluation against only synthetic test data may overestimate real-world performance.

---

## 18. Recommended Data Splitting

The dataset does not prescribe one universal train/test split.

Users should create task-specific splits appropriate to their objectives.

When creating splits, consider:

* duplicate prevention;
* lexical leakage;
* label distribution;
* linguistic diversity;
* regional/contextual diversity;
* random seed reproducibility.

For serious benchmarking, an independent evaluation set is recommended.

---

## 19. Ethical Considerations

Users should consider the potential consequences of models trained on informal-language data.

Particular attention should be paid to:

* dialect and regional variation;
* slang interpretation;
* sarcasm;
* humor;
* offensive language;
* ambiguity;
* code-switching;
* context-dependent meaning.

A model should not automatically treat slang or regional language as an indicator of negative behavior, low quality, or undesirable user characteristics.

---

## 20. Security Considerations

The dataset may contain informal expressions that could include offensive, provocative, or context-sensitive language.

Users integrating the dataset into applications should implement appropriate:

* filtering;
* moderation;
* input validation;
* access controls;
* logging;
* safety policies.

The dataset should not be assumed to be safe for direct display to end users without application-level controls.

---

## 21. Maintenance

The project is actively maintained as an evolving Indonesian NLP data resource.

Future releases may include:

* additional records;
* improved metadata;
* expanded linguistic coverage;
* improved annotations;
* quality improvements;
* human validation;
* benchmark datasets;
* additional file formats;
* improved regional coverage.

Changes should be documented in:

`CHANGELOG.md`

Released versions should remain identifiable so that research and applications can reference a specific dataset version.

---

## 22. Versioning Policy

The current dataset is:

`v1.0.0`

Future releases should use explicit version numbers.

Examples:

```text
v1.0.0
v1.1.0
v1.2.0
v2.0.0
```

Major structural changes should be associated with a major version where appropriate.

The original `v1.0.0` dataset should remain identifiable as a historical release.

---

## 23. Licensing

Dataset usage is governed by:

`DATASET_LICENSE.md`

The repository source code is licensed separately under:

`LICENSE`

Users should review the applicable license before:

* commercial use;
* redistribution;
* sublicensing;
* derivative dataset creation;
* enterprise deployment.

Commercial access may be available under a separate agreement.

---

## 24. Commercial and Enterprise Access

The public dataset is intended to provide a foundation for research and experimentation.

Additional commercial offerings may be developed in the future, potentially including:

* commercial training rights;
* enterprise access;
* larger datasets;
* extended annotations;
* custom datasets;
* domain-specific datasets;
* custom linguistic categories;
* private data packages;
* production-use licensing;
* redistribution rights where explicitly negotiated.

Commercial rights are not automatically granted by access to the public repository.

For commercial licensing, enterprise access, partnerships, custom dataset development, or other inquiries, contact the project owner.

**Project owner:** `e17do`

**GitHub:**
`https://github.com/e17do`

**Repository:**
`https://github.com/e17do/id-slang-synthetic-nlp`

**Email:**
See the contact email published in `README.md`.

---

## 25. Citation

If you use this dataset in research, publications, benchmarks, demonstrations, or other publicly presented work, please provide attribution.

Project:

**Indonesian Casual Language & Slang Synthetic Dataset**

Repository:

`e17do/id-slang-synthetic-nlp`

See:

`CITATION.cff`

for the project's citation metadata.

---

## 26. Related Documentation

For additional information, see:

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

---

## 27. Dataset Status

**Status:** Active Development

**Current Release:** `v1.0.0`

**Records:** 20,000

The current release establishes the initial structured synthetic corpus.

The project roadmap focuses on improving:

* documentation;
* data quality measurement;
* linguistic validation;
* benchmarking;
* evaluation;
* annotation depth;
* production usability;
* commercial licensing options.

---

## 28. Disclaimer

This dataset is provided as a research and development resource.

Users are responsible for determining whether the dataset is suitable for
their intended application.

The dataset creator makes no guarantee that the dataset is:

* complete;
* error-free;
* representative of all Indonesian speakers;
* representative of all Indonesian regions;
* suitable for every NLP task;
* suitable for production deployment.

Production systems should undergo appropriate independent evaluation,
testing, safety assessment, and legal review.

---

## 29. Summary

The Indonesian Casual Language & Slang Synthetic Dataset provides a
20,000-record structured synthetic corpus focused on Indonesian
informal and conversational language.

Its primary purpose is to support:

* Indonesian NLP research;
* AI experimentation;
* conversational-language understanding;
* slang analysis;
* data augmentation;
* classification experiments;
* future benchmarking and model development.

The dataset is intentionally maintained as a versioned resource so that
future improvements can be introduced without silently changing the
existing `v1.0.0` release.
