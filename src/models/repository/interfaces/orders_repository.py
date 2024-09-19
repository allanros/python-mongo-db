from abc import ABC, abstractmethod

class OrdersRepositoryInterface(ABC):
    @abstractmethod
    def insert_order(self, order: dict) -> None:
        pass

    @abstractmethod
    def insert_list_of_orders(self, orders: list) -> None:
        pass

    @abstractmethod
    def select_many(self, query: dict) -> list:
        pass

    @abstractmethod
    def select_one(self, query: dict) -> dict:
        pass

    @abstractmethod
    def select_many_with_properties(self, query: dict) -> list:
        pass

    @abstractmethod
    def select_by_object_id(self, object_id: str) -> dict:
        pass

    @abstractmethod
    def edit_many_registry(self, query: dict, new_values: dict) -> None:
        pass

    @abstractmethod
    def edit_registry(self, order_id: str, new_values: dict) -> None:
        pass

    @abstractmethod
    def delete_registry(self, query: dict) -> None:
        pass
