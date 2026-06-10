# USER MANUAL

# TruthLens AI

## Introduction

TruthLens AI is an AI-powered trust and risk intelligence platform that helps users analyze contracts and assess the credibility of news articles using Google's Gemini AI.

The application provides simplified summaries, risk assessments, credibility evaluations, and actionable insights to help users make informed decisions.

---

# System Requirements

## Hardware Requirements

* Computer/Laptop
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

Or using pip:

```bash
pip install -r requirements.txt
```

## Step 3: Configure Environment Variables

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

## Step 4: Launch the Application

```bash
uv run streamlit run app.py
```

The application will open automatically in your default browser.

---

# Application Modules

## 1. Contract Risk Analyzer

### Purpose

The Contract Risk Analyzer helps users understand legal contracts by generating summaries, identifying risks, and highlighting obligations.

### Steps to Use

1. Open the application.
2. Navigate to the **Contract Risk Analyzer** tab.
3. Click **Upload Contract PDF**.
4. Select a PDF contract file.
5. Click **Analyze Contract**.
6. Wait for the AI analysis to complete.

### Output

The application generates:

* Executive Summary
* Risk Assessment
* High-Risk Clauses
* Medium-Risk Clauses
* User Obligations
* Recommendations

---

## 2. News Credibility Analyzer

### Purpose

The News Credibility Analyzer evaluates the reliability and credibility of news articles.

### Steps to Use

1. Open the application.
2. Navigate to the **News Credibility Analyzer** tab.
3. Paste the news article into the text area.
4. Click **Analyze News**.
5. Wait for the AI analysis to complete.

### Output

The application generates:

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
* User-friendly interface
* Fast analysis results

---

# Troubleshooting

## API Key Error

Problem:

```text
GOOGLE_API_KEY not found
```

Solution:

* Verify that the `.env` file exists.
* Ensure the API key is correctly configured.

---

## Quota Exceeded Error

Problem:

```text
429 ResourceExhausted
```

Solution:

* Wait for the quota reset period.
* Retry after a few seconds.

---

## PDF Upload Issues

Problem:

PDF is not processed correctly.

Solution:

* Ensure the file is in PDF format.
* Verify that the PDF contains selectable text.

---

# Limitations

* Results depend on AI-generated analysis.
* Very large contracts may require longer processing times.
* News credibility assessments should be used as guidance rather than definitive judgments.

---

# Future Improvements

* Real-time fact checking
* Multi-language support
* Social media content verification
* Browser extension integration
* Advanced risk scoring dashboard

---

# Support

For issues, improvements, or contributions, please refer to the project repository documentation.

---

# Version

TruthLens AI v1.0

Hackathon Prototype Release
