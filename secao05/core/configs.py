from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/faculdade"
    # "postgresql+asyncpg://<USER>:<PASSWORD>@localhost:5432/<DATABASE>"

    class Config:
        case_sensitive = True

settings: Settings = Settings()