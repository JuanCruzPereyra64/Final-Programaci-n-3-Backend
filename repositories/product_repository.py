from typing import List, Optional
from sqlalchemy.orm import Session
from models.product import ProductModel
from repositories.base_repository_impl import BaseRepositoryImpl

class ProductRepository(BaseRepositoryImpl[ProductModel]):
    def __init__(self, db: Session):
        super().__init__(db, ProductModel)

    def get_all(self, skip: int = 0, limit: int = 100, category_id: Optional[int] = None) -> List[ProductModel]:
        query = self.db.query(self.model)
        if category_id:
            query = query.filter(self.model.category_id == category_id)
        return query.offset(skip).limit(limit).all()
