from pxolly_api.methods import BaseMethodCategory
from pxolly_api.models import AccountGetInfoResponse, AccountGetInfo


class AccountCategory(BaseMethodCategory):
    """Методы для работы с аккаунтом"""

    async def get_info(self) -> AccountGetInfoResponse:
        """
        Получить информацию о текущем аккаунте
        Документация: https://vk.com/app7273656#/dev/method/account.getInfo
        """
        response = await self.api.method("account.getInfo")
        return AccountGetInfoResponse(response=AccountGetInfo(**response["response"]), raw_response=response)
