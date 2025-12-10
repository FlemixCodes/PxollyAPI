import asyncio

from pxolly_api import PxollyAPI
from pxolly_api.exceptions import PxollyAPIError


async def main():
    try:
        pxolly_api = PxollyAPI(token="token")
        response = await pxolly_api.account.get_info()
        print(response)
    except PxollyAPIError as error:
        print(f"Ошибка: {error}")
    finally:
        await pxolly_api.close()


if __name__ == "__main__":
    asyncio.run(main())
