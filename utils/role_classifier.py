from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# Load Model
# -----------------------------
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# -----------------------------
# Role Descriptions
# -----------------------------
ROLE_DESCRIPTIONS = {
    "Frontend Developer": """
    HTML CSS JavaScript TypeScript React Angular Vue UI UX responsive design
    frontend web development browser DOM Bootstrap Tailwind
    """,

    "Backend Developer": """
    Python Java Node.js FastAPI Flask Django Express REST API GraphQL
    server database authentication backend development microservices
    """,

    "Full Stack Developer": """
    frontend backend React Node.js Python JavaScript database API full stack
    web application development deployment
    """,

    "Data Analyst": """
    SQL Excel Power BI Tableau data analysis dashboards reporting statistics
    data visualization business intelligence
    """,

    "Data Scientist": """
    Python machine learning statistics pandas numpy scikit-learn data science
    predictive modeling data analysis visualization
    """,

    "Machine Learning Engineer": """
    machine learning deep learning NLP computer vision TensorFlow PyTorch
    model training deployment MLOps AI algorithms
    """,

    "AI Engineer": """
    artificial intelligence LLM RAG LangChain OpenAI Gemini vector database
    embeddings prompt engineering agents generative AI
    """,

    "DevOps Engineer": """
    Docker Kubernetes AWS Azure GCP CI/CD Jenkins GitHub Actions Terraform
    cloud deployment infrastructure monitoring
    """,

    "Mobile App Developer": """
    Android iOS Flutter React Native Kotlin Swift mobile app development
    """,

    "Software Engineer": """
    programming software development algorithms data structures APIs databases
    testing debugging system design
    """
}


# -----------------------------
# Classify Resume Role
# -----------------------------
def classify_resume_role(
    resume_text,
    job_description=""
):

    combined_text = resume_text + " " + job_description

    input_embedding = model.encode(
        combined_text
    )

    best_role = None
    best_score = 0

    role_scores = {}

    for role, description in ROLE_DESCRIPTIONS.items():

        role_embedding = model.encode(
            description
        )

        similarity = cosine_similarity(
            [input_embedding],
            [role_embedding]
        )[0][0]

        score = round(
            similarity * 100,
            2
        )

        role_scores[role] = score

        if score > best_score:

            best_score = score
            best_role = role

    sorted_roles = dict(
        sorted(
            role_scores.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )

    return best_role, best_score, sorted_roles