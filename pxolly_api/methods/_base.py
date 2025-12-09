import typing

if typing.TYPE_CHECKING:
    from pxolly_api import PxollyAPI


class BaseMethodCategory:
    """Базовая категория методов API"""

    def __init__(self, api: "PxollyAPI") -> None:
        self.api = api
