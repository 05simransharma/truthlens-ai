# CONTRIBUTING

Thank you for your interest in contributing to TruthLens AI.

This document provides guidelines for contributing to the project.

---

# Code of Conduct

Contributors are expected to:

* Be respectful and professional.
* Provide constructive feedback.
* Collaborate openly and responsibly.
* Follow project standards and guidelines.

---

# Getting Started

## 1. Fork the Repository

Create your own copy of the repository.

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd truthlens-ai
```

---

## 2. Install Dependencies

Using uv:

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

---

## 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## 4. Run the Application

```bash
uv run streamlit run app.py
```

---

# Development Workflow

## Create a Branch

Before making changes, create a new branch:

```bash
git checkout -b feature-name
```

Example:

```bash
git checkout -b improve-news-analysis
```

---

## Make Changes

Possible contribution areas include:

* User Interface improvements
* AI prompt optimization
* Contract analysis enhancements
* News credibility evaluation improvements
* Documentation updates
* Bug fixes
* Performance optimization

---

## Commit Changes

Use clear and descriptive commit messages.

Example:

```bash
git commit -m "Improved contract risk analysis"
```

---

## Push Changes

```bash
git push origin feature-name
```

---

## Submit a Pull Request

Create a Pull Request describing:

* What changes were made
* Why the changes were made
* Any testing performed

---

# Project Structure

```text
truthlens-ai/
│
├── app.py
│
├── modules/
│   ├── contract_analyzer.py
│   └── news_analyzer.py
│
├── utils/
│   ├── gemini_client.py
│   └── pdf_loader.py
│
├── README.md
├── USER_MANUAL.md
├── SYSTEM_ARCHITECTURE.md
├── PROJECT_REPORT.md
├── CONTRIBUTING.md
├── pyproject.toml
└── uv.lock
```

---

# Coding Guidelines

* Follow Python best practices.
* Write readable and maintainable code.
* Use meaningful variable and function names.
* Keep modules focused on a single responsibility.
* Document significant changes.

---

# Reporting Issues

When reporting issues, include:

* Steps to reproduce the problem
* Expected behavior
* Actual behavior
* Error messages (if any)
* Environment details

---

# Feature Requests

Feature requests should include:

* Problem description
* Proposed solution
* Expected impact
* Implementation ideas (optional)

---

# Acknowledgements

We appreciate all contributors who help improve TruthLens AI.

Your contributions help make information analysis more accessible and reliable.

---

# Project

TruthLens AI

Version 1.0
