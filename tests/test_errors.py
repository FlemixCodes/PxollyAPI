import pytest

from pxolly_api import PxollyAPI
from pxolly_api.exceptions import PxollyAPIError


class TestPxollyAPIError:
    @pytest.mark.asyncio
    async def test_invalid_method(self, pxolly_api: PxollyAPI):
        with pytest.raises(PxollyAPIError):
            await pxolly_api.method("invalid_method")

    @pytest.mark.asyncio
    async def test_invalid_version(self, pxolly_api: PxollyAPI):
        with pytest.raises(PxollyAPIError):
            pxolly_api._version = "invalid_version"
            await pxolly_api.method("account.get_info")
