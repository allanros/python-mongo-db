from datetime import datetime
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.models.repository.interfaces.orders_repository import OrdersRepositoryInterface

class RegistryOrder:
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body =  http_request.body
            new_order = self.__format_new_order(body)
            self.__registry_order(new_order)

            return self.__format_response(new_order)

        except Exception as exc:
            return HttpResponse(
                body= {
                    "error": exc
                },
                status_code=400
            )


    def __format_new_order(self, body: dict) -> dict:
        new_order = body["data"]
        new_order = { **new_order, "created_at": datetime.now() }
        return new_order

    def __registry_order(self, new_order: dict) -> None:
        self.__orders_repository.insert_order(new_order)

    def __format_response(self, new_order: dict) -> dict:
        return HttpResponse(
            body={
                "data": {
                    "type": "order",
                    "count": 1,
                    "registry": True
                },
                "order_data": new_order
            },
            status_code=201
        )
