from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# Load Sentence Transformer Model
# -----------------------------
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# -----------------------------
# Calculate Semantic Similarity
# -----------------------------
def calculate_semantic_similarity(
    resume_text,
    job_description
):

    resume_embedding = model.encode(
        resume_text
    )

    jd_embedding = model.encode(
        job_description
    )

    similarity_score = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    semantic_match = round(
        similarity_score * 100,
        2
    )

    return semantic_match