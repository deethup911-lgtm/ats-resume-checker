import re


# -----------------------------
# Resume Section Detection
# -----------------------------
def detect_resume_sections(
    resume_text
):

    sections = {
        "Skills": False,
        "Projects": False,
        "Experience": False,
        "Education": False,
        "Certifications": False
    }

    text = resume_text.lower()

    if "skill" in text:
        sections["Skills"] = True

    if "project" in text:
        sections["Projects"] = True

    if "experience" in text:
        sections["Experience"] = True

    if "education" in text:
        sections["Education"] = True

    if (
        "certification" in text
        or
        "certifications" in text
    ):
        sections["Certifications"] = True

    return sections


# -----------------------------
# Contact Information Detection
# -----------------------------
def detect_contact_info(
    resume_text
):

    contact_info = {
        "Email": False,
        "Phone": False,
        "LinkedIn": False,
        "GitHub": False
    }

    # -----------------------------
    # Email Detection
    # -----------------------------
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    if re.search(
        email_pattern,
        resume_text
    ):
        contact_info["Email"] = True

    # -----------------------------
    # Phone Detection
    # -----------------------------
    phone_pattern = r'(\+?\d[\d\s\-\(\)]{8,}\d)'

    if re.search(
        phone_pattern,
        resume_text
    ):
        contact_info["Phone"] = True

    # -----------------------------
    # LinkedIn Detection
    # -----------------------------
    if "linkedin.com" in resume_text.lower():
        contact_info["LinkedIn"] = True

    # -----------------------------
    # GitHub Detection
    # -----------------------------
    if "github.com" in resume_text.lower():
        contact_info["GitHub"] = True

    return contact_info