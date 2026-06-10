# SYSTEM ARCHITECTURE

# TruthLens AI

## Overview

TruthLens AI is an AI-powered trust and risk intelligence platform that analyzes legal contracts and evaluates the credibility of news content using Google's Gemini Large Language Model.

The system follows a modular architecture that separates the user interface, business logic, document processing, and AI inference layers.

---

# High-Level Architecture

```text
+----------------------+
|      User            |
+----------+-----------+
           |
           v
+----------------------+
|   Streamlit UI       |
|      (app.py)        |
+----------+-----------+
           |
           v
+----------------------+
| Application Modules  |
+----------+-----------+
           |
   +-------+-------+
   |               |
   v               v
Contract       News
Analyzer      Analyzer
   |               |
   +-------+-------+
           |
           v
+----------------------+
| Gemini AI Service    |
| (Google Gemini API)  |
+----------+-----------+
           |
           v
+----------------------+
| Analysis Results     |
+----------------------+
```

---

# System Components

## 1. User Interface Layer

### Technology

* Streamlit

### Responsibilities

* Accept user input
* Upload PDF contracts
* Receive news article text
* Display AI-generated analysis
* Present results in a user-friendly format

### File

```text
app.py
```

---

## 2. Document Processing Layer

### Technology

* PyPDF

### Responsibilities

* Read uploaded PDF files
* Extract textual content
* Prepare content for AI analysis

### File

```text
utils/pdf_loader.py
```

### Workflow

```text
PDF Upload
     ↓
PDF Reader
     ↓
Text Extraction
     ↓
Contract Analyzer
```

---

## 3. Contract Analysis Module

### Purpose

Processes legal contracts and identifies risks.

### Responsibilities

* Generate summaries
* Detect risky clauses
* Highlight obligations
* Produce recommendations

### File

```text
modules/contract_analyzer.py
```

### Workflow

```text
Contract Text
      ↓
Prompt Generation
      ↓
Gemini AI
      ↓
Risk Assessment
      ↓
Results
```

---

## 4. News Analysis Module

### Purpose

Evaluates news content credibility.

### Responsibilities

* Extract major claims
* Detect bias
* Assess credibility
* Generate verdicts

### File

```text
modules/news_analyzer.py
```

### Workflow

```text
News Article
      ↓
Prompt Generation
      ↓
Gemini AI
      ↓
Credibility Analysis
      ↓
Results
```

---

## 5. AI Inference Layer

### Technology

* Google Gemini API

### Responsibilities

* Natural Language Understanding
* Contract Interpretation
* Risk Assessment
* Bias Detection
* Content Summarization

### File

```text
utils/gemini_client.py
```

### Workflow

```text
Prompt
   ↓
Gemini Model
   ↓
Generated Analysis
   ↓
Application Output
```

---

# Directory Structure

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
├── .env
├── pyproject.toml
├── uv.lock
├── README.md
├── USER_MANUAL.md
└── SYSTEM_ARCHITECTURE.md
```

---

# Data Flow

## Contract Analysis Flow

```text
User
 ↓
Upload PDF
 ↓
PDF Text Extraction
 ↓
Contract Analyzer
 ↓
Gemini API
 ↓
Risk Analysis Report
 ↓
Display Results
```

---

## News Analysis Flow

```text
User
 ↓
Paste Article
 ↓
News Analyzer
 ↓
Gemini API
 ↓
Credibility Assessment
 ↓
Display Results
```

---

# Security Considerations

* API keys are stored in environment variables.
* Sensitive credentials are excluded from version control.
* User-uploaded documents are processed temporarily.
* No permanent storage of user data.

---

# Scalability Considerations

Future versions may include:

* Multiple AI model support
* Database integration
* User authentication
* Analysis history
* Cloud deployment
* Real-time fact-checking services

---

# Technology Stack

## Frontend

* Streamlit

## Backend

* Python

## AI Services

* Google Gemini

## Document Processing

* PyPDF

## Environment Management

* Python Dotenv

## Dependency Management

* uv

---

# Version

TruthLens AI v1.0

Hackathon Prototype Architecture Documentation
