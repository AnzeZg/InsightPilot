"""Study-related schemas."""

from datetime import datetime

from pydantic import BaseModel, Field


class StudyCreate(BaseModel):
    """Schema for creating a study."""

    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    consent_text: str = Field(..., min_length=1)
    max_agent_turns: int = Field(default=9, ge=1, le=50)


class StudyUpdate(BaseModel):
    """Schema for updating a study."""

    title: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = Field(None, min_length=1)
    consent_text: str | None = Field(None, min_length=1)
    max_agent_turns: int | None = Field(None, ge=1, le=50)


class StudyResponse(BaseModel):
    """Schema for study response."""

    id: int
    owner_user_id: int
    title: str
    description: str
    consent_text: str
    max_agent_turns: int
    created_at: datetime

    class Config:
        from_attributes = True


class QuestionCreate(BaseModel):
    """Schema for creating a study question."""

    text: str = Field(..., min_length=1)
    sort_order: int = Field(default=0, ge=0)


class QuestionUpdate(BaseModel):
    """Schema for updating a question."""

    text: str | None = Field(None, min_length=1)


class QuestionReorder(BaseModel):
    """Schema for reordering questions."""

    question_id: int
    sort_order: int = Field(..., ge=0)


class QuestionBatchReorder(BaseModel):
    """Schema for batch reordering questions."""

    updates: list[QuestionReorder]


class QuestionResponse(BaseModel):
    """Schema for question response."""

    id: int
    study_id: int
    text: str
    sort_order: int

    class Config:
        from_attributes = True

