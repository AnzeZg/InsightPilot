"""initial schema

Revision ID: 001
Revises: 
Create Date: 2025-10-06

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create all tables."""
    
    # Create users table
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)

    # Create sessions table
    op.create_table(
        "sessions",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.Column("expires_at", sa.DateTime(), nullable=False),
        sa.Column("csrf_secret", sa.String(length=64), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_sessions_user_id"), "sessions", ["user_id"], unique=False)

    # Create studies table
    op.create_table(
        "studies",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("owner_user_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("consent_text", sa.Text(), nullable=False),
        sa.Column("max_agent_turns", sa.Integer(), nullable=False, server_default="9"),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["owner_user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_studies_id"), "studies", ["id"], unique=False)
    op.create_index(op.f("ix_studies_owner_user_id"), "studies", ["owner_user_id"], unique=False)

    # Create study_questions table
    op.create_table(
        "study_questions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("study_id", sa.Integer(), nullable=False),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("sort_order", sa.Integer(), nullable=False, server_default="0"),
        sa.ForeignKeyConstraint(["study_id"], ["studies.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_study_questions_id"), "study_questions", ["id"], unique=False)
    op.create_index(op.f("ix_study_questions_study_id"), "study_questions", ["study_id"], unique=False)

    # Create invites table
    op.create_table(
        "invites",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("study_id", sa.Integer(), nullable=False),
        sa.Column("invite_code", sa.String(length=64), nullable=False),
        sa.Column("interviewee_email", sa.String(length=255), nullable=True),
        sa.Column("status", sa.String(length=20), nullable=False, server_default="created"),
        sa.Column("expires_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["study_id"], ["studies.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("invite_code"),
    )
    op.create_index(op.f("ix_invites_id"), "invites", ["id"], unique=False)
    op.create_index(op.f("ix_invites_study_id"), "invites", ["study_id"], unique=False)
    op.create_index(op.f("ix_invites_invite_code"), "invites", ["invite_code"], unique=True)

    # Create interviews table
    op.create_table(
        "interviews",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("study_id", sa.Integer(), nullable=False),
        sa.Column("invite_id", sa.Integer(), nullable=False),
        sa.Column("started_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.Column("completed_at", sa.DateTime(), nullable=True),
        sa.Column("agent_turns", sa.Integer(), nullable=False, server_default="0"),
        sa.ForeignKeyConstraint(["study_id"], ["studies.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["invite_id"], ["invites.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("invite_id"),
    )
    op.create_index(op.f("ix_interviews_id"), "interviews", ["id"], unique=False)
    op.create_index(op.f("ix_interviews_study_id"), "interviews", ["study_id"], unique=False)

    # Create interviewees table
    op.create_table(
        "interviewees",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("interview_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("demographics_json", postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column("consent_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["interview_id"], ["interviews.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("interview_id"),
    )
    op.create_index(op.f("ix_interviewees_id"), "interviewees", ["id"], unique=False)

    # Create messages table
    op.create_table(
        "messages",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("interview_id", sa.Integer(), nullable=False),
        sa.Column("role", sa.String(length=20), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["interview_id"], ["interviews.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_messages_id"), "messages", ["id"], unique=False)
    op.create_index(op.f("ix_messages_interview_id"), "messages", ["interview_id"], unique=False)

    # Create insights table
    op.create_table(
        "insights",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("interview_id", sa.Integer(), nullable=False),
        sa.Column("summary", sa.Text(), nullable=False),
        sa.Column("sentiment", sa.String(length=20), nullable=False),
        sa.Column("keywords_json", postgresql.JSON(astext_type=sa.Text()), nullable=False),
        sa.Column("quotes_json", postgresql.JSON(astext_type=sa.Text()), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["interview_id"], ["interviews.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("interview_id"),
    )
    op.create_index(op.f("ix_insights_id"), "insights", ["id"], unique=False)


def downgrade() -> None:
    """Drop all tables."""
    op.drop_index(op.f("ix_insights_id"), table_name="insights")
    op.drop_table("insights")
    
    op.drop_index(op.f("ix_messages_interview_id"), table_name="messages")
    op.drop_index(op.f("ix_messages_id"), table_name="messages")
    op.drop_table("messages")
    
    op.drop_index(op.f("ix_interviewees_id"), table_name="interviewees")
    op.drop_table("interviewees")
    
    op.drop_index(op.f("ix_interviews_study_id"), table_name="interviews")
    op.drop_index(op.f("ix_interviews_id"), table_name="interviews")
    op.drop_table("interviews")
    
    op.drop_index(op.f("ix_invites_invite_code"), table_name="invites")
    op.drop_index(op.f("ix_invites_study_id"), table_name="invites")
    op.drop_index(op.f("ix_invites_id"), table_name="invites")
    op.drop_table("invites")
    
    op.drop_index(op.f("ix_study_questions_study_id"), table_name="study_questions")
    op.drop_index(op.f("ix_study_questions_id"), table_name="study_questions")
    op.drop_table("study_questions")
    
    op.drop_index(op.f("ix_studies_owner_user_id"), table_name="studies")
    op.drop_index(op.f("ix_studies_id"), table_name="studies")
    op.drop_table("studies")
    
    op.drop_index(op.f("ix_sessions_user_id"), table_name="sessions")
    op.drop_table("sessions")
    
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")

