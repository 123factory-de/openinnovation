# Commit Message Convention

This project follows the **Conventional Commits** specification for clear and automated versioning.

## Format
```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Types

| Type | Description |
| :--- | :--- |
| **feat** | A new feature |
| **fix** | A bug fix |
| **docs** | Documentation only changes |
| **style** | Changes that do not affect the meaning of the code (white-space, formatting, etc) |
| **refactor** | A code change that neither fixes a bug nor adds a feature |
| **perf** | A code change that improves performance |
| **test** | Adding missing tests or correcting existing tests |
| **build** | Changes that affect the build system or external dependencies |
| **ci** | Changes to our CI configuration files and scripts |
| **chore** | Other changes that don't modify src or test files |
| **revert** | Reverts a previous commit |

## Examples

- `feat: add initial homepage layout`
- `fix: resolve timeout issue with API requests`
- `docs: update branching strategy documentation`
- `refactor(navigation): simplify header menu logic`
- `chore: update dependencies in package.json`

## Rules

1. **Use the imperative mood** in the description (e.g., "add" instead of "added").
2. **Limit the subject line to 50 characters.**
3. **Do not end the subject line with a period.**
4. Use the body to explain **what** and **why** vs. **how**.
