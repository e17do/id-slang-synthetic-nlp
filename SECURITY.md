# Security Policy

## Scope

This policy covers security issues affecting the `id-slang-synthetic-nlp` repository, its automated workflows, release artifacts, and associated tooling.

## Reporting a Vulnerability

Please do not disclose security vulnerabilities publicly in an issue before the maintainer has had an opportunity to assess them.

Use GitHub's private vulnerability reporting or another private maintainer-approved channel when available.

Include:

- a clear description of the issue;
- affected file, workflow, or component;
- reproduction steps where applicable;
- potential impact;
- suggested mitigation if known.

Do not include passwords, access tokens, API keys, personal data, or other secrets in a report.

## Secrets

Never commit:

- GitHub tokens;
- API keys;
- passwords;
- private credentials;
- private datasets;
- confidential customer information.

If a secret is accidentally committed, revoke or rotate it immediately and notify the maintainer.

## Dataset Security and Privacy

Although this release is synthetic, contributors must not introduce private or confidential source material into the repository.

Regional, demographic, and linguistic annotations must not be used to expose or infer personal identity.

## Dependency and Workflow Security

Changes to GitHub Actions, scripts, dependencies, or release automation should be reviewed carefully.

Workflow changes should follow the principle of least privilege and should avoid unnecessary write permissions.

## Supported Releases

Security fixes should target the current maintained release.

Older releases may not receive fixes unless explicitly maintained.

## Disclosure

After remediation, the maintainer may document a security issue and its resolution in an appropriate release note without exposing sensitive information.
