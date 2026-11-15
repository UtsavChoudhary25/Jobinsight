from fastapi import APIRouter, HTTPException, status
from app.schemas.requests import SkillExtractionRequest
from app.schemas.responses import SkillExtractionResponse
from app.services.nlp_service import nlp_extractor

router = APIRouter(prefix="/api", tags=["NLP Skill Extraction"])

@router.post("/extract-skills", response_model=SkillExtractionResponse, status_code=status.HTTP_200_OK)
async def extract_skills(request: SkillExtractionRequest):
    """
    Accepts arbitrary job description text, performs n-gram phrase matching,
    extracts categorized technical skills, soft competencies, experience requirements,
    and credential degrees.
    """
    try:
        results = nlp_extractor.extract(request.description)
        return results
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"NLP extraction error: {str(e)}"
        )
