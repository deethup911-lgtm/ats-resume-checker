from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    file_path,
    ats_score,
    best_role,
    role_alignment_score,
    match_percentage,
    semantic_match,
    missing_keywords,
    suggestions,
    ai_suggestions
):

    doc = SimpleDocTemplate(
        file_path
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "ATS Resume Analysis Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"ATS Score: {ats_score:.2f}/100",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Predicted Role: {best_role}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Role Alignment: {role_alignment_score:.2f}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Keyword Match: {match_percentage:.2f}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Semantic Match: {semantic_match:.2f}%",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Missing Skills",
            styles["Heading2"]
        )
    )

    for skill in missing_keywords:

        content.append(
            Paragraph(
                f"• {skill}",
                styles["BodyText"]
            )
        )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "ATS Suggestions",
            styles["Heading2"]
        )
    )

    for suggestion in suggestions:

        content.append(
            Paragraph(
                suggestion,
                styles["BodyText"]
            )
        )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "AI Suggestions",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            ai_suggestions,
            styles["BodyText"]
        )
    )

    doc.build(content)

    return file_path