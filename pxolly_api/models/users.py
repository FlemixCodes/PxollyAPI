from pydantic import BaseModel

from ._base import BaseResponse


class GetUserRegisterdDateResponse(BaseResponse):
    response: GetUserRegisterdDate


class GetUserRegisterdDate(BaseModel):
    id: int
    registered: int
