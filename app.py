import streamlit as st

# -----------------------------
# Utility Imports
# -----------------------------
from utils.text_extractor import (
    extract_text_from_pdf,
    extract_text_from_docx
)

from utils.keyword_matcher import (
    match_keywords
)

from utils.charts import (
    create_role_pie_chart,
    create_score_breakdown_chart,
    create_ats_gauge,
    create_resume_health_radar,
    create_role_skill_coverage_chart
)

from utils.role_weights import ROLE_SKILLS

from utils.nlp_keyword_extractor import (
    extract_nlp_keywords
)

from utils.semantic_matcher import (
    calculate_semantic_similarity
)

from utils.resume_checks import (
    detect_resume_sections,
    detect_contact_info
)

from utils.formatting_checker import (
    check_resume_formatting
)

from utils.scorer import (
    calculate_ats_score,
    calculate_role_alignment,
    generate_suggestions
)

from utils.ai_suggestions import (
    generate_ai_suggestions
)

from utils.role_classifier import (
    classify_resume_role
)

from utils.resume_rewriter import (
    rewrite_resume_content
)

from utils.pdf_report import (
    generate_pdf_report
)

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="ATS Resume Checker",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("ATS-Friendly Resume Checker")

st.write(
    "Upload your resume and paste the job description."
)

# -----------------------------
# Resume Upload
# -----------------------------
uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

# -----------------------------
# Job Title
# -----------------------------
job_title = st.selectbox(
    "Job Title",
    [
        "",
        "AI Engineer",
        "Machine Learning Engineer",
        "Backend Developer",
        "Frontend Developer",
        "Full Stack Developer",
        "Data Scientist",
        "DevOps Engineer"
    ]
)

# -----------------------------
# Job Description
# -----------------------------
job_description = st.text_area(
    "Job Description (Optional)",
    height=250
)

