# SYSTEM ARCHITECTURE

# TruthLens AI

## Overview

TruthLens AI is an AI-powered trust and risk intelligence platform that analyzes legal contracts and evaluates the credibility of news content using Google's Gemini Large Language Model.

The system follows a modular architecture that separates the user interface, document processing, business logic, and AI inference layers.

---

# High-Level Architecture

```text
User
  ↓
BYOK Authentication Layer
  ↓
Streamlit Interface
  ↓
Analysis Modules
  ↓
Gemini AI Service
  ↓
Results
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
* Collect Gemini API key
* Display AI-generated analysis

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

---

## 3. Contract Analysis Module

### Responsibilities

* Generate summaries
* Detect risky clauses
* Highlight obligations
* Produce recommendations

### File

```text
modules/contract_analyzer.py
```

---

## 4. News Analysis Module

### Responsibilities

* Extract major claims
* Detect bias
* Assess credibility
* Generate verdicts

### File

```text
modules/news_analyzer.py
```

---

## 5. AI Inference Layer

### Technology

* Google Gemini API

### Responsibilities

* Runtime BYOK Authentication
* Contract Interpretation
* Risk Assessment
* Bias Detection
* Content Summarization
* Natural Language Understanding

### File

```text
utils/gemini_client.py
```

---

# Data Flow

```text
User
  ↓
BYOK Authentication Layer
  ↓
Streamlit Interface
  ↓
Analysis Modules
  ↓
Gemini AI Service
  ↓
Results
```

---

# Security Considerations

* The application follows a Bring Your Own Key (BYOK) model.
* Users provide their own Gemini API key during runtime.
* API keys are not stored by the application.
* User-uploaded documents are processed temporarily.
* No permanent storage of user credentials or uploaded data.

---

# Scalability Considerations

Future versions may include:

* Multiple AI model providers
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

## Dependency Management

* uv

---

# Version

TruthLens AI v1.0

Hackathon Prototype Architecture Documentation
