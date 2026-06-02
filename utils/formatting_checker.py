# -----------------------------
# Resume Formatting Checker
# -----------------------------
def check_resume_formatting(
    resume_text,
    file_name
):

    formatting_results = {
        "ATS-safe file type": False,
        "Good text extraction": False,
        "Readable text length": False,
        "Low special character usage": False,
        "Clean line structure": False
    }

    issues = []

    # -----------------------------
    # File Type Check
    # -----------------------------
    if file_name.endswith(".pdf") or file_name.endswith(".docx"):
        formatting_results["ATS-safe file type"] = True
    else:
        issues.append("Use PDF or DOCX format.")

    # -----------------------------
    # Text Extraction Check
    # -----------------------------
    if resume_text and len(resume_text.strip()) > 200:
        formatting_results["Good text extraction"] = True
    else:
        issues.append(
            "Very little text was extracted. Resume may be image-based or poorly formatted."
        )

    # -----------------------------
    # Readable Length Check
    # -----------------------------
    if len(resume_text.split()) >= 100:
        formatting_results["Readable text length"] = True
    else:
        issues.append(
            "Resume text is too short. Add more details about skills, projects, and experience."
        )

    # -----------------------------
    # Special Character Check
    # -----------------------------
    special_chars = 0

    for char in resume_text:
        if not char.isalnum() and not char.isspace():
            special_chars += 1

    if len(resume_text) > 0:
        special_char_ratio = special_chars / len(resume_text)
    else:
        special_char_ratio = 1

    if special_char_ratio < 0.08:
        formatting_results["Low special character usage"] = True
    else:
        issues.append(
            "Resume contains many special characters, icons, or symbols. ATS may not parse them correctly."
        )

    # -----------------------------
    # Line Structure Check
    # -----------------------------
    lines = resume_text.splitlines()

    short_lines = []

    for line in lines:
        if 0 < len(line.strip()) < 4:
            short_lines.append(line)

    if len(lines) > 0:
        short_line_ratio = len(short_lines) / len(lines)
    else:
        short_line_ratio = 1

    if short_line_ratio < 0.30:
        formatting_results["Clean line structure"] = True
    else:
        issues.append(
            "Resume has many broken/very short lines. It may contain columns or complex layout."
        )

    formatting_score = round(
        (
            sum(formatting_results.values())
            / len(formatting_results)
        ) * 100,
        2
    )

    return formatting_results, issues, formatting_score