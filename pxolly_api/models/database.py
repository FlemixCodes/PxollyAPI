from pydantic import BaseModel


class DatabaseGetIrisMember(BaseModel):
    """Участник базы данных Iris"""

    user_id: int
    last_banned: int
    spam_count: int | None = None
    text: str | None = None
    is_fake: int | None = None
    comment: str | None = None


class DatabaseGetIris(BaseModel):
    """База данных Iris"""

    count: int
    items: list[DatabaseGetIrisMember]


class DatabaseGet(BaseModel):
    """База данных"""

    response: DatabaseGetIris
