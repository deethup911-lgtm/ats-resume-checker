import os

from dotenv import load_dotenv
from google import genai


# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# -----------------------------
# Generate AI Suggestions
# -----------------------------
def generate_ai_suggestions(
    resume_text,
    job_description,
    missing_keywords,
    ats_score,
    best_role
):

    prompt = f"""
You are an ATS resume optimization expert.

Analyze the resume for the target role: {best_role}

Resume:
{resume_text}

Job Description:
{job_description}

Missing Keywords:
{missing_keywords}

ATS Score:
{ats_score}

Give the output in this structure:

1. ATS Summary
- Explain whether the resume is strong or weak for this job.

2. Missing Keyword Usage
- Suggest how to naturally add missing keywords.
- Do not suggest fake skills.

3. Resume Rewrite Suggestions
- Rewrite 3 weak resume/project/experience lines into stronger ATS-friendly bullet points.
- Use action verbs.
- Add measurable impact wherever possible.

4. Project Improvement Suggestions
- Suggest how to improve project descriptions for this role.

5. Role-Specific Advice
- Give advice specific to the predicted role.

Keep the answer clear, practical, and beginner-friendly.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text