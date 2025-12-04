from sqlalchemy.orm import Session
from models.client import ClientModel
from repositories.client_repository import ClientRepository
from services.base_service_impl import BaseServiceImpl

class ClientService(BaseServiceImpl[ClientModel]):
    def __init__(self, db: Session):
        self.repository = ClientRepository(db)
        super().__init__(self.repository)
