from sqlalchemy.orm import Session
from models.order_detail import OrderDetailModel
from repositories.order_detail_repository import OrderDetailRepository
from services.base_service_impl import BaseServiceImpl

class OrderDetailService(BaseServiceImpl[OrderDetailModel]):
    def __init__(self, db: Session):
        self.repository = OrderDetailRepository(db)
        super().__init__(self.repository)
