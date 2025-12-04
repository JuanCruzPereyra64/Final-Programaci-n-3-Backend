from typing import List, Optional
from sqlalchemy.orm import Session
from models.product import ProductModel
from repositories.product_repository import ProductRepository
from services.base_service_impl import BaseServiceImpl

class ProductService(BaseServiceImpl[ProductModel]):
    def __init__(self, db: Session):
        self.repository = ProductRepository(db)
        super().__init__(self.repository)

    def get_all(self, skip: int = 0, limit: int = 100, category_id: Optional[int] = None) -> List[ProductModel]:
        return self.repository.get_all(skip, limit, category_id)
