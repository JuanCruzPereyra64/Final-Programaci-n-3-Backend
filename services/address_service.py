from sqlalchemy.orm import Session
from models.address import AddressModel
from repositories.address_repository import AddressRepository
from services.base_service_impl import BaseServiceImpl

class AddressService(BaseServiceImpl[AddressModel]):
    def __init__(self, db: Session):
        self.repository = AddressRepository(db)
        super().__init__(self.repository)
