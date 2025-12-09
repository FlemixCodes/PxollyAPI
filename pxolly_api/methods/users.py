from pxolly_api.methods import BaseMethodCategory
from pxolly_api.models import (
    GetUserRegisterdDate,
    GetUserRegisterdDateResponse,
    UserStickerPacksCategory,
    UserStickerPacksAmount,
    GetUserStickerPacksResponse,
    GetUserStickerPacks,
)


class UsersCategory(BaseMethodCategory):
    """Методы для работы с пользователями"""

    async def get_registered_date(self, user_ids: list[int]) -> GetUserRegisterdDateResponse:
        """
        Получить дату регистрации пользователей
        Документация: https://vk.com/app7273656#/dev/method/users.getRegisteredDate

        :param user_ids: ID пользователей
        """
        params = {"user_ids": user_ids}
        response = await self.api.method("users.getRegisteredDate", params)
        return GetUserRegisterdDateResponse(response=[GetUserRegisterdDate(**user) for user in response["response"]])

    async def get_sticker_packs(self, user_id: int, max_count: int, need_titles: bool = False) -> GetUserStickerPacksResponse:
        """
        Получить список стикер паков пользователя
        Документация: https://vk.com/app7273656#/dev/method/users.getStickerPacks

        :param user_id: ID пользователя
        :param max_count: Максимальное количество паков
        :param need_titles: Получить названия пакетов
        """
        params = {"user_id": user_id, "max_count": max_count, "need_titles": need_titles}
        response = await self.api.method("users.getUserStickerPacks", params)

        amount = UserStickerPacksAmount(
            rubles=response["response"]["amount"]["rubles"],
            vk_votes=response["response"]["amount"]["vk_votes"],
        )

        free = UserStickerPacksCategory(
            count=response["response"]["free"]["count"],
            items=response["response"]["free"]["items"],
        )

        paid = UserStickerPacksCategory(
            count=response["response"]["paid"]["count"],
            items=response["response"]["paid"]["items"],
        )

        collectible = UserStickerPacksCategory(
            count=response["response"]["collectible"]["count"],
            items=response["response"]["collectible"]["items"],
        )

        model_response = GetUserStickerPacks(
            name=response["response"]["name"],
            total_count=response["response"]["total_count"],
            amount=amount,
            free=free,
            paid=paid,
            collectible=collectible,
        )

        return GetUserStickerPacksResponse(response=model_response, raw_response=response)
