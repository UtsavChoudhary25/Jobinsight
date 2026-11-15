from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class SalaryPredictionResponse(BaseModel):
    predicted_salary: float = Field(..., description="Estimated annual median salary in USD")
    expected_range_min: float = Field(..., description="Lower bound of 80% confidence interval")
    expected_range_max: float = Field(..., description="Upper bound of 80% confidence interval")
    percentile_rank: float = Field(..., description="Estimated percentile across LinkedIn dataset distribution")
    currency: str = "USD"
    pay_period: str = "YEARLY"
    model_name: str
    model_r2_score: float
    model_mae: float
    features_used: Dict[str, str]

class TokenStatistics(BaseModel):
    word_count: int
    character_count: int
    unique_words: int
    skill_density_pct: float

class SkillExtractionResponse(BaseModel):
    total_detected: int
    technical_skills: List[str]
    soft_skills: List[str]
    tools_and_platforms: List[str]
    domain_skills: List[str]
    experience_required: str
    degree_required: str
    inferred_category: str
    token_statistics: TokenStatistics

class ModelInfoResponse(BaseModel):
    model_name: str
    target: str
    currency: str
    total_training_records: int
    total_test_records: int
    features: List[str]
    categories: Dict[str, List[str]]
    metrics: Dict[str, float]
    comparison: Dict[str, Dict[str, float]]
    trained_date: str

class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    nlp_ready: bool
    version: str = "1.0.0"
