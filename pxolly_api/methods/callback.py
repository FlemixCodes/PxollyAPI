from pxolly_api.models.callback import (
    CallbackEditSettings,
    CallbackGetConfirmationCode,
    CallbackGetSettings,
    CallbackSetBotPrefix,
)
from pxolly_api.requester import PxollyRequester


class CallbackCategory:
    """Методы для работы с Callback API сервером"""

    def __init__(self, requester: PxollyRequester) -> None:
        self.requester = requester

    async def get_settings(self) -> CallbackGetSettings:
        """
        Получить настройки Callback API текущего аккаунта
        Документация: https://vk.com/app7273656#/dev/method/callback.getSettings
        """
        response = await self.requester.method("callback.getSettings")
        return CallbackGetSettings(**response["response"])

    async def get_confirmation_code(self) -> CallbackGetConfirmationCode:
        """
        Получить код для подтверждения Callback API
        Документация: https://vk.com/app7273656#/dev/method/callback.getConfirmationCode
        """
        response = await self.requester.method("callback.getConfirmationCode")
        return CallbackGetConfirmationCode(**response["response"])

    async def edit_settings(self, url: str, secret_key: str, is_hidden: bool) -> CallbackEditSettings:
        """
        Изменить настройки Callback API
        Документация: https://vk.com/app7273656#/dev/method/callback.editSettings

        :param url: Ссылка на Callback API
        :param secret_key: Секретный ключ
        :param is_hidden: Скрыть адрес сервера Callback API
        """
        params = {"url": url, "secret_key": secret_key, "is_hidden": is_hidden}
        response = await self.requester.method("callback.editSettings", params)
        return CallbackEditSettings(**response)

    async def set_bot_prefix(self, prefix: str) -> CallbackSetBotPrefix:
        """
        Установить префикс бота для Callback API
        Документация: https://vk.com/app7273656#/dev/method/callback.setBotPrefix

        :param prefix: Префикс
        """
        params = {"prefix": prefix}
        response = await self.requester.method("callback.setBotPrefix", params)
        return CallbackSetBotPrefix(**response)
