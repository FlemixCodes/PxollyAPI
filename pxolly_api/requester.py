import json
from typing import Any

import httpx

from pxolly_api.exceptions import ApiError, RequestError, ResponseError


class PxollyRequester:
    API_URL = "https://api.pxolly.ru/method"

    def __init__(self, token: str, version: str = "2.5", session: httpx.AsyncClient | None = None) -> None:
        self._token = token
        self._version = version
        self._session = session or httpx.AsyncClient(base_url=self.API_URL)
        self._base_params = {"v": self._version, "access_token": self._token}

    async def method(self, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        method_params = params or {}
        finally_params = {**self._base_params, **method_params}
        response = await self._session.get(method, params=finally_params)

        try:
            data: dict[str, Any] = response.json()
            error: dict[str, Any] | None = data.get("error")
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

    async def execute(self, code: str) -> dict[str, Any]:
        params = {"code": code}
        return await self.method("execute", params)

    async def close(self) -> None:
        await self._session.aclose()
