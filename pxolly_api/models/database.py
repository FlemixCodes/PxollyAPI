from pydantic import BaseModel

from pxolly_api.models import BaseResponse


class DatabaseGetResponse(BaseResponse):
    response: DatabaseGetIris


class DatabaseGetIris(BaseModel):
    count: int
    items: list[DatabaseGetIrisMember]


class DatabaseGetIrisMember(BaseModel):
    user_id: int
    last_banned: int
    spam_count: int | None
    text: str | None
    is_fake: int | None
    comment: str | None
