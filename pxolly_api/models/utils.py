from pydantic import BaseModel

from pxolly_api.models import BaseResponse


class UtilsGetServerTimeResponse(BaseResponse):
    response: int | UtilsGetServerTimeExtended


class UtilsGetServerTimeExtended(BaseResponse):
    seconds: int
    milliseconds: int
