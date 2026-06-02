# -----------------------------
# Technical Skill Database
# -----------------------------
TECH_SKILLS = {
    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "php",
    "ruby",
    "golang",
    "rust",
    "kotlin",
    "swift",
    "scala",
    "r language",
    "matlab",

    # Web Frontend
    "html",
    "css",
    "sass",
    "bootstrap",
    "tailwind",
    "tailwind css",
    "react",
    "react.js",
    "next.js",
    "angular",
    "vue",
    "vue.js",
    "jquery",

    # Backend
    "node.js",
    "node",
    "express",
    "express.js",
    "fastapi",
    "flask",
    "django",
    "spring boot",
    "laravel",
    "rails",
    "ruby on rails",

    # Databases
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",
    "oracle",
    "firebase",
    "redis",
    "cassandra",
    "dynamodb",
    "neo4j",

    # APIs
    "api",
    "rest api",
    "restful api",
    "graphql",
    "soap",
    "postman",
    "swagger",

    # AI / ML / Data Science
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "ai",
    "ml",
    "nlp",
    "natural language processing",
    "computer vision",
    "data science",
    "data analysis",
    "pandas",
    "numpy",
    "scikit-learn",
    "sklearn",
    "tensorflow",
    "keras",
    "pytorch",
    "opencv",
    "matplotlib",
    "seaborn",
    "plotly",

    # GenAI / LLM
    "llm",
    "large language model",
    "rag",
    "retrieval augmented generation",
    "langchain",
    "llamaindex",
    "openai",
    "gemini",
    "huggingface",
    "hugging face",
    "sentence-transformers",
    "transformers",
    "crewai",
    "langgraph",

    # Vector Databases
    "faiss",
    "chroma",
    "chromadb",
    "pinecone",
    "weaviate",
    "qdrant",
    "milvus",

    # Cloud / DevOps
    "aws",
    "azure",
    "gcp",
    "google cloud",
    "docker",
    "kubernetes",
    "jenkins",
    "github actions",
    "ci/cd",
    "terraform",
    "ansible",
    "nginx",

    # Version Control
    "git",
    "github",
    "gitlab",
    "bitbucket",

    # Testing
    "pytest",
    "selenium",
    "junit",
    "unittest",
    "jest",
    "cypress",

    # Mobile
    "android",
    "ios",
    "flutter",
    "react native",
    "dart",

    # BI / Analytics
    "power bi",
    "tableau",
    "excel",
    "google sheets",

    # Project / Collaboration Tools
    "jira",
    "trello",
    "slack",
    "notion",

    # Other Tools
    "streamlit",
    "gradio",
    "fastapi",
    "uvicorn"
}

# -----------------------------
# Skill Normalization Mapping
# -----------------------------
SKILL_NORMALIZATION = {

    # AI / ML
    "ai/ml": "artificial intelligence",
    "ai ml": "artificial intelligence",
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "llm": "large language model",
    "nlp": "natural language processing",

    # JavaScript
    "js": "javascript",
    "ts": "typescript",

    # APIs
    "restful api": "rest api",

    # Frameworks
    "react.js": "react",
    "vue.js": "vue",
    "express.js": "express",

    # GenAI
    "retrieval augmented generation": "rag",
    "hugging face": "huggingface",

    # Databases
    "postgres": "postgresql",

    # Cloud
    "google cloud": "gcp"
}