from sqlalchemy.orm import Session
from models.bill import BillModel
from repositories.base_repository_impl import BaseRepositoryImpl

class BillRepository(BaseRepositoryImpl[BillModel]):
    def __init__(self, db: Session):
        super().__init__(db, BillModel)
