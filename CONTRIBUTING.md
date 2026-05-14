# Contributing to RedlineOS

Thank you for your interest in contributing. RedlineOS is an open-source project and all contributions — bug reports, feature suggestions, documentation, and code — are welcome.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Development Workflow](#development-workflow)
- [Code Style](#code-style)
- [Commit Messages](#commit-messages)
- [Pull Request Guidelines](#pull-request-guidelines)

---

## Code of Conduct

Be respectful and constructive. Harassment or exclusionary behavior of any kind will not be tolerated.

---

## Getting Started

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/RedlineOS.git
   cd RedlineOS
   ```
3. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. Run the app to confirm everything works:
   ```bash
   python main.py
   ```

---

## Reporting Bugs

Open an issue and include:

- A clear description of the problem
- Steps to reproduce it
- Expected vs. actual behavior
- Your OS, Python version, and PySide6 version

---

## Suggesting Features

Open an issue with the `enhancement` label. Describe the use case, not just the feature — explaining *why* something is needed helps prioritize it correctly. For large features, open a discussion before writing code so the approach can be agreed on first.

---

## Development Workflow

1. Create a branch from `main`:
   ```bash
   git checkout -b feature/short-description
   ```
2. Make your changes in focused, logical commits (see [Commit Messages](#commit-messages)).
3. Test your changes manually and, where applicable, add or update automated tests.
4. Push your branch and open a pull request against `main`.

---

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/).
- Use `black` for formatting and `ruff` for linting (configuration in `pyproject.toml` once added).
- Name things clearly — prefer readable names over abbreviations.
- Keep functions small and single-purpose.

---

## Commit Messages

Use the imperative mood and keep the subject line under 72 characters:

```
Add freehand pen tool to drawing canvas
Fix crash when opening password-protected PDFs
Update CAD symbol library with ISO 128 shapes
```

For non-trivial changes, add a short body after a blank line explaining *why*, not just *what*.

---

## Pull Request Guidelines

- Keep PRs focused — one feature or fix per PR.
- Reference any related issues in the PR description (e.g., `Closes #42`).
- Make sure the app runs without errors before submitting.
- Be responsive to review feedback; PRs inactive for 30 days may be closed.

---

## License

By contributing to RedlineOS, you agree that your contributions will be licensed under the [MIT License](LICENSE).
