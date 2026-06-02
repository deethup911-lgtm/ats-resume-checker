from sklearn.feature_extraction.text import TfidfVectorizer


# -----------------------------
# Extract Keywords from JD
# -----------------------------
def extract_keywords_from_jd(
    job_description,
    top_n=30
):

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 3),
        max_features=top_n
    )

    tfidf_matrix = vectorizer.fit_transform(
        [job_description]
    )

    keywords = vectorizer.get_feature_names_out()

    return sorted(list(keywords))


# -----------------------------
# Match Keywords
# -----------------------------
def match_keywords(resume_text, jd_keywords):

    resume_lower = resume_text.lower()

    matched_keywords = []
    missing_keywords = []

    for keyword in jd_keywords:

        keyword_lower = keyword.lower().strip()

        # Direct match
        if keyword_lower in resume_lower:
            matched_keywords.append(keyword)
            continue

        # Split combined keywords like "flask mysql"
        parts = keyword_lower.split()

        found_parts = []

        for part in parts:
            if part in resume_lower:
                found_parts.append(part)

        if found_parts:
            matched_keywords.extend(found_parts)

            missing_parts = list(set(parts) - set(found_parts))
            missing_keywords.extend(missing_parts)

        else:
            missing_keywords.append(keyword)

    matched_keywords = sorted(list(set(matched_keywords)))
    missing_keywords = sorted(list(set(missing_keywords) - set(matched_keywords)))

    if len(jd_keywords) == 0:
        match_percentage = 0
    else:
        match_percentage = round(
            (len(matched_keywords) / (len(matched_keywords) + len(missing_keywords))) * 100,
            2
        )

    return matched_keywords, missing_keywords, match_percentage