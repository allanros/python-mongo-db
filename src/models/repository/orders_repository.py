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
