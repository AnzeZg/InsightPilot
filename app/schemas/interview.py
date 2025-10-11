"""Pydantic schemas for interview-related models."""

from datetime import datetime

from pydantic import BaseModel, EmailStr


class ConsentForm(BaseModel):
    """Schema for consent form submission."""

    agreed: bool


class IntakeForm(BaseModel):
    """Schema for intake form submission."""

    name: str
    email: EmailStr
    age_range: str | None = None
    location: str | None = None
    occupation: str | None = None


class MessageResponse(BaseModel):
    """Schema for chat message response."""

    id: int
    interview_id: int
    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class IntervieweeResponse(BaseModel):
    """Schema for interviewee information."""

    id: int
    interview_id: int
    name: str
    email: str
    demographics_json: dict | None = None
    consent_at: datetime

    class Config:
        from_attributes = True


class InsightResponse(BaseModel):
    """Schema for interview insights."""

    id: int
    interview_id: int
    summary: str
    sentiment: str
    keywords_json: list
    quotes_json: list
    created_at: datetime

    class Config:
        from_attributes = True


class InterviewListItem(BaseModel):
    """Schema for interview in list view."""

    id: int
    study_id: int
    started_at: datetime
    completed_at: datetime | None
    agent_turns: int
    interviewee: IntervieweeResponse | None = None
    insight: InsightResponse | None = None
    message_count: int = 0

    class Config:
        from_attributes = True


class InterviewDetailResponse(BaseModel):
    """Schema for detailed interview view with full transcript."""

    id: int
    study_id: int
    started_at: datetime
    completed_at: datetime | None
    agent_turns: int
    interviewee: IntervieweeResponse | None = None
    messages: list[MessageResponse] = []
    insight: InsightResponse | None = None

    class Config:
        from_attributes = True


class SentimentDistribution(BaseModel):
    """Sentiment distribution across interviews."""

    positive: int = 0
    neutral: int = 0
    negative: int = 0
    total: int = 0


class KeywordFrequency(BaseModel):
    """Keyword with frequency count."""

    keyword: str
    count: int


class DemographicBreakdown(BaseModel):
    """Demographic breakdown for a specific field."""

    field: str
    values: dict[str, int]  


class ResponseMetrics(BaseModel):
    """Aggregate response metrics."""

    avg_message_count: float = 0.0
    avg_response_length: float = 0.0
    avg_conversation_length: float = 0.0
    total_messages: int = 0


class InterviewTimeline(BaseModel):
    """Timeline data point for interviews."""

    date: str  # YYYY-MM-DD
    completed: int
    in_progress: int


class StudyAnalytics(BaseModel):
    """Aggregated analytics for a study."""

    study_id: int
    study_title: str
    total_interviews: int
    completed_interviews: int
    sentiment_distribution: SentimentDistribution
    top_keywords: list[KeywordFrequency]
    response_metrics: ResponseMetrics
    demographics: list[DemographicBreakdown]
    timeline: list[InterviewTimeline]
    sample_quotes: list[str]
