from pydantic import BaseModel

from ._base import BaseResponse
from pxolly_api.enums import AccountType


class AccountGetInfoResponse(BaseResponse):
    response: AccountGetInfo


class AccountGetInfo(BaseModel):
    user_id: int
    account_type: AccountType
    vk_added: int
    balance: int
