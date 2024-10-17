from typing import Final

from fastapi import FastAPI

from core.settings import APP_SETTINGS
from core.responses import Success


from fastapi.middleware.cors import CORSMiddleware
app: Final[FastAPI] = FastAPI(
    title=APP_SETTINGS.PROJECT_NAME,
    default_response_class=Success,
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



