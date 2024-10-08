from bson import ObjectId
from .interfaces.orders_repository import OrdersRepositoryInterface

class OrdersRepository(OrdersRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_order(self, order: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(order)

    def insert_list_of_orders(self, orders: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(orders)

    def select_many(self, query: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(query)

        return data

    def select_one(self, query: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one(query)

        return data

    def select_many_with_properties(self, query: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            query,
            {
                "_id": 0,
                "cupom": 0
            }
        )

        return data

    def select_by_object_id(self, object_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({ "_id": ObjectId(object_id) })
        return data

    def edit_registry(self, order_id: str, new_values: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {
                "_id": ObjectId(order_id)
            },
            {
                "$set": new_values
            }
        )

    def edit_many_registry(self, query: dict, new_values: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            query,
            {
                "$set": new_values
            }
        )

    def delete_registry(self, query: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many(query)
