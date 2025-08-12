from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@db:5432/balance"
    SERVICE_JWT_SECRET: str = "change-me-in-prod"
    EXPIRY_WORKER_INTERVAL: int = 5  # seconds

    class Config:
        env_file = ".env"

settings = Settings()
