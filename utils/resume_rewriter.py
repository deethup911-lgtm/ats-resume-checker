import os

from dotenv import load_dotenv
from google import genai


# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# -----------------------------
# Resume Bullet Rewriter
# -----------------------------
def rewrite_resume_content(
    resume_text,
    best_role
):

    prompt = f"""
You are an expert ATS Resume Writer.

Target Role:
{best_role}

Resume Content:
{resume_text}

Task:

1. Identify weak bullet points.
2. Rewrite them professionally.
3. Use strong action verbs.
4. Make them ATS-friendly.
5. Add impact-oriented wording.
6. Keep them realistic.
7. Return only improved bullet points.

Format:

Original:
...

Improved:
...
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text