from pxolly_api.methods import BaseMethodCategory
from pxolly_api.models import DatabaseGetIris, DatabaseGetResponse
from pxolly_api.enums import DatabaseID


class DatabaseCategory(BaseMethodCategory):
    """Методы для работы с базами данных"""

    async def get(self, database_id: DatabaseID, user_ids: str, allow_fakes: bool, key: str | None = None) -> DatabaseGetResponse:
        """
        Получить данные из базы данных
        Документация: https://vk.com/app7273656#/dev/method/database.get

        :param database_id: ID базы данных
        :param user_ids: ID пользователей
        :param allow_fakes: Разрешить использование фейковых данных
        :param key: Ключ для снятия ограничений
        """
        params = {"database_id": database_id, "user_ids": user_ids, "allow_fakes": allow_fakes, "key": key}
        response = await self.api.method("database.get", params)
        return DatabaseGetResponse(response=[DatabaseGetIris(**iris) for iris in response["response"]], raw_response=response)
