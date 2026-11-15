from pydantic import BaseModel, Field
from typing import Optional

class SalaryPredictionRequest(BaseModel):
    role_category: str = Field(
        default="Technology", 
        description="Standardized role domain (Technology, Finance, Management, Healthcare, Sales, Operations, Retail)"
    )
    formatted_experience_level: str = Field(
        default="Mid-Senior level",
        description="Experience level (Entry level, Associate, Mid-Senior level, Director, Executive, Internship, Not Specified)"
    )
    formatted_work_type: str = Field(
        default="Full-time",
        description="Work type (Full-time, Contract, Part-time, Temporary, Internship)"
    )
    location_tier: str = Field(
        default="Tier 1 (NYC, SF, Seattle, Boston)",
        description="Geographic cost tier"
    )
    remote_allowed: str = Field(
        default="1",
        description="'1' for remote, '0' for on-site/unspecified"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "role_category": "Technology",
                "formatted_experience_level": "Mid-Senior level",
                "formatted_work_type": "Full-time",
                "location_tier": "Tier 1 (NYC, SF, Seattle, Boston)",
                "remote_allowed": "1"
            }
        }

class SkillExtractionRequest(BaseModel):
    description: str = Field(
        ...,
        min_length=5,
        description="Full text of the job description to parse"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "description": "We are seeking a Senior Cloud Engineer with 5+ years of experience in distributed systems. Proficiency in Python, AWS (EC2, S3), Docker, and Kubernetes required. Bachelor's degree in Computer Science."
            }
        }
