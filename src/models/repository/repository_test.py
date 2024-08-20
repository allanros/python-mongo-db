import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip('integration test')
def test_insert_order():
    orders_repository = OrdersRepository(conn)
    order = {
        "alguma": "coisa",
        "valor": 5
    }
    orders_repository.insert_order(order)

@pytest.mark.skip('integration test')
def test_insert_list_of_orders():
    orders_repository = OrdersRepository(conn)
    orders = [
        {
            "alguma": "coisa",
            "valor": 5
        },
        {
            "outra": "coisa",
            "valor": 10
        }
    ]
    orders_repository.insert_list_of_orders(orders)
