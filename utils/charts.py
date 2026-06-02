import plotly.express as px


def create_role_pie_chart(role_scores):

    top_roles = dict(
        list(role_scores.items())[:5]
    )

    fig = px.pie(
        names=list(top_roles.keys()),
        values=list(top_roles.values()),
        title="Resume Role Classification"
    )

    fig.update_traces(
        textinfo="label+percent"
    )

    return fig


import plotly.express as px


def create_score_breakdown_chart(
    match_percentage,
    semantic_match,
    section_score,
    contact_score,
    formatting_score
):

    score_data = {
        "Category": [
            "Keyword Match",
            "Semantic Match",
            "Section Score",
            "Contact Score",
            "Formatting Score"
        ],
        "Score": [
            round(match_percentage, 2),
            round(semantic_match, 2),
            round(section_score, 2),
            round(contact_score, 2),
            round(formatting_score, 2)
        ]
    }

    fig = px.bar(
        score_data,
        x="Category",
        y="Score",
        title="ATS Score Breakdown",
        text="Score"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig.update_layout(
        yaxis_range=[0, 100],
        yaxis_title="Score out of 100",
        xaxis_title="Category"
    )

    return fig

import plotly.express as px


import plotly.graph_objects as go


def create_ats_gauge(
    ats_score
):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=ats_score,
            title={
                "text": "ATS Score"
            },
            number={
                "valueformat": ".2f"
            },
            gauge={
                "axis": {
                    "range": [0, 100]
                },
                "bar": {
                    "thickness": 0.3
                },
                "steps": [
                    {
                        "range": [0, 50],
                        "color": "#ffcccc"
                    },
                    {
                        "range": [50, 80],
                        "color": "#fff4cc"
                    },
                    {
                        "range": [80, 100],
                        "color": "#d4f7d4"
                    }
                ]
            }
        )
    )

    fig.update_layout(
        height=350
    )

    return fig


import plotly.graph_objects as go


def create_resume_health_radar(
    match_percentage,
    semantic_match,
    section_score,
    contact_score,
    formatting_score
):

    categories = [
        "Keyword Match",
        "Semantic Match",
        "Sections",
        "Contact Info",
        "Formatting"
    ]

    values = [
        match_percentage,
        semantic_match,
        section_score,
        contact_score,
        formatting_score
    ]

    # Close the polygon
    categories.append(categories[0])
    values.append(values[0])

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill="toself",
            name="Resume Health"
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False,
        title="Resume Health Analysis"
    )

    return fig

import plotly.express as px


def create_role_skill_coverage_chart(
    best_role,
    resume_text,
    role_skills
):

    skills = role_skills.get(
        best_role,
        []
    )

    resume_lower = resume_text.lower()

    skill_data = []

    for skill in skills:

        if skill.lower() in resume_lower:

            skill_data.append(
                {
                    "Skill": skill,
                    "Status": "Present",
                    "Value": 1
                }
            )

        else:

            skill_data.append(
                {
                    "Skill": skill,
                    "Status": "Missing",
                    "Value": 1
                }
            )

    fig = px.bar(
        skill_data,
        x="Skill",
        y="Value",
        color="Status",
        title=f"{best_role} Skill Coverage"
    )

    fig.update_layout(
        yaxis_visible=False
    )

    return fig