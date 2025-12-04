from sqlalchemy.orm import Session
from models.bill import BillModel
from repositories.bill_repository import BillRepository
from services.base_service_impl import BaseServiceImpl

class BillService(BaseServiceImpl[BillModel]):
    def __init__(self, db: Session):
        self.repository = BillRepository(db)
        super().__init__(self.repository)
