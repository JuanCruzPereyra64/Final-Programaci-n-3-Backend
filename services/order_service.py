from sqlalchemy.orm import Session
from models.order import OrderModel
from repositories.order_repository import OrderRepository
from services.base_service_impl import BaseServiceImpl

class OrderService(BaseServiceImpl[OrderModel]):
    def __init__(self, db: Session):
        self.repository = OrderRepository(db)
        super().__init__(self.repository)
