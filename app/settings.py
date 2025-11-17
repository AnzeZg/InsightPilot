"""Application settings and configuration."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    app_env: str = Field(default="dev", description="Application environment (dev/staging/prod)")

    # Security
    secret_key: str = Field(
        ..., description="Secret key for signing sessions and tokens (required)"
    )
    session_cookie_name: str = Field(default="ip_session", description="Name of the session cookie")

    # Database
    database_url: str = Field(..., description="PostgreSQL connection URL (required)")

    # LLM (to be used in later days)
    openai_api_key: str | None = Field(default=None, description="OpenAI API key")
    anthropic_api_key: str | None = Field(default=None, description="Anthropic API key")

    # Email (optional, for later)
    resend_api_key: str | None = Field(default=None, description="Resend email API key")
    mailgun_api_key: str | None = Field(default=None, description="Mailgun API key")

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )

    @property
    def is_production(self) -> bool:
        """Check if running in production."""
        return self.app_env.lower() == "prod"

    @property
    def is_development(self) -> bool:
        """Check if running in development."""
        return self.app_env.lower() == "dev"


settings = Settings()
