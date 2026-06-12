# 🔍 TruthLens AI

## 🌐 Live Demo

https://truthlens-aigit-s14a.streamlit.app/

---

# Overview

TruthLens AI is an AI-powered Trust and Risk Intelligence Platform designed to help users make informed decisions by analyzing legal contracts and evaluating the credibility of news content.

The platform leverages Google's Gemini AI model to generate summaries, identify risks, detect bias, and provide actionable insights from complex documents and articles.

TruthLens AI supports **Bring Your Own Key (BYOK)**, allowing users to securely connect their own Gemini API credentials without storing sensitive keys on the platform.

The application also supports **Multilingual User Interfaces** in:

* English
* Hindi
* Telugu

---

# Problem Statement

In today's digital world, users are constantly exposed to:

* Complex legal contracts that are difficult to understand.
* Misleading or biased news articles.
* Information overload that makes verification challenging.

Many individuals lack the expertise or time required to carefully review such content before making important decisions.

---

# Solution

TruthLens AI simplifies information analysis through Generative AI by enabling users to:

* Analyze contracts and identify potential risks.
* Summarize lengthy legal documents.
* Evaluate the credibility of news articles.
* Detect possible bias and misinformation.
* Receive understandable recommendations.

---

# Features

## 📄 Contract Risk Analyzer

* Upload PDF contracts.
* Generate executive summaries.
* Identify risky clauses.
* Highlight user obligations.
* Provide recommendations and risk insights.

## 📰 News Credibility Analyzer

* Analyze news articles and reports.
* Extract major claims.
* Detect potential bias.
* Evaluate credibility.
* Generate AI-powered verdicts.

## 🔑 Bring Your Own Key (BYOK)

* Secure Gemini API integration.
* User-provided API keys.
* No permanent credential storage.
* User-controlled AI usage and quota management.

## 🌐 Multilingual Support

* English Interface
* Hindi Interface
* Telugu Interface
* Dynamic Language Switching
* Localized User Experience

---

# Tech Stack

## Frontend

* Streamlit

## Backend

* Python

## AI Model

* Google Gemini 2.5 Flash

## Libraries

* google-generativeai
* pypdf
* plotly

## Package Management

* uv

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
│   ├── translations.py
│   ├── gemini_client.py
│   └── pdf_loader.py
│
├── assets/
│
├── README.md
├── CONTRIBUTING.md
├── USER_MANUAL.md
├── SYSTEM_ARCHITECTURE.md
├── PROJECT_REPORT.md
├── AGENTS.md
│
├── pyproject.toml
└── uv.lock
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/05simransharma/truthlens-ai.git
cd truthlens-ai
```

## Install Dependencies

```bash
uv sync
```

---

# Running the Application

```bash
uv run streamlit run app.py
```

The application will launch in your default browser.

---

# Usage

## Step 1

Launch the application.

## Step 2

Enter your Gemini API Key in the sidebar.

## Step 3

Select your preferred language:

* English
* Hindi
* Telugu

## Step 4

Choose one of the available modules:

* Contract Risk Analyzer
* News Credibility Analyzer

## Step 5

Upload a contract PDF or paste a news article.

## Step 6

Click the Analyze button and review the generated insights.

---

# Application UI

## Home Page

![Home Page](assets/Homepage.png)

## Contract Analysis

![Contract Analyzer](assets/ContractAnalysis.png)

## News Analysis

![News Analyzer](assets/NewsAnalysis.png)

## Hindi Interface

![Hindi Interface](assets/HindiUI.png)

## Telugu Interface

![Telugu Interface](assets/TeluguUI.png)

---

# Documentation

Additional project documentation is available:

* USER_MANUAL.md
* SYSTEM_ARCHITECTURE.md
* PROJECT_REPORT.md
* AGENTS.md
* CONTRIBUTING.md

---

# Security

* User API keys are never stored permanently.
* Credentials remain under user control through BYOK.
* Uploaded documents are processed temporarily.
* No contract or news data is stored after analysis.

---

# Future Enhancements

* Real-time web fact-checking
* Browser extension integration
* Social media content verification
* Advanced trust scoring dashboard
* Multiple AI model providers
* Local AI inference support
* Additional Indian language support

---

# Team Members

* Simran Sharma
* Kishor Chary

---

# License

This project was developed as part of a hackathon and is intended for educational and demonstration purposes.
