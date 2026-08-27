from pydantic import BaseModel

from pxolly_api.enums import ChatMemberStatus, FormattingEntityType


class ChatBanMember(BaseModel):
    """Бан участника в чате"""

    response: int


class ChatEditTitle(BaseModel):
    """Изменение названия чата"""

    response: int


class Chat(BaseModel):
    """Чат"""

    id: str
    title: str
    photo: str | None = None
    members_count: int | None = None
    is_gold: int
    owner_id: int
    admin_ids: list[int] | None = None
    bot_ids: list[int] | None = None
    role: int | None = None
    immune: int | None = None
    warns: int | None = None
    max_warns: int | None = None


class ChatsGetByID(BaseModel):
    """Чаты"""

    response: list[Chat]


class ChatMember(BaseModel):
    """Участник чата"""

    id: int
    role: int
    immune: int | None = None
    status: ChatMemberStatus
    warns: int | None = None
    messages: int
    ban_expire: int | None = None
    mute_expire: int | None = None


class ChatMemberAccount(BaseModel):
    """Аккаунт участника чата"""

    id: int
    name: str
    sex: int
    photo_200: str
    screen_name: str


class ChatGetMembersById(BaseModel):
    """Участники чата"""

    response: list[ChatMember]


class ChatGetMembers(BaseModel):
    """Участники чата"""

    count: int
    items: list[ChatMember]
    accounts: list[ChatMemberAccount]


class ChatRole(BaseModel):
    """Роль чата"""

    name: str
    role_id: str


class ChatGetRoles(BaseModel):
    """Роли чата"""

    response: list[ChatRole]


class ChatFormattingEntity(BaseModel):
    """Формат текста"""

    type: FormattingEntityType
    offset: int
    length: int
    url: str | None = None


class ChatGetRules(BaseModel):
    """Правила чата"""

    text: str
    entities: list[ChatFormattingEntity]
    owner_id: int


class ChatSendMessage(BaseModel):
    """Отправка сообщения в чат"""

    response: int


class ChatSetMemberRole(BaseModel):
    """Установка роли участника чата"""

    response: int


class ChatSetSilenceMode(BaseModel):
    """Установка режима тишины чата"""

    response: int
