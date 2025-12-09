from pxolly_api.methods import BaseMethodCategory
from pxolly_api.models import UtilsGetServerTimeExtended, UtilsGetServerTimeResponse


class UtilsCategory(BaseMethodCategory):
    """
    Методы для работы с утилитами
    """

    async def get_server_time(self, extended: bool = False) -> UtilsGetServerTimeResponse:
        """
        Получить время сервера Pxolly
        Документация: https://vk.com/app7273656#/dev/method/utils.getServerTime

        :param extended: Подробный ответ
        """
        params = {"extended": extended}
        response = await self.api.method("utils.getServerTime", params)

        if extended:
            return UtilsGetServerTimeResponse(response=UtilsGetServerTimeExtended(**response["response"]), raw_response=response)
        return UtilsGetServerTimeResponse(response=response["response"], raw_response=response)
