Pre-commit hook template
========================

This repo is a template for a [pre-commit hook](https://pre-commit.com/).

Try it out by running:

```bash
pre-commit try-repo https://github.com/stefsmeets/pre-commit-hook-template/ --all-files
```

## Installing it as a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions.

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/stefsmeets/pre-commit-hook-template/
    rev: v1.0.1
    hooks:
    -   id: yourhook
```
