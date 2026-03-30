"""
MedConcierge — Centralized Configuration
All settings loaded from environment variables / .env file.
Never hard-code secrets. Never commit .env.
"""

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List


class Settings(BaseSettings):
    # ── App
    APP_ENV: str = Field(default="development")
    DEBUG: bool = Field(default=False)

    # ── CORS
    CORS_ORIGINS: List[str] = Field(default=["http://localhost:3000"])

    # ── LLM — Primary: Gemini 2.0 Flash
    GEMINI_API_KEY: str = Field(default="")
    GEMINI_MODEL: str = Field(default="gemini-2.0-flash")
    GEMINI_MAX_TOKENS: int = Field(default=1024)

    # ── LLM — Fallback: Groq (Llama 3.3)
    GROQ_API_KEY: str = Field(default="")
    GROQ_MODEL: str = Field(default="llama-3.3-70b-versatile")

    # ── Google Places API
    GOOGLE_PLACES_API_KEY: str = Field(default="")

    # ── Serper (Web Search Fallback)
    SERPER_API_KEY: str = Field(default="")

    # ── Supabase
    SUPABASE_URL: str = Field(default="")
    SUPABASE_ANON_KEY: str = Field(default="")
    SUPABASE_SERVICE_ROLE_KEY: str = Field(default="")

    # ── Upstash Redis
    UPSTASH_REDIS_REST_URL: str = Field(default="")
    UPSTASH_REDIS_REST_TOKEN: str = Field(default="")
    REDIS_SESSION_TTL_SECONDS: int = Field(default=86400)
    REDIS_MAX_HISTORY_MESSAGES: int = Field(default=20)

    # ── Cloudinary
    CLOUDINARY_CLOUD_NAME: str = Field(default="")
    CLOUDINARY_API_KEY: str = Field(default="")
    CLOUDINARY_API_SECRET: str = Field(default="")

    # ── Clerk
    CLERK_SECRET_KEY: str = Field(default="")
    CLERK_PUBLISHABLE_KEY: str = Field(default="")

    # ── Sentry
    SENTRY_DSN: str = Field(default="")

    # ── Insurance PDF Parser
    PDF_MAX_CHARS: int = Field(default=8000)
    PDF_MAX_FILE_SIZE_MB: int = Field(default=10)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()