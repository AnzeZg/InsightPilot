"""Interview schemas for forms and validation."""

from pydantic import BaseModel, EmailStr, Field


class ConsentForm(BaseModel):
    """Form data for consent submission."""

    agreed: bool = Field(..., description="User has agreed to consent")


class IntakeForm(BaseModel):
    """Form data for interviewee intake."""

    name: str = Field(..., min_length=1, max_length=255, description="Full name of interviewee")
    email: EmailStr = Field(..., description="Email address of interviewee")
    demographics: dict | None = Field(
        default=None, description="Optional demographics data as JSON"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jane@example.com",
                "demographics": {"age_range": "25-34", "location": "US"},
            }
        }

