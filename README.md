# 🔍 TruthLens AI

## Overview

TruthLens AI is an AI-powered trust and risk intelligence platform designed to help users make informed decisions by analyzing contracts and evaluating the credibility of news content.

The platform leverages Google's Gemini AI model to provide clear summaries, identify risks, detect bias, and generate actionable insights from complex documents and articles.

---

## Problem Statement

In today's digital world, users are constantly exposed to:

* Complex legal contracts that are difficult to understand.
* Misleading or biased news articles.
* Information overload that makes verification challenging.

Many individuals lack the expertise or time required to carefully review such content before making important decisions.

---

## Solution

TruthLens AI simplifies information analysis by using Generative AI to:

* Analyze contracts and identify potential risks.
* Summarize lengthy legal documents.
* Evaluate the credibility of news articles.
* Detect possible bias and misinformation.
* Provide understandable recommendations.

---

## Features

### 📄 Contract Risk Analyzer

* Upload PDF contracts.
* Generate concise summaries.
* Identify risky clauses.
* Highlight user obligations.
* Provide recommendations and risk insights.

### 📰 News Credibility Analyzer

* Analyze news articles and reports.
* Extract major claims.
* Detect potential bias.
* Evaluate credibility.
* Generate AI-powered verdicts.

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Google Gemini

### Libraries

* google-generativeai
* pypdf
* python-dotenv
* plotly

### Package Management

* uv

---

## Project Structure

```text
truthlens-ai/
│
├── app.py
├── modules/
│   ├── contract_analyzer.py
│   └── news_analyzer.py
│
├── utils/
│   ├── gemini_client.py
│   └── pdf_loader.py
│
├── .env
├── pyproject.toml
├── uv.lock
└── README.md
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd truthlens-ai
```

### Install Dependencies

Using uv:

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Running the Application

```bash
uv run streamlit run app.py
```

The application will launch in your browser.

---

## Usage

### Contract Analysis

1. Open the Contract Analysis tab.
2. Upload a PDF contract.
3. Click **Analyze Contract**.
4. Review the generated report.

### News Analysis

1. Open the News Analysis tab.
2. Paste a news article.
3. Click **Analyze News**.
4. Review the credibility assessment.

---

## Application UI

### Home Page
![Home Page](assets/Homepage.png)

### Contract Analysis
![Contract Analyzer](assets/ContractAnalysis.png)

### News Analysis
![News Analyzer](assets/NewsAnalysis.png)

## Future Enhancements

* Real-time web fact-checking
* Multi-language support
* Browser extension integration
* Social media content verification
* Advanced trust scoring dashboard

---

## Team Members

* Simran Sharma
* Kishor Chary

---

## License

This project was developed as part of a hackathon and is intended for educational and demonstration purposes.
