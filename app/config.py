from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://agrismart:agrismart_secret_2024@localhost:5432/userdb"
    DATABASE_URL_SYNC: str = "postgresql://agrismart:agrismart_secret_2024@localhost:5432/userdb"
    JWT_SECRET: str = "agrismart-jwt-super-secret-key-change-me-in-production-2024"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRY_MINUTES: int = 60
    PORT: int = 8001
    LOG_LEVEL: str = "info"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
