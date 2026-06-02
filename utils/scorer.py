from utils.role_weights import ROLE_SKILLS


# -----------------------------
# Role Alignment Score
# -----------------------------
def calculate_role_alignment(
    best_role,
    resume_text
):

    skills = ROLE_SKILLS.get(
        best_role,
        []
    )

    if not skills:
        return 0

    resume_lower = resume_text.lower()

    matched = 0

    for skill in skills:

        if skill.lower() in resume_lower:
            matched += 1

    alignment_score = round(
        (
            matched / len(skills)
        ) * 100,
        2
    )

    return alignment_score

# -----------------------------
# Calculate Final ATS Score
# -----------------------------
def calculate_ats_score(
    match_percentage,
    semantic_match,
    role_alignment_score,
    sections,
    contact_info,
    formatting_score
):

    # -----------------------------
    # Section Score
    # -----------------------------
    section_score = round(
        (
            sum(sections.values())
            / len(sections)
        ) * 100,
        2
    )

    # -----------------------------
    # Contact Score
    # -----------------------------
    contact_score = round(
        (
            sum(contact_info.values())
            / len(contact_info)
        ) * 100,
        2
    )

    # -----------------------------
    # Final ATS Score
    # -----------------------------
    ats_score = round(
        (match_percentage * 0.35) +
        (semantic_match * 0.25) +
        (role_alignment_score * 0.15) +
        (section_score * 0.10) +
        (contact_score * 0.05) +
        (formatting_score * 0.10),
        2
    )
    
    return (
        ats_score,
        section_score,
        contact_score
    )


# -----------------------------
# Generate Suggestions
# -----------------------------
def generate_suggestions(
    ats_score,
    missing_keywords,
    semantic_match
):

    suggestions = []

    # -----------------------------
    # ATS Score Suggestions
    # -----------------------------
    if ats_score >= 80:

        suggestions.append(
            "Your resume is highly ATS-friendly."
        )

    elif ats_score >= 60:

        suggestions.append(
            "Your resume is moderately ATS-friendly. Some improvements are recommended."
        )

    else:

        suggestions.append(
            "Your resume has a low ATS match. Major improvements are needed."
        )

    # -----------------------------
    # Missing Keyword Suggestions
    # -----------------------------
    if missing_keywords:

        suggestions.append(
            "Consider adding these missing keywords if they match your actual skills:"
        )

        for keyword in missing_keywords[:10]:

            suggestions.append(
                f"- {keyword}"
            )

    # -----------------------------
    # Semantic Similarity Suggestions
    # -----------------------------
    if semantic_match < 60:

        suggestions.append(
            "Your resume content is not strongly aligned with the job description."
        )

        suggestions.append(
            "Try rewriting your projects and experience according to the job role."
        )

    # -----------------------------
    # General ATS Suggestions
    # -----------------------------
    suggestions.append(
        "Use standard section headings like Skills, Projects, Experience, and Education."
    )

    suggestions.append(
        "Avoid complex tables, graphics, and images in resumes."
    )

    suggestions.append(
        "Use measurable achievements in experience sections."
    )

    return suggestions