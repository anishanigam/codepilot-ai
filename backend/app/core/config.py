from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str

    APP_VERSION: str

    MONGODB_URI: str

    DATABASE_NAME: str

    JWT_SECRET: str

    JWT_ALGORITHM: str

    JWT_EXPIRE_DAYS: int

    GITHUB_CLIENT_ID: str = ""

    GITHUB_CLIENT_SECRET: str = ""

    FRONTEND_URL: str

    AI_REQUEST_TIMEOUT: int = 20

    AI_MAX_RETRIES: int = 2

    AI_MAX_CONCURRENT_TASKS: int = 4

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

    GROQ_API_KEY: str
    
    GROQ_MODEL: str = "llama-3.3-70b-versatile"


settings = Settings()