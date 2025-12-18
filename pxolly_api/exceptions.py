class PxollyAPIError(Exception):
    """Общий класс исключений"""

    pass


class ResponseError(PxollyAPIError):
    """Ошибка при обработке ответа от API"""

    pass


class RequestError(PxollyAPIError):
    """Ошибка при неправильном запросе к API"""

    pass


class ApiError(PxollyAPIError):
    """Ошибка API при выполнении запроса"""

    def __init__(self, error_code: int, error_msg: str, error_text: str | None = None, request_params: dict | None = None):
        self.error_code = error_code
        self.error_msg = error_msg
        self.error_text = error_text
        self.request_params = request_params

    def __str__(self):
        return f"{self.error_code} ({self.error_msg})"
