from pydantic import BaseModel

from pxolly_api.models import BaseResponse
from pxolly_api.enums import FormattingEntityType, ChatMemberStatus


class ChatBanMemberResponse(BaseResponse):
    response: int


class ChatEditTitleResponse(BaseResponse):
    response: int


class ChatGetByIDResponse(BaseResponse):
    response: ChatGetByID | list


class ChatGetByID(BaseModel):
    id: str
    title: str
    photo: str | None
    members_count: int | None
    is_gold: int
    owner_id: int
    admin_ids: list[int] | None
    bot_ids: list[int] | None
    role: int | None
    immune: int | None
    warns: int | None
    max_warns: int


class ChatGetMembersResponse(BaseResponse):
    response: list[ChatMember]


class ChatMember(BaseModel):
    id: int
    role: int
    immune: int | None
    status: ChatMemberStatus
    warns: int | None
    messages: int
    ban_expire: int | None
    mute_expire: int | None


class ChatGetRolesResponse(BaseResponse):
    response: list[ChatRole]


class ChatRole(BaseModel):
    name: str
    role_id: str


class ChatGetRulesResponse(BaseResponse):
    response: ChatGetRules


class ChatGetRules(BaseModel):
    text: str
    entities: list[FormattingEntityType]
    owner_id: int


class ChatFormattingEntity(BaseModel):
    type: FormattingEntityType
    offset: int
    length: int
    url: str = None


class ChatSendMessageResponse(BaseResponse):
    response: int


class ChatSetMemberRoleResponse(BaseResponse):
    response: int


class ChatSetSilenceModeResponse(BaseResponse):
    response: int
