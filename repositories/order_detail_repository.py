from sqlalchemy.orm import Session
from models.order_detail import OrderDetailModel
from repositories.base_repository_impl import BaseRepositoryImpl

class OrderDetailRepository(BaseRepositoryImpl[OrderDetailModel]):
    def __init__(self, db: Session):
        super().__init__(db, OrderDetailModel)
