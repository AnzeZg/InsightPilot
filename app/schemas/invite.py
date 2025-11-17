"""Invite-related schemas."""

from datetime import datetime

from pydantic import BaseModel, EmailStr


class InviteCreate(BaseModel):
    """Schema for creating an invite."""

    interviewee_email: EmailStr | None = None
    expires_at: datetime | None = None


class InviteResponse(BaseModel):
    """Schema for invite response."""

    id: int
    study_id: int
    invite_code: str
    interviewee_email: str | None
    status: str
    expires_at: datetime | None
    created_at: datetime

    class Config:
        from_attributes = True
