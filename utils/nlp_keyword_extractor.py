import re
import spacy

from utils.skill_database import (
    TECH_SKILLS,
    SKILL_NORMALIZATION
)


# -----------------------------
# Load spaCy Model
# -----------------------------
nlp = spacy.load("en_core_web_sm")


# -----------------------------
# Generic Non-Skill Words
# -----------------------------
GENERIC_WORDS = {
    "experience",
    "ability",
    "applications",
    "knowledge",
    "understanding",
    "skills",
    "work",
    "team",
    "project",
    "projects",
    "development",
    "developer",
    "using",
    "system",
    "systems",
    "solutions",
    "based",
    "strong",
    "good",
    "company",
    "description",
    "website",
    "years",
    "environment",
    "commitment",
    "passionate",
    "skilled",
    "global",
    "talent",
    "mobility",
    "collaborative",
    "fast-paced"
}


# -----------------------------
# Check technical-looking unknown terms
# -----------------------------
def is_potential_tech_term(term):
    WEAK_TERMS = {
        "api",
        "apis",
        "cd",
        "ci",
        "ml",
        "ai"
    }

    term = term.strip()

    if not term:
        return False

    # Remove URLs
    if "http" in term or "www." in term:
        return False

    # Remove numbers like 1.5 years
    if re.search(r"\d", term):
        return False

    # Remove long generic phrases
    if len(term.split()) > 3:
        return False

    lower_term = term.lower()
    if (
        lower_term in GENERIC_WORDS
        or
        lower_term in WEAK_TERMS
    ):
        return False

    # Keep terms like CrewAI, LangGraph, Qdrant, FastAPI
    if re.search(r"[A-Z][a-z]+[A-Z]", term):
        return True

    # Keep terms with common tech suffixes
    tech_suffixes = (
        "js",
        "db",
        "sql",
        "api",
        "ai",
        "ml",
        "nlp",
        "cloud",
        "graph"
    )

    if lower_term.endswith(tech_suffixes):
        return True

    # Keep common short technical uppercase terms
    if term.isupper() and 2 <= len(term) <= 6:
        return True

    return False


# -----------------------------
# NLP Keyword Extraction
# -----------------------------
def extract_nlp_keywords(text):

    doc = nlp(text)

    confirmed_skills = set()
    potential_skills = set()

    text_lower = text.lower()

    # -----------------------------
    # 1. Match known technical skills from DB
    # -----------------------------
    for skill in TECH_SKILLS:

        if skill in text_lower:
            confirmed_skills.add(skill)

    # -----------------------------
    # 2. Extract possible new tools using spaCy
    # -----------------------------
    for token in doc:

        term = token.text.strip()

        if is_potential_tech_term(term):
            potential_skills.add(term.lower())

    # -----------------------------
    # 3. Extract noun chunks but filter strongly
    # -----------------------------
    for chunk in doc.noun_chunks:

        term = chunk.text.strip()

        lower_term = term.lower()

        if lower_term in TECH_SKILLS:
            confirmed_skills.add(lower_term)

        elif is_potential_tech_term(term):
            potential_skills.add(lower_term)

    # -----------------------------
    # Combine Skills
    # -----------------------------
    all_keywords = (
        confirmed_skills
        | potential_skills
    )

    normalized_keywords = set()

    # -----------------------------
    # Normalize Similar Skills
    # -----------------------------
    for keyword in all_keywords:

        keyword_lower = keyword.lower()

        if keyword_lower in SKILL_NORMALIZATION:

            normalized_keywords.add(
                SKILL_NORMALIZATION[keyword_lower]
            )

        else:

            normalized_keywords.add(
                keyword_lower
            )

    return sorted(list(normalized_keywords))