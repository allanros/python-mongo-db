from src.main.http_types.http_response import HttpResponse
from .types.http_not_found import HttpNotFoundError
from .types.http_unprocessable_entity import HttpUnprocessableEntityError


def error_handler(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpUnprocessableEntityError)):
        return HttpResponse({
            "errors": [{
                "title": error.name,
                "detail": error.message
            }]
        }, error.status_code)

    return HttpResponse({
        "errors": [{
            "title": "Internal Server Error",
            "detail": str(error)
        }]
    }, 500)
