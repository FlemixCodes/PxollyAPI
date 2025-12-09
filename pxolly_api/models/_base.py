from typing import Any

from pydantic import BaseModel


class BaseResponse(BaseModel):
    response: Any
    raw_response: dict
