from sqlalchemy.orm import Session
from models.client import ClientModel
from repositories.base_repository_impl import BaseRepositoryImpl

class ClientRepository(BaseRepositoryImpl[ClientModel]):
    def __init__(self, db: Session):
        super().__init__(db, ClientModel)
