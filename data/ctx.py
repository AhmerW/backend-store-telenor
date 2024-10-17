from typing import Final

from fastapi import FastAPI

from core.settings import APP_SETTINGS
from core.responses import Success


app: Final[FastAPI] = FastAPI(
    title=APP_SETTINGS.PROJECT_NAME,
    default_response_class=Success,
)
