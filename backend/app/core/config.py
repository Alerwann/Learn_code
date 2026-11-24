from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Application
    APP_ENV: str = "development"
    APP_DEBUG: bool = True

    # MySQL (PyMySQL)
    MYSQL_HOST: str = "mysql"
    MYSQL_PORT: int = 3306
    MYSQL_DATABASE: str = "codelearn"
    MYSQL_USER: str = "Learner"
    MYSQL_PASSWORD: str

    # MongoDB (PyMongo)
    MONGO_HOST: str = "mongo"
    MONGO_PORT: int = 27017
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_INITDB_DATABASE: str = "codelearn"
    MONGO_URI: str | None = None


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
