import pytest

from pxolly_api import PxollyAPI
from pxolly_api.enums import DatabaseID
from pxolly_api.models import AccountGetInfoResponse, DatabaseGetResponse


class TestPxollyAPIMethods:
    @pytest.mark.asyncio
    async def test_account_get_info(self, pxolly_api: PxollyAPI):
        response = await pxolly_api.account.get_info()
        assert isinstance(response, AccountGetInfoResponse)

    @pytest.mark.asyncio
    async def test_database_get(self, pxolly_api: PxollyAPI):
        response = await pxolly_api.database.get(DatabaseID.IRIS, "733772362", True)
        assert isinstance(response, DatabaseGetResponse)
