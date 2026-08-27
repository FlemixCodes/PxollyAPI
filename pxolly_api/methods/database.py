from pxolly_api.enums import DatabaseID
from pxolly_api.models.database import DatabaseGet
from pxolly_api.requester import PxollyRequester


class DatabaseCategory:
    """Методы для работы с базами данных"""

    def __init__(self, requester: PxollyRequester) -> None:
        self.requester = requester

    async def get(
        self,
        database_id: DatabaseID,
        user_ids: str,
        allow_fakes: bool,
        key: str | None = None,
    ) -> DatabaseGet:
        """
        Получить данные из базы данных
        Документация: https://vk.com/app7273656#/dev/method/database.get

        :param database_id: ID базы данных
        :param user_ids: ID пользователей
        :param allow_fakes: Разрешить использование фейковых данных
        :param key: Ключ для снятия ограничений
        """
        params = {"database_id": database_id, "user_ids": user_ids, "allow_fakes": allow_fakes, "key": key}
        response = await self.requester.method("database.get", params)
        return DatabaseGet(**response)
