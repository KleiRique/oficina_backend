from pydantic import BaseSettings

class Settings(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_SERVICE_KEY: str
    OPENAI_API_KEY: str
    WAHA_API_KEY: str
    WAHA_API_BASE: str = ""
    REDIS_URL: str | None = None
    ENV: str = "dev"

    class Config:
        env_file = ".env"

settings = Settings()
