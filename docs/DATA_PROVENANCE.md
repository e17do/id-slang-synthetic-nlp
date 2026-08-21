# Data Provenance

## 1. Purpose

This document describes the provenance, construction, and intended interpretation of the `id-slang-synthetic-nlp` dataset.

The dataset is intended to provide a structured research and NLP resource for Indonesian informal-language and slang patterns.

## 2. Dataset Origin

This release consists of synthetic Indonesian conversational examples generated for NLP research and evaluation.

The records are not presented as direct transcripts of private conversations and should not be interpreted as a corpus of verified real-world conversations.

Each record contains structured metadata describing the simulated linguistic context.

## 3. Record-Level Fields

The dataset currently uses the following core fields:

- `id` — unique record identifier.
- `konteks_percakapan` — simulated Indonesian conversational text.
- `ragam_slang` — target slang expression represented in the record.
- `sentimen_emosi` — categorical sentiment/emotion annotation.
- `lokasi_dominan` — regional or demographic context assigned to the record.

## 4. Synthetic Data Policy

Synthetic records are created for linguistic and NLP purposes.

Synthetic examples may represent plausible informal Indonesian usage without constituting evidence that a particular expression was actually used by a real speaker in the stated context or location.

Regional and demographic metadata should therefore be interpreted as dataset annotation/context, not as verified speaker origin or identity.

## 5. Provenance Interpretation

Provenance should be interpreted at the dataset and record-design level.

The presence of a slang expression in this dataset does not by itself establish:

- historical first use;
- geographic origin;
- ownership of an expression;
- prevalence in a population;
- current real-world frequency;
- exclusive association with a region or community.

Such claims require independent evidence.

## 6. Intended Use

Appropriate uses include:

- NLP experimentation;
- text classification;
- slang recognition;
- language normalization research;
- synthetic-data benchmarking;
- model evaluation;
- linguistic feature engineering;
- educational and research applications.

Commercial use should be evaluated against the repository license and any applicable third-party rights.

## 7. Quality and Validation

The repository uses automated validation workflows to detect structural and data-quality problems.

Validation confirms machine-checkable constraints. It does not guarantee that every linguistic interpretation is objectively correct.

## 8. Future Provenance Expansion

Future releases may add more explicit provenance fields, source classifications, evidence records, confidence levels, and versioned observations.

Backward compatibility should be considered when extending the dataset schema.

## 9. Important Distinction

This dataset is a synthetic linguistic resource.

It should not be marketed as a verified census, survey, or exhaustive representation of Indonesian informal language.
