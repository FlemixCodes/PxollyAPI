from functools import cached_property
from types import TracebackType
from typing import Any

import httpx

from pxolly_api.methods import (
    AccountCategory,
    CallbackCategory,
    ChatsCategory,
    DatabaseCategory,
    UsersCategory,
    UtilsCategory,
)
from pxolly_api.requester import PxollyRequester


class PxollyAPI:
    """Клиент для взаимодействия с API чат менеджера Pxolly"""

    def __init__(self, token: str, version: str = "2.5", http_client: httpx.AsyncClient | None = None) -> None:
        """
        :param token: Токен доступа
        :param version: Версия
        :param http_client: HTTP клиент httpx.AsyncClient
        """

        self.requester = PxollyRequester(token, version, http_client)

    @cached_property
    def account(self) -> AccountCategory:
        """Категория методов для работы с аккаунтом"""
        return AccountCategory(self.requester)

    @cached_property
    def callback(self) -> CallbackCategory:
        """Категория методов для работы с Callback API сервером"""
        return CallbackCategory(self.requester)

    @cached_property
    def chats(self) -> ChatsCategory:
        """Категория методов для работы с чатами"""
        return ChatsCategory(self.requester)

    @cached_property
    def database(self) -> DatabaseCategory:
        """Категория методов для работы с базами данных"""
        return DatabaseCategory(self.requester)

    @cached_property
    def users(self) -> UsersCategory:
        """Категория методов для работы с пользователями"""
        return UsersCategory(self.requester)

    @cached_property
    def utils(self) -> UtilsCategory:
        """Категория методов для работы с утилитами"""
        return UtilsCategory(self.requester)

    async def __aenter__(self) -> "PxollyAPI":
        return self

    async def __aexit__(self, type: type[BaseException], value: BaseException, traceback: TracebackType) -> None:
        await self.close()

    async def method(self, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Вызвать метод API

        :param method: Название метода
        :param params: Параметры запроса
        :return: dict
        """
        return await self.requester.method(method, params)

    async def execute(self, code: str) -> dict[str, Any]:
        """
        Выполнить несколько методов API
        Документация: https://vk.com/app7273656#/dev/method/execute

        :param code: Код запросов
        :return: dict
        """
        return await self.requester.execute(code)

    async def close(self) -> None:
        """Закрыть соединение с API"""
        await self.requester.close()
