# PROJECT REPORT

# TruthLens AI

## Abstract

TruthLens AI is an AI-powered trust and risk intelligence platform developed to help users better understand complex contracts and evaluate the credibility of news content. The system utilizes Google's Gemini Large Language Model (LLM) to analyze text, identify risks, detect potential bias, and generate actionable insights.

The platform supports Bring Your Own Key (BYOK), allowing users to securely provide their own Gemini API credentials at runtime.

---

# 1. Introduction

The rapid growth of digital information has made it increasingly difficult for individuals to evaluate the reliability and implications of the content they consume.

TruthLens AI addresses these challenges by providing automated analysis and simplified insights through Generative AI.

---

# 2. Problem Statement

Users face several challenges when reviewing contracts and news articles:

* Legal contracts are lengthy and difficult to interpret.
* Important clauses and risks may be overlooked.
* News content may contain misinformation or hidden bias.
* Manual verification is time-consuming.

---

# 3. Objectives

* Simplify contract review and risk assessment.
* Improve transparency in legal documentation.
* Evaluate news credibility.
* Detect potential bias and misinformation.
* Provide AI-generated recommendations.
* Deliver a user-friendly experience.

---

# 4. Proposed Solution

TruthLens AI provides:

## Contract Risk Analyzer

* Executive summaries
* Risk assessments
* Missing clause detection
* User obligations
* Recommendations

## News Credibility Analyzer

* Main claim extraction
* Bias analysis
* Credibility evaluation
* Missing information detection
* AI-generated verdicts

---

# 5. System Architecture

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
Generated Insights
```

---

# 6. Technology Stack

## Frontend

* Streamlit

## Backend

* Python

## Artificial Intelligence

* Google Gemini API

## Authentication Model

* Bring Your Own Key (BYOK)
* Runtime Gemini API Authentication

## Libraries

* google-generativeai
* pypdf
* plotly

## Dependency Management

* uv

---

# 7. Implementation

## Contract Analysis Workflow

1. User uploads a PDF contract.
2. Text is extracted using PyPDF.
3. Gemini analyzes the contract.
4. Risk assessment is generated.
5. Results are displayed.

## News Analysis Workflow

1. User pastes a news article.
2. Gemini evaluates the content.
3. Credibility and bias are assessed.
4. Results are displayed.

---

# 8. Features

* Contract Risk Analysis
* News Credibility Analysis
* AI-Powered Summarization
* Risk Identification
* Bias Detection
* BYOK Support
* Secure Runtime Authentication
* Interactive Streamlit Interface

---

# 9. Results

The platform successfully performs:

* Contract analysis from uploaded PDFs.
* News credibility evaluation.
* AI-generated summaries and recommendations.
* Risk and bias identification.

---

# 10. Challenges Faced

* Gemini API rate limits.
* Environment configuration issues.
* Dependency compatibility.
* Prompt engineering.
* PDF extraction consistency.

---

# 11. Future Scope

* Real-time fact-checking integration
* Multi-language support
* Browser extension
* Social media verification
* Multiple AI model providers
* Advanced trust scoring dashboard

---

# 12. Conclusion

TruthLens AI demonstrates how Generative AI can improve transparency and decision-making by simplifying contract review and evaluating news credibility.

The project provides a strong foundation for future development into a comprehensive trust and risk intelligence platform.

---

# Team Members

* Simran Sharma
* Kishor Chary

---

# Version

TruthLens AI v1.0

Hackathon Prototype Submission
