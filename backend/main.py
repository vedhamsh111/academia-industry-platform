from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Academia-Industry Collaboration Platform",
    description="AI-enabled platform for skill mapping, internships and placements",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Academia-Industry Platform API is running",
        "status": "success"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/api")
def api_info():
    return {
        "project": "Academia-Industry Collaboration Platform",
        "features": [
            "Student Profiles",
            "Company Profiles",
            "Internships",
            "Placements",
            "Skill Mapping",
            "AI Matching",
            "Skill Gap Analysis",
            "Recommendations",
            "Analytics"
        ]
    }
