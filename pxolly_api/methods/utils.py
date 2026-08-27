from typing import Literal, overload

from ..models.utils import UtilsCheckText, UtilsGetServerTime, UtilsGetServerTimeExtended
from ..requester import PxollyRequester


class UtilsCategory:
    """Методы для работы с утилитами"""

    def __init__(self, requester: PxollyRequester) -> None:
        self.requester = requester

    async def check_text(self, text: str, dictionary: str) -> UtilsCheckText:
        """
        Проверить совпадение текста указанному словарю
        Экспериментальный метод, доступ к которому может быть не у всех
        Документация: https://vk.com/app7273656#/dev/method/utils.checkText

        :param text: Текст
        :param dictionary: Название словаря
        """
        params = {"text": text, "dictionary": dictionary}
        response = await self.requester.method("utils.checkText", params)
        return UtilsCheckText(**response)

    @overload
    async def get_server_time(self, extended: Literal[False] = ...) -> UtilsGetServerTime: ...

    @overload
    async def get_server_time(self, extended: Literal[True] = ...) -> UtilsGetServerTimeExtended: ...

    async def get_server_time(self, extended: bool = False) -> UtilsGetServerTime | UtilsGetServerTimeExtended:
        """
        Получить время сервера Pxolly
        Документация: https://vk.com/app7273656#/dev/method/utils.getServerTime

        :param extended: Вернуть подробное время
        """
        params = {"extended": extended}
        response = await self.requester.method("utils.getServerTime", params)

        if extended:
            return UtilsGetServerTimeExtended(**response["response"])
        return UtilsGetServerTime(**response)
