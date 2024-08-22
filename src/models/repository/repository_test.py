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

@pytest.mark.skip('integration test')
def test_select_many():
    orders_repository = OrdersRepository(conn)
    query = {
        "cupom": False
    }
    orders = orders_repository.select_many(query)

    print(f"\nOrders: {orders}")

    for doc in orders:
        print(doc)

@pytest.mark.skip('integration test')
def test_select_one():
    orders_repository = OrdersRepository(conn)
    query = {
        "cupom": False
    }
    order = orders_repository.select_many(query)

    print(f"\nOrders: {order}")

    for doc in order:
        print(doc['client'])

@pytest.mark.skip('integration test')
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    orders = orders_repository.select_many_with_properties('')

    for doc in orders:
        print(doc)

@pytest.mark.skip('integration test')
def test_edit_registry():
    orders_repository = OrdersRepository(conn)
    query = {
        "cupom": False
    }
    new_values = {
        "cupom": True
    }
    orders_repository.edit_registry(query, new_values)

    orders = orders_repository.select_many(query)

    for doc in orders:
        print(doc)

def test_delete_registry():
    orders_repository = OrdersRepository(conn)
    query = {
        "cupom": False
    }

    orders_repository.delete_registry(query)
