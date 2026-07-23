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

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()