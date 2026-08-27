from ..models.account import AccountGetInfo
from ..requester import PxollyRequester


class AccountCategory:
    """Методы для работы с аккаунтом"""

    def __init__(self, requester: PxollyRequester) -> None:
        self.requester = requester

    async def get_info(self) -> AccountGetInfo:
        """
        Получить информацию о текущем аккаунте
        Документация: https://vk.com/app7273656#/dev/method/account.getInfo
        """
        response = await self.requester.method("account.getInfo")
        return AccountGetInfo(**response["response"])
