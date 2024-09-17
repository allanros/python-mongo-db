from .orders_repository import OrdersRepository

class CollectionMock:
    def __init__(self) -> None:
        self.insert_one_att = {}
        self.find_att = {}
        self.update_att = {}

    def insert_one(self, order: dict) -> None:
        self.insert_one_att["dict"] = order

    def find(self, *args):
        self.find_att["args"] = args

    def update_many(self, *args):
        self.update_att["args"] = args

class DbCollectionMock:
    def __init__(self, collection) -> None:
        self.get_collection_att = {}
        self.collection = collection

    def get_collection(self, collection_name):
        self.get_collection_att["collection_name"] = collection_name
        return self.collection

def test_insert_order():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    order = { "order_id": 1 }
    repo.insert_order(order)
    response = collection.insert_one_att["dict"]

    assert response == order

def test_select_many_with_properties():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    doc = { "order_id": 1 }
    repo.select_many_with_properties(doc)

    assert collection.find_att["args"][0] == doc
    assert collection.find_att["args"][1] == {"_id": 0, "cupom": 0}

def test_edit_registry():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    doc = { "order_id": 1 }
    values = { "name": "alter" }

    repo.edit_registry(doc, values)

    assert collection.update_att["args"][0] == doc
    assert collection.update_att["args"][1] == {'$set': values}