# -----------------------------
# ATS Button
# -----------------------------
if st.button("Check ATS Score"):

    # -----------------------------
    # Input Validation
    # -----------------------------
    if uploaded_resume is None:

        st.error(
            "Please upload a resume."
        )

    elif (
        not job_title.strip()
        and
        not job_description.strip()
    ):
        st.error(
            "Please enter a Job Title or Job Description."
        )

    else:

        # -----------------------------
        # File Detection
        # -----------------------------
        file_name = uploaded_resume.name.lower()

        # -----------------------------
        # Resume Text Extraction
        # -----------------------------
        if file_name.endswith(".pdf"):

            resume_text = extract_text_from_pdf(
                uploaded_resume
            )

        elif file_name.endswith(".docx"):

            resume_text = extract_text_from_docx(
                uploaded_resume
            )

        else:

            st.error(
                "Unsupported file type."
            )

            st.stop()

        # -----------------------------
        # Target Job Text
        # -----------------------------
        target_job_text = (
            job_title + " " + job_description
        ).strip()

        # -----------------------------
        # Use Role Skills if JD Missing
        # -----------------------------
        if (
            job_title.strip()
            and
            not job_description.strip()
        ):

            role_skills = ROLE_SKILLS.get(
                job_title,
                []
            )

            target_job_text += " " + " ".join(
                role_skills
            )

        # -----------------------------
        # Extract JD Keywords using NLP
        # -----------------------------
        jd_keywords = extract_nlp_keywords(
            target_job_text
        )

        # -----------------------------
        # Keyword Matching
        # -----------------------------
        (
            matched_keywords,
            missing_keywords,
            match_percentage
        ) = match_keywords(
            resume_text,
            jd_keywords
        )

        # -----------------------------
        # Semantic Similarity
        # -----------------------------
        semantic_match = calculate_semantic_similarity(
            resume_text,
            job_description
        )

        # -----------------------------
        # Resume Checks
        # -----------------------------
        sections = detect_resume_sections(
            resume_text
        )
        # -----------------------------
        # Resume Role Classification
        # -----------------------------
        best_role, role_score, role_scores = classify_resume_role(
            resume_text,
            job_description
        )
        # -----------------------------
        # Role Alignment Score
        # -----------------------------
        role_alignment_score = calculate_role_alignment(
            best_role,
            resume_text
        )

        contact_info = detect_contact_info(
            resume_text
        )
        (
            formatting_results,
            formatting_issues,
            formatting_score
        ) = check_resume_formatting(
            resume_text,
            file_name
        )
        # -----------------------------
        # ATS Score Calculation
        # -----------------------------
        (
            ats_score,
            section_score,
            contact_score
        ) = calculate_ats_score(
            match_percentage,
            semantic_match,
            role_alignment_score,
            sections,
            contact_info,
            formatting_score
        )

        # -----------------------------
        # Suggestions
        # -----------------------------
        suggestions = generate_suggestions(
            ats_score,
            missing_keywords,
            semantic_match
        )
        # -----------------------------
        # AI Suggestions
        # -----------------------------
        ai_suggestions = generate_ai_suggestions(
            resume_text,
            job_description,
            missing_keywords,
            ats_score,
            best_role
        )
        rewritten_resume = rewrite_resume_content(
            resume_text,
            best_role
        )

        report_path = "ATS_Report.pdf"

        generate_pdf_report(
            report_path,
            ats_score,
            best_role,
            role_alignment_score,
            match_percentage,
            semantic_match,
            missing_keywords,
            suggestions,
            ai_suggestions
        )
        # =====================================================
        # DISPLAY SECTION
        # =====================================================

        # -----------------------------
        # Resume Preview
        # -----------------------------
        st.subheader("Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )

        # -----------------------------
        # ATS Score
        # -----------------------------
        st.subheader("Final ATS Score")

        st.progress(
            int(ats_score)
        )


        ats_gauge = create_ats_gauge(
            ats_score
        )

        st.plotly_chart(
            ats_gauge,
            use_container_width=True
        )

        
        score_breakdown_chart = create_score_breakdown_chart(
            match_percentage,
            semantic_match,
            section_score,
            contact_score,
            formatting_score
        )

        st.plotly_chart(
            score_breakdown_chart,
            use_container_width=True
        )

        # -----------------------------
        # Resume Health Radar
        # -----------------------------
        st.subheader(
            "Resume Health Analysis"
        )

        radar_chart = create_resume_health_radar(
            match_percentage,
            semantic_match,
            section_score,
            contact_score,
            formatting_score
        )

        st.plotly_chart(
            radar_chart,
            use_container_width=True
        )
        
        # -----------------------------
        # ATS Status
        # -----------------------------
        if ats_score >= 80:

            st.success(
                "Excellent ATS Match — Your resume is highly ATS-friendly."
            )

        elif ats_score >= 60:

            st.warning(
                "Moderate ATS Match — Resume can be improved further."
            )

        else:

            st.error(
                "Low ATS Match — Resume needs significant improvements."
            )

        # -----------------------------
        # Semantic Similarity
        # -----------------------------
        st.subheader("Semantic Match")

        st.progress(
            int(semantic_match)
        )

        st.metric(
            label="Semantic Similarity",
            value=f"{semantic_match:.2f}%"
        )

        # -----------------------------
        # Keyword Match Results
        # -----------------------------
        st.subheader("Keyword Match Results")

        st.metric(
            "Keyword Match Percentage",
            f"{match_percentage}%"
        )

        col1, col2 = st.columns(2)

        # -----------------------------
        # Matched Keywords
        # -----------------------------
        with col1:

            st.subheader("Matched Keywords")

            if matched_keywords:

                for keyword in matched_keywords:

                    st.success(keyword)

            else:

                st.warning(
                    "No matched keywords found."
                )

        # -----------------------------
        # Missing Keywords
        # -----------------------------
        with col2:

            st.subheader("Missing Keywords")

            if missing_keywords:

                for keyword in missing_keywords:

                    st.error(keyword)

            else:

                st.success(
                    "No missing keywords found."
                )

        # -----------------------------
        # Resume Section Analysis
        # -----------------------------
        st.subheader(
            "Resume Section Analysis"
        )

        for section, present in sections.items():

            if present:

                st.success(
                    f"{section} section found"
                )

            else:

                st.error(
                    f"{section} section missing"
                )

        # -----------------------------
        # Contact Information Analysis
        # -----------------------------
        st.subheader(
            "Contact Information Analysis"
        )

        for item, present in contact_info.items():

            if present:

                st.success(
                    f"{item} found"
                )

            else:

                st.error(
                    f"{item} missing"
                )
        # -----------------------------
        # Resume Formatting Analysis
        # -----------------------------
        st.subheader("Resume Formatting Analysis")

        st.metric(
            "Formatting Score",
            f"{formatting_score}/100"
        )

        for check, passed in formatting_results.items():

            if passed:
                st.success(f"{check} passed")

            else:
                st.error(f"{check} failed")

        if formatting_issues:

            st.subheader("Formatting Issues")

            for issue in formatting_issues:
                st.write(f"- {issue}")


        # -----------------------------
        # Resume Role Classification
        # -----------------------------
        st.subheader("Resume Role Classification")

        st.metric(
            "Predicted Role",
            best_role
        )

        st.metric(
            "Role Confidence",
            f"{role_score:.2f}%"
        )

        st.metric(
            "Role Alignment Score",
            f"{role_alignment_score:.2f}%"
        )

        role_chart = create_role_pie_chart(
            role_scores
        )

        st.plotly_chart(
            role_chart,
            use_container_width=True
        )

        # -----------------------------
        # Role Skill Coverage
        # -----------------------------
        st.subheader(
            "Role Skill Coverage"
        )

        coverage_chart = create_role_skill_coverage_chart(
            best_role,
            resume_text,
            ROLE_SKILLS
        )

        st.plotly_chart(
            coverage_chart,
            use_container_width=True
        )
        # -----------------------------
        # Suggestions
        # -----------------------------
        st.subheader(
            "Improvement Suggestions"
        )

        for suggestion in suggestions:

            st.write(
                suggestion
            )

        # -----------------------------
        # AI Resume Suggestions
        # -----------------------------
        st.subheader(
            "AI-Powered Resume Suggestions"
        )

        st.write(
            ai_suggestions
        )

        st.subheader(
            "Resume Bullet Point Rewriter"
        )

        st.write(
            rewritten_resume
        )

        st.subheader(
            "Download ATS Report"
        )

        with open(
            report_path,
            "rb"
        ) as pdf_file:

            st.download_button(
                label="Download PDF Report",
                data=pdf_file,
                file_name="ATS_Report.pdf",
                mime="application/pdf"
            )