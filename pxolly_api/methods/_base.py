from ..requester import PxollyRequester


class BaseCategory:
    """Базовая категория методов API"""

    __slots__ = ("requester",)

    def __init__(self, requester: PxollyRequester) -> None:
        self.requester = requester
