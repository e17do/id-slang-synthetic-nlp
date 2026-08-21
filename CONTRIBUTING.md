# Contributing

Thank you for helping improve `id-slang-synthetic-nlp`.

## Scope

Contributions should improve dataset quality, documentation, validation, reproducibility, or tooling.

## Before Contributing

Please review:

- `README.md`
- `docs/DATA_DICTIONARY.md`
- `docs/DATA_PROVENANCE.md`
- `docs/KNOWN_LIMITATIONS.md`
- repository schema and validation workflows

## Data Contributions

Do not submit:

- private or confidential conversations;
- personal data without an appropriate legal basis;
- copied dictionary/database content where redistribution rights are unavailable;
- copyrighted material that is not permitted by its license;
- claims of regional or demographic origin without appropriate evidence.

Synthetic examples should be clearly distinguishable from claims about observed real-world usage.

## Quality Requirements

Contributions should:

1. preserve the existing schema;
2. use stable unique identifiers;
3. avoid duplicate records;
4. preserve valid JSON encoding;
5. pass repository validation;
6. document material changes;
7. avoid silently changing the meaning of existing fields.

## Pull Requests

Pull requests should explain:

- what changed;
- why it changed;
- whether the dataset schema changed;
- whether validation was run;
- whether documentation was updated.

For substantial dataset changes, include the intended release impact.

## Versioning

Do not rewrite an existing published release.

Material dataset or schema changes should be released under a new version.

## Maintainer Review

All contributions are subject to maintainer review.

A contribution may be rejected when provenance, licensing, quality, privacy, reproducibility, or schema compatibility cannot be established.
