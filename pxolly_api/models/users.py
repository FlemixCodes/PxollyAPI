from pydantic import BaseModel


class UserRegisteredDate(BaseModel):
    """Дата регистрации пользователя"""

    id: int
    registered: int


class GetUserRegisteredDate(BaseModel):
    """Дата регистрации пользователей"""

    response: list[UserRegisteredDate]


class UserStickerPacksCategory(BaseModel):
    """Категория стикерпаков пользователя"""

    count: int
    animated_count: int | None
    pack_titles: list[str] | None


class UserStickerPacksAmount(BaseModel):
    """Цена стикерпаков пользователя"""

    rubles: int
    vk_votes: int


class GetUserStickerPacks(BaseModel):
    """Стикерпаки пользователя"""

    name: str
    total_count: int
    amount: UserStickerPacksAmount
    free: UserStickerPacksCategory
    paid: UserStickerPacksCategory
    collectible: UserStickerPacksCategory
