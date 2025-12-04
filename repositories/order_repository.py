from sqlalchemy.orm import Session
from models.order import OrderModel
from repositories.base_repository_impl import BaseRepositoryImpl

class OrderRepository(BaseRepositoryImpl[OrderModel]):
    def __init__(self, db: Session):
        super().__init__(db, OrderModel)
