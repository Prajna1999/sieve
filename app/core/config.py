from pydantic import BaseSettings, AnyHttpUrl
from typing import List, Optional


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "CivicFlow"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    NEON_HOST: str
    NEON_DB: str
    NEON_USER: str
    NEON_PASSWORD: str
    NEON_ENDPOINT_ID: str

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.NEON_USER}:{self.NEON_PASSWORD}@{self.NEON_HOST}/{self.NEON_DB}?options=endpoint%3D{self.NEON_ENDPOINT_ID}"

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
