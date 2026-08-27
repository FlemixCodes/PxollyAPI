import json
from typing import Any, TypedDict

import httpx

from pxolly_api.exceptions import ApiError, RequestError, ResponseError


class ErrorDict(TypedDict):
    error_code: int
    error_msg: str
    error_text: str | None
    request_params: list[dict[str, str]] | None
    error_subcode: int | None
    confirmation_text: str | None


class ResponseDict(TypedDict):
    response: dict[str, Any]
    error: ErrorDict | None


class PxollyRequester:
    API_URL = "https://api.pxolly.ru/method"

    def __init__(self, token: str, version: str = "2.5", http_client: httpx.AsyncClient | None = None) -> None:
        self._token = token
        self._version = version
        self.http_client = http_client or httpx.AsyncClient(base_url=self.API_URL)
        self._base_params = {"v": self._version, "access_token": self._token}

    async def method(self, method: str, params: dict[str, Any] | None = None) -> ResponseDict:
        method_params = params or {}
        finally_params = {**self._base_params, **method_params}
        response = await self.http_client.get(method, params=finally_params)

        try:
            data: ResponseDict = response.json()
            error: ErrorDict | None = data.get("error")
        except json.JSONDecodeError as exception:
            raise ResponseError(f"Invalid response: {exception}")

        if response.status_code in (httpx.codes.NOT_FOUND, httpx.codes.FORBIDDEN):
            raise RequestError(f"Invalid request: {error}")

        if error:
            raise ApiError(
                error_code=error["error_code"],
                error_msg=error["error_msg"],
                error_text=error.get("error_text"),
                request_params=error.get("request_params"),
            )

        return data

    async def execute(self, code: str) -> ResponseDict:
        params = {"code": code}
        return await self.method("execute", params)

    async def close(self) -> None:
        await self.http_client.aclose()
