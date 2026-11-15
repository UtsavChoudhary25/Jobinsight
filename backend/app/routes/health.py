from fastapi import APIRouter, HTTPException, status
from app.schemas.responses import HealthResponse, ModelInfoResponse
from app.services.salary_service import salary_service

router = APIRouter(tags=["Health & Model Info"])

@router.get("/health", response_model=HealthResponse, status_code=status.HTTP_200_OK)
async def health_check():
    """
    Checks backend health and confirms whether ML and NLP pipelines are ready.
    """
    return {
        "status": "healthy",
        "model_loaded": salary_service.is_loaded(),
        "nlp_ready": True,
        "version": "1.0.0"
    }

@router.get("/api/model-info", response_model=ModelInfoResponse, status_code=status.HTTP_200_OK)
async def get_model_info():
    """
    Returns actual training metrics, evaluation comparison, feature schemas, and metadata.
    """
    if not salary_service.metadata:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Model metadata is not available."
        )
    return salary_service.metadata
