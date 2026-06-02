# ATS Resume Checker

An AI-powered ATS (Applicant Tracking System) Resume Checker built using Python, Streamlit, NLP, Sentence Transformers, Gemini AI, and Plotly.

The application analyzes resumes against job requirements, calculates ATS compatibility scores, identifies missing skills, predicts suitable job roles, generates AI-powered improvement suggestions, and provides an interactive analytics dashboard.

---

## Features

### Resume Analysis
- Upload PDF resumes
- Upload DOCX resumes
- Automatic resume text extraction
- ATS-friendly formatting analysis
- Resume section detection
- Contact information detection

### ATS Scoring
- Keyword matching
- Semantic similarity analysis
- Role alignment scoring
- Formatting score
- Contact score
- Section score
- Overall ATS score out of 100

### AI Features
- AI-powered resume suggestions
- Resume bullet point rewriter
- Missing skill recommendations
- ATS optimization advice
- Role-specific resume improvements

### Role-Based Analysis
- Resume role classification
- Role confidence score
- Role alignment score
- Job title support
- Optional job description analysis

Supported Roles:
- AI Engineer
- Machine Learning Engineer
- Data Scientist
- Backend Developer
- Frontend Developer
- Full Stack Developer
- DevOps Engineer

### Interactive Dashboard
- ATS Score Gauge Meter
- Resume Health Radar Chart
- Role Classification Pie Chart
- ATS Score Breakdown Chart
- Role Skill Coverage Visualization

### Reporting
- ATS PDF Report Generation
- Downloadable ATS Analysis Report

---

## Tech Stack

| Category | Tools Used |
|-----------|------------|
| Programming Language | Python |
| Frontend/UI | Streamlit |
| NLP | spaCy |
| Embeddings | Sentence Transformers |
| Similarity Engine | Scikit-learn |
| AI Suggestions | Gemini API |
| PDF Parsing | PyMuPDF |
| DOCX Parsing | python-docx |
| Visualizations | Plotly |
| PDF Reports | ReportLab |
| Environment Variables | python-dotenv |

---

## Project Structure

```text
ats_resume_checker/
│
├── app.py
│
├── README.md
├── requirements.txt
├── .env
│
├── utils/
│   ├── ai_suggestions.py
│   ├── charts.py
│   ├── contact_checker.py
│   ├── formatting_checker.py
│   ├── keyword_matcher.py
│   ├── nlp_extractor.py
│   ├── pdf_report.py
│   ├── resume_rewriter.py
│   ├── role_classifier.py
│   ├── role_weights.py
│   ├── scorer.py
│   ├── section_checker.py
│   ├── semantic_matcher.py
│   ├── skill_database.py
│   └── text_extractor.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/ats-resume-checker.git

cd ats-resume-checker
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Run Application

```bash
streamlit run app.py
```

Application runs at:

```text
http://localhost:8501
```

---

## ATS Workflow

```text
Resume Upload
        ↓
Text Extraction
        ↓
NLP Skill Extraction
        ↓
Keyword Matching
        ↓
Semantic Similarity Analysis
        ↓
Role Classification
        ↓
Role Alignment Scoring
        ↓
ATS Score Calculation
        ↓
Dashboard Visualization
        ↓
AI Suggestions
        ↓
Resume Rewriting
        ↓
PDF Report Generation
```

---

## Future Enhancements

- Resume Version Comparison
- MongoDB Analysis History
- ESCO Skill Ontology Integration
- Authentication System
- Resume Recommendation Engine
- Job Description Templates

---

## Author

Deethu P

