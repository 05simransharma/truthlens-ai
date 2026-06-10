# PROJECT REPORT

# TruthLens AI

## Abstract

TruthLens AI is an AI-powered trust and risk intelligence platform developed to help users better understand complex contracts and evaluate the credibility of news content. The system utilizes Google's Gemini Large Language Model (LLM) to analyze text, identify risks, detect potential bias, and generate actionable insights.

The platform addresses two common challenges faced by users today:

1. Understanding lengthy legal contracts.
2. Identifying potentially misleading or biased news content.

By leveraging Generative AI, TruthLens AI simplifies decision-making and improves information transparency.

---

# 1. Introduction

The rapid growth of digital information has made it increasingly difficult for individuals to evaluate the reliability and implications of the content they consume.

Legal contracts often contain complex language that can obscure important obligations and risks. Similarly, the widespread availability of online news has increased the risk of misinformation, sensationalism, and biased reporting.

TruthLens AI was developed to address these challenges by providing automated analysis and simplified insights through artificial intelligence.

---

# 2. Problem Statement

Users face several challenges when reviewing contracts and news articles:

* Legal contracts are often lengthy and difficult to interpret.
* Important clauses and risks may be overlooked.
* News content may contain misinformation or hidden bias.
* Manual verification is time-consuming and requires expertise.

The absence of accessible tools for analyzing such content can lead to poor decision-making and increased risk.

---

# 3. Objectives

The primary objectives of TruthLens AI are:

* Simplify contract review and risk assessment.
* Improve transparency in legal documentation.
* Evaluate the credibility of news articles.
* Detect potential bias and misinformation.
* Provide AI-generated recommendations and summaries.
* Create an intuitive and user-friendly interface.

---

# 4. Proposed Solution

TruthLens AI provides two integrated analysis modules:

## Contract Risk Analyzer

Allows users to upload PDF contracts and receive:

* Executive summaries
* Risk assessments
* Identification of risky clauses
* User obligations
* Recommendations

## News Credibility Analyzer

Allows users to submit news content and receive:

* Main claim extraction
* Bias analysis
* Credibility evaluation
* Missing information detection
* AI-generated verdicts

---

# 5. System Architecture

The system follows a modular architecture consisting of:

```text
User
  ↓
Streamlit Interface
  ↓
Analysis Modules
  ↓
Gemini AI Service
  ↓
Generated Insights
```

### Components

1. User Interface Layer
2. Document Processing Layer
3. Contract Analysis Module
4. News Analysis Module
5. Gemini AI Integration Layer

---

# 6. Technology Stack

## Frontend

* Streamlit

## Backend

* Python

## Artificial Intelligence

* Google Gemini API

## Libraries

* google-generativeai
* pypdf
* python-dotenv
* plotly

## Dependency Management

* uv

## Version Control

* Git
* GitLab

---

# 7. Implementation

## Contract Analysis Workflow

1. User uploads a PDF contract.
2. Text is extracted using PyPDF.
3. Extracted content is passed to Gemini AI.
4. The model performs risk analysis.
5. Results are displayed to the user.

## News Analysis Workflow

1. User submits a news article.
2. Article content is sent to Gemini AI.
3. The model evaluates credibility and bias.
4. Results are generated and displayed.

---

# 8. Features

### Contract Risk Analyzer

* PDF Upload Support
* Contract Summarization
* Risk Identification
* Obligation Detection
* AI Recommendations

### News Credibility Analyzer

* Credibility Assessment
* Bias Detection
* Claim Extraction
* Information Gap Analysis
* AI Verdict Generation

### General Features

* Interactive User Interface
* Fast Analysis
* Modular Architecture
* Cloud-Based AI Integration

---

# 9. Results

The developed system successfully performs:

* Contract analysis using uploaded PDF documents.
* News credibility evaluation from user-provided content.
* AI-powered summaries and recommendations.
* Risk and bias identification.

Testing demonstrated that the platform provides meaningful insights within seconds while maintaining a simple user experience.

---

# 10. Challenges Faced

During development, the following challenges were encountered:

* Gemini API rate limits during testing.
* Environment configuration issues.
* Dependency management and package compatibility.
* Prompt optimization for accurate results.
* PDF text extraction consistency.

These challenges were resolved through proper configuration, testing, and modular development practices.

---

# 11. Future Scope

Future enhancements may include:

* Real-time fact-checking integration
* Multi-language support
* Social media content verification
* User authentication and history tracking
* Risk score visualizations
* Browser extension support
* Advanced misinformation detection

---

# 12. Conclusion

TruthLens AI demonstrates how Generative AI can be used to improve transparency and decision-making in everyday digital interactions.

By simplifying contract review and assisting users in evaluating news credibility, the platform provides practical value while showcasing the capabilities of modern AI systems.

The project establishes a strong foundation for future development into a comprehensive trust and risk intelligence platform.

---

# Team Members

* Simran Sharma
* Kishor Chary

---

# Project

TruthLens AI

Hackathon Prototype Submission

Version 1.0
