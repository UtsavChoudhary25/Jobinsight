import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.salary import router as salary_router
from app.routes.nlp import router as nlp_router
from app.routes.health import router as health_router

app = FastAPI(
    title="JobInsight AI — Job Market Intelligence API",
    description="Machine Learning Salary Regression and NLP Skill Extraction service trained on 123k+ LinkedIn job postings.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Configuration
# Allows local Vite development, production Vercel frontend, and Vercel preview deployments
origins = [
    "http://localhost:5173",
    "http://localhost:4173",
    "http://localhost:3000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:4173",
    "https://jobinsight-peach.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Register API Routers
app.include_router(health_router)
app.include_router(salary_router)
app.include_router(nlp_router)

@app.get("/")
def root():
    return {
        "service": "JobInsight AI Backend API",
        "status": "online",
        "documentation": "/docs",
        "endpoints": [
            "GET /health",
            "GET /api/model-info",
            "POST /api/predict-salary",
            "POST /api/extract-skills"
        ]
    }
