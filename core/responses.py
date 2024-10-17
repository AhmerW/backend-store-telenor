from typing import Any, Dict, Optional

from fastapi.responses import JSONResponse
from fastapi.encoders import  jsonable_encoder
from pydantic import BaseModel


class Response(BaseModel):
    msg: str
    data: Dict[str, Any] = dict()
    error: Dict[str, Any] = dict()


class Success(JSONResponse):
    def __init__(
        self,
            data=None,
        msg: str = "success",
        status_code: int = 200,
        **kwargs,
    ):
        super().__init__(
            jsonable_encoder(dict(
                msg=msg,
                error=dict(),
                data=data,
            )),
            status_code=status_code,
            **kwargs,
        )
        if data is None:
            data = {}


class Error(JSONResponse):
    def __init__(
        self,
        status_code: int,
        error_msg: str,
        error_code: Optional[int] = None,
        data: Optional[Dict[Any, Any]] = dict(),
        **kwargs,
    ) -> None:
        return super().__init__(
            dict(
                msg="Error",
                error=dict(
                    msg=error_msg,
                    code=error_code,
                ),
                data=data,
            ),
            status_code=status_code,
            **kwargs,
        )
