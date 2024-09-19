from src.models.connection.connection_handler import db_connection_handler
from src.models.repository.orders_repository import OrdersRepository
from src.use_cases.registry_uptader import RegistryUpdater

def registry_updater_composer():
    connection = db_connection_handler.get_db_connection()
    model = OrdersRepository(connection)
    use_case = RegistryUpdater(model)

    return use_case
