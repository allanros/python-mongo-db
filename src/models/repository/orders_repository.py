class OrdersRepository:
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
