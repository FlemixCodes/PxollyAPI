from pydantic import BaseModel

from pxolly_api.models import BaseResponse


class GetUserRegisterdDateResponse(BaseResponse):
    response: GetUserRegisterdDate


class GetUserRegisterdDate(BaseModel):
    id: int
    registered: int


class GetUserStickerPacksResponse(BaseResponse):
    response: GetUserStickerPacks


class GetUserStickerPacks(BaseModel):
    name: str
    total_count: int
    amount: UserStickerPacksAmount
    free: UserStickerPacksCategory
    paid: UserStickerPacksCategory
    collectible: UserStickerPacksCategory


class UserStickerPacksAmount(BaseModel):
    rubles: int
    vk_votes: int


class UserStickerPacksCategory(BaseModel):
    count: int
    animated_count: int | None
    pack_titles: list[str] | None
