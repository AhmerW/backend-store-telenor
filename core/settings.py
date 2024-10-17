from typing import Final

from pydantic_settings import BaseSettings


ENV_FILE: Final[str] = ".env"


class AppSettings(BaseSettings):
    """
    Should load all additional settings from
    the project's ENV_FILE into this class.
    """

    PROJECT_NAME: str = "fastapi-app"
    LOGGER_NAME: str = "uvicorn.access"

    # Postgres DNS Url
    PG_DSN: str = ""

    class Config:
        env_file = ENV_FILE


class DevSettings(BaseSettings):
    """
    Configuration settings for the development environment
    """

    HOST: str = "localhost"
    PORT: int = 8000


APP_SETTINGS: Final[AppSettings] = AppSettings()
DEV_SETTINGS: Final[DevSettings] = DevSettings()
