from pydantic import BaseModel

from ._base import BaseResponse
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
    photo: str
    members_count: int
    is_gold: int
    owner_id: int
    admin_ids: list[int]
    bot_ids: list[int]
    role: int
    immune: int
    warns: int
    max_warns: int


class ChatGetMembersResponse(BaseResponse):
    response: list[ChatMember]


class ChatMember(BaseModel):
    id: int
    role: int
    immune: int
    status: ChatMemberStatus
    warns: int
    messages: int
    ban_expire: int
    mute_expire: int


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
