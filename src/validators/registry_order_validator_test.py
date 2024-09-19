import pytest
from .registry_order_validator import registry_order_validator

def test_registry_order_validator():
    body = {
        "data": {
            "name": "John Doe",
            "address": "Rua dos Bobos, 0",
            "cupom": False,
            "items": [
                {
                    "item": "item1",
                    "quantity": 1
                },
                {
                    "item": "item2",
                    "quantity": 2
                }
            ]
        }
    }
    registry_order_validator(body)

def test_registry_order_validator_error():
    body = {
        "data": {
            "cupom": False,
            "items": [
                {
                    "item": "item1",
                    "quantity": 1
                },
                {
                    "item": "item2",
                    "quantity": 2
                }
            ]
        }
    }

    with pytest.raises(Exception):
        registry_order_validator(body)
