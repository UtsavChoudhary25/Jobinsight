from fastapi import APIRouter, HTTPException, status
from app.schemas.requests import SalaryPredictionRequest
from app.schemas.responses import SalaryPredictionResponse
from app.services.salary_service import salary_service

router = APIRouter(prefix="/api", tags=["Salary Prediction"])

@router.post("/predict-salary", response_model=SalaryPredictionResponse, status_code=status.HTTP_200_OK)
async def predict_salary(request: SalaryPredictionRequest):
    """
    Predicts expected annual compensation using the trained HistGradientBoosting regression model.
    Applies the full training pipeline including OneHotEncoding and empirical uncertainty bounds.
    """
    if not salary_service.is_loaded():
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Trained Salary ML Model is currently unavailable or loading."
        )

    try:
        result = salary_service.predict(request.model_dump())
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Inference error: {str(e)}"
        )
