from pydantic import BaseModel

from pxolly_api.models import BaseResponse


class CallbackGetSettingsResponse(BaseResponse):
    response: CallbackGetSettings


class CallbackGetSettings(BaseModel):
    enabled: int
    url: str
    secret_key: str
    confirm_code: str


class CallbackGetConfirmationCodeResponse(BaseResponse):
    response: CallbackGetConfirmationCode


class CallbackGetConfirmationCode(BaseModel):
    code: str


class CallbackEditSettingsResponse(BaseResponse):
    response: dict


class CallbackSetBotPrefixResponse(BaseResponse):
    response: int
