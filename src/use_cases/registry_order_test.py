import pytest
from src.main.http_types.http_request import HttpRequest
from .registry_order import RegistryOrder


class OrdersRepositoryMock:
    def __init__(self) -> None:
        self.insert_document_att = {}

    def insert_order(self, document: dict) -> None:
        self.insert_document_att["document"] = document

class OrdersRepositoryMockError:
    def insert_order(self, document: dict) -> None:
        raise Exception("Error")

def test_registry():
    repository = OrdersRepositoryMock()
    registry_order = RegistryOrder(repository)

    mock_registry = HttpRequest(
        body={
            "data": {
                "name": "John Doe",
                "address": "Rua dos Bobos, 0",
                "cupom": False,
                "items": [
                    {"item": "item1", "quantity": 1},
                    {"item": "item2", "quantity": 2}
                ]
            }
        }
    )

    response = registry_order.registry(mock_registry)

    assert response.status_code == 201
    assert response.body["data"]["type"] == "order"
    assert response.body["data"]["count"] == 1

def test_registry_error():
    repository = OrdersRepositoryMockError()
    registry_order = RegistryOrder(repository)

    mock_registry = HttpRequest(
        body={
            "data": {
                "name": "John Doe",
                "address": "Rua dos Bobos, 0",
                "cupom": False,
                "items": [
                    {"item": "item1", "quantity": 1},
                    {"item": "item2", "quantity": 2}
                ]
            }
        }
    )

    response = registry_order.registry(mock_registry)

    assert response.status_code == 400

    with pytest.raises(Exception):
        raise Exception(response.body["error"])
