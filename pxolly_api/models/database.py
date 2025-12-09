from pydantic import BaseModel

from ._base import BaseResponse


class DatabaseGetResponse(BaseResponse):
    response: list[DatabaseGetIris]


class DatabaseGetIris(BaseModel):
    user_id: int
    last_banned: int
    spam_count: int
    text: str
    is_fake: int
    comment: str
