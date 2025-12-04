from sqlalchemy.orm import Session
from models.address import AddressModel
from repositories.base_repository_impl import BaseRepositoryImpl

class AddressRepository(BaseRepositoryImpl[AddressModel]):
    def __init__(self, db: Session):
        super().__init__(db, AddressModel)
