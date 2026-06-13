# SYSTEM ARCHITECTURE

# TruthLens AI

## Overview

TruthLens AI is an AI-powered Trust and Risk Intelligence Platform that analyzes legal contracts and evaluates the credibility of news content using Google's Gemini Large Language Model.

The system follows a modular architecture that separates the user interface, document processing, business logic, localization, and AI inference layers.

---

# High-Level Architecture

```text
User
  ↓
Language Selection Layer
  ↓
BYOK Authentication Layer
  ↓
Streamlit Interface
  ↓
Analysis Modules
  ↓
Gemini AI Service
  ↓
Localized Results
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
* Render multilingual interface

### File

```text
app.py
```

---

## 2. Localization Layer

### Technology

* Python Dictionary-Based Translation System

### Responsibilities

* Manage language selection
* Render UI content in English, Hindi, and Telugu
* Support future language expansion

### File

```text
utils/translations.py
```

---

## 3. Document Processing Layer

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

## 4. Contract Analysis Module

### Responsibilities

* Generate summaries
* Detect risky clauses
* Highlight obligations
* Produce recommendations
* Generate risk assessments

### File

```text
modules/contract_analyzer.py
```

---

## 5. News Analysis Module

### Responsibilities

* Extract major claims
* Detect bias
* Assess credibility
* Identify missing information
* Generate verdicts

### File

```text
modules/news_analyzer.py
```

---

## 6. AI Inference Layer

### Technology

* Google Gemini 2.5 Flash

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

# Contract Analysis Workflow

```text
User
 ↓
Upload Contract PDF
 ↓
PDF Text Extraction
 ↓
Contract Analyzer Module
 ↓
Gemini AI Processing
 ↓
Risk Assessment & Summary
 ↓
Localized Results Display
```

---

# News Analysis Workflow

```text
User
 ↓
Paste News Article
 ↓
News Analyzer Module
 ↓
Gemini AI Processing
 ↓
Credibility Assessment
 ↓
Localized Results Display
```

---

# Data Flow

```text
User Input
     ↓
Language Selection
     ↓
BYOK Authentication
     ↓
Relevant Analysis Module
     ↓
Gemini AI Service
     ↓
Generated Insights
     ↓
Localized Output
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
* Local AI model integration
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

* Google Gemini 2.5 Flash

## Document Processing

* PyPDF

## Localization

* Python Translation Layer

## Dependency Management

* uv

---

# Version

TruthLens AI v1.0

Hackathon Prototype Architecture Documentation
