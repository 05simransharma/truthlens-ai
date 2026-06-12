# USER MANUAL

# TruthLens AI

## Introduction

TruthLens AI is an AI-powered Trust and Risk Intelligence Platform that helps users analyze contracts and evaluate the credibility of news articles using Google Gemini AI.

The application provides contract summaries, risk assessments, credibility evaluations, bias detection, and actionable insights.

TruthLens AI follows a Bring Your Own Key (BYOK) model, allowing users to securely provide their own Gemini API key during runtime.

---

# System Requirements

## Hardware Requirements

* Computer or Laptop
* Internet Connection

## Software Requirements

* Python 3.10+
* Streamlit
* Google Gemini API Key
* uv (recommended) or pip

---

# Installation Guide

## Step 1: Clone the Repository

```bash
git clone <repository-url>
cd truthlens-ai
```

## Step 2: Install Dependencies

Using uv:

```bash
uv sync
```

---

## Step 3: Launch the Application

```bash
uv run streamlit run app.py
```

The application will automatically open in your browser.

---

# Using TruthLens AI

## Step 1

Launch the application.

## Step 2

- AI Configuration

1. Enter your Gemini API Key in the sidebar.
2. Select your preferred language.
3. Choose an analyzer.
4. Generate AI-powered insights.

## Step 3

Choose one of the available modules:

* Contract Risk Analyzer
* News Credibility Analyzer

## Step 4

Upload a contract PDF or paste a news article.

## Step 5

Click the Analyze button.

## Step 6

Review the AI-generated analysis report.

---

# Contract Risk Analyzer

## Purpose

The Contract Risk Analyzer helps users understand legal contracts by generating summaries, identifying risks, and highlighting obligations.

## Outputs

* Executive Summary
* Risk Assessment
* High-Risk Clauses
* Medium-Risk Clauses
* User Obligations
* Recommendations

---

# News Credibility Analyzer

## Purpose

The News Credibility Analyzer evaluates the reliability and credibility of news articles.

## Outputs

* Main Claims
* Bias Analysis
* Credibility Assessment
* Information Gaps
* Final Verdict

---

# Features

* AI-powered contract analysis
* News credibility evaluation
* Automated summarization
* Risk identification
* Bias detection
* Bring Your Own Key (BYOK)
* Interactive user interface
* Fast analysis results
* Multi-Language Support

---

# Troubleshooting

## Invalid API Key

### Problem

Authentication failed while connecting to Gemini.

### Solution

* Verify that the API key is valid.
* Ensure the key was generated from Google AI Studio.
* Re-enter the API key in the sidebar.

---

## Quota Exceeded Error

### Problem

```text
429 ResourceExhausted
```

### Solution

* Wait for the Gemini quota reset period.
* Retry after a few moments.
* Use a different Gemini API key if available.

---

## PDF Upload Issues

### Problem

The PDF is not processed correctly.

### Solution

* Ensure the file is in PDF format.
* Verify that the PDF contains selectable text.
* Avoid scanned image-only PDFs.

---

# Limitations

* Results depend on AI-generated analysis.
* Very large contracts may require longer processing times.
* News credibility assessments should be treated as guidance rather than definitive judgments.

---

# Future Improvements

* Real-time fact checking
* Social media content verification
* Browser extension integration
* Advanced risk scoring dashboard
* Multi-model AI support

---

## Multilingual Support

TruthLens AI supports the following languages:

* English
* Hindi
* Telugu

To change the language:

1. Open the sidebar.
2. Select your preferred language.
3. The interface updates automatically.

---

# Support

For issues, improvements, or contributions, please refer to the project repository documentation.

---

# Version

TruthLens AI v1.0

Hackathon Prototype Release
