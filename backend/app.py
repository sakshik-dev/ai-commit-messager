from fastapi import FastAPI

from backend.models.request_models import DiffRequest

from backend.services.gemini_service import (
    generate_commit_artifacts,
)

from backend.services.code_review_service import (
    review_code,
)

from backend.services.secret_detector import (
    detect_secrets,
)

from backend.utils.diff_parser import (
    diff_stats,
)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Git Assistant"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {
        "status": "running"
    }


@app.post("/generate")
def generate(request: DiffRequest):

    result = generate_commit_artifacts(
        request.diff
    )

    result["secrets"] = detect_secrets(
        request.diff
    )

    result["statistics"] = diff_stats(
        request.diff
    )

    return result


@app.post("/review")
def review(request: DiffRequest):

    result = review_code(
        request.diff
    )

    return result