import os

import pytest
import dotenv

from pxolly_api import PxollyAPI

dotenv.load_dotenv()


@pytest.fixture()
def pxolly_api() -> PxollyAPI:
    api = PxollyAPI(os.getenv("PXOLLY_TOKEN"))
    return api
