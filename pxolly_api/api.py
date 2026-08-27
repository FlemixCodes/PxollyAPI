from types import TracebackType
from typing import Any

import niquests

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

    def __init__(self, token: str, version: str = "2.5", session: niquests.AsyncSession | None = None) -> None:
        """
        :param token: Токен доступа
        :param version: Версия
        :param session: Сессия niquests.AsyncSession
        """

        self._requester = PxollyRequester(token, version, session)
        self._account = AccountCategory(self._requester)
        self._callback = CallbackCategory(self._requester)
        self._chats = ChatsCategory(self._requester)
        self._database = DatabaseCategory(self._requester)
        self._users = UsersCategory(self._requester)
        self._utils = UtilsCategory(self._requester)

    @property
    def account(self) -> AccountCategory:
        """Категория методов для работы с аккаунтом"""
        return self._account

    @property
    def callback(self) -> CallbackCategory:
        """Категория методов для работы с Callback API сервером"""
        return self._callback

    @property
    def chats(self) -> ChatsCategory:
        """Категория методов для работы с чатами"""
        return self._chats

    @property
    def database(self) -> DatabaseCategory:
        """Категория методов для работы с базами данных"""
        return self._database

    @property
    def users(self) -> UsersCategory:
        """Категория методов для работы с пользователями"""
        return self._users

    @property
    def utils(self) -> UtilsCategory:
        """Категория методов для работы с утилитами"""
        return self._utils

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
        return await self._requester.method(method, params)

    async def execute(self, code: str) -> dict[str, Any]:
        """
        Выполнить несколько методов API
        Документация: https://vk.com/app7273656#/dev/method/execute

        :param code: Код запросов
        :return: dict
        """
        return await self._requester.execute(code)

    async def close(self) -> None:
        """Закрыть соединение с API"""
        await self._requester.close()
