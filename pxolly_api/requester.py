from typing import Any

import niquests

from pxolly_api.exceptions import ApiError, RequestError, ResponseError


class PxollyRequester:
    API_URL = "https://api.pxolly.ru/method"

    def __init__(self, token: str, version: str = "2.5", session: niquests.AsyncSession | None = None) -> None:
        self._token = token
        self._version = version
        self._session = session or niquests.AsyncSession(base_url=self.API_URL)
        self._base_params = {"v": self._version, "access_token": self._token}

    async def method(self, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        method_params = params or {}
        finally_params = {**self._base_params, **method_params}
        response = await self._session.get(method, params=finally_params)

        try:
            data: dict[str, Any] = response.json()
            error = data.get("error")
        except niquests.JSONDecodeError as error:
            raise ResponseError(f"Invalid response: {error}")

        if response.status_code in (niquests.codes.not_found, niquests.codes.forbidden):
            raise RequestError(f"Invalid request: {error}")

        if error:
            raise ApiError(
                error["error_code"], error["error_msg"], error.get("error_text"), error.get("request_params")
            )

        return data

    async def execute(self, code: str) -> dict[str, Any]:
        params = {"code": code}
        return await self.method("execute", params)

    async def close(self) -> None:
        await self._session.close()
