from pydantic import BaseModel

from pxolly_api.enums import AccountType


class AccountGetInfo(BaseModel):
    """Информация о текущем аккаунте"""

    user_id: int
    account_type: AccountType
    vk_added: int
    balance: int
