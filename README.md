### Pxolly API
Библиотека для взаимодействия с API чат менеджера Pxolly (https://api.pxolly.ru)

### Инструменты
* Язык: Python
* Валидация: Pydantic
* HTTP Клиент: niquests
* Тестирование: pytest
* Менеджер пакетов: UV


### Использование (example.py)
```python
import asyncio

from pxolly_api import PxollyAPI
from pxolly_api.exceptions import PxollyAPIError


# Способ 1
async def main():
    try:
        pxolly_api = PxollyAPI(token="token")
        response = await pxolly_api.account.get_info()
        print(response)
    except PxollyAPIError as error:
        print(f"Ошибка: {error}")
    finally:
        await pxolly_api.close()


# Способ 2
async def main():
    async with PxollyAPI(token="token") as pxolly_api:
        try:
            response = await pxolly_api.account.get_info()
            print(response)
        except PxollyAPIError as error:
            print(f"Ошибка: {error}")


if __name__ == "__main__":
    asyncio.run(main())

```
