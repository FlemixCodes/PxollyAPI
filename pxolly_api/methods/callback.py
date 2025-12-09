from pxolly_api.methods import BaseMethodCategory
from pxolly_api.models import (
    CallbackGetSettings,
    CallbackGetSettingsResponse,
    CallbackGetConfirmationCode,
    CallbackGetConfirmationCodeResponse,
    CallbackEditSettingsResponse,
    CallbackSetBotPrefixResponse,
)


class CallbackCategory(BaseMethodCategory):
    """Методы для работы с Callback API"""

    async def get_settings(self) -> CallbackGetSettingsResponse:
        """
        Получить настройки Callback API текущего аккаунта
        Документация: https://vk.com/app7273656#/dev/method/callback.getSettings
        """
        response = await self.api.method("callback.getSettings")
        return CallbackGetSettingsResponse(response=CallbackGetSettings(**response["response"]), raw_response=response)

    async def get_confirmation_code(self) -> CallbackGetConfirmationCodeResponse:
        """
        Получить код для подтверждения Callback API
        Документация: https://vk.com/app7273656#/dev/method/callback.getConfirmationCode
        """
        response = await self.api.method("callback.getConfirmationCode")
        return CallbackGetConfirmationCodeResponse(response=CallbackGetConfirmationCode(**response["response"]), raw_response=response)

    async def edit_settings(self, url: str, secret_key: str, is_hidden: bool) -> CallbackEditSettingsResponse:
        """
        Изменить настройки Callback API
        Документация: https://vk.com/app7273656#/dev/method/callback.editSettings

        :param url: Ссылка на Callback API
        :param secret_key: Секретный ключ
        :param is_hidden: Скрыть адрес сервера Callback API
        """
        params = {"url": url, "secret_key": secret_key, "is_hidden": is_hidden}
        response = await self.api.method("callback.editSettings", params)
        return CallbackEditSettingsResponse(response=response["response"], raw_response=response)

    async def set_bot_prefix(self, prefix: str) -> CallbackEditSettingsResponse:
        """
        Установить префикс бота для Callback API
        Документация: https://vk.com/app7273656#/dev/method/callback.setBotPrefix

        :param prefix: Префикс
        """
        params = {"prefix": prefix}
        response = await self.api.method("callback.setBotPrefix", params)
        return CallbackSetBotPrefixResponse(response=response["response"], raw_response=response)
