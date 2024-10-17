from fastapi import HTTPException
from starlette.requests import Request


from data.ctx import app
from core.log import get_logger
from core.responses import Error
from resources.products.routes import router

logger = get_logger()


@app.exception_handler(HTTPException)
async def http_exc_handler(
    _: Request,
    exc: HTTPException,
) -> Error:
    logger.info("HTTP Exception")

    return Error(
        status_code=exc.status_code,
        error_msg=str(exc.detail),
    )


# Routers

app.include_router(router)
