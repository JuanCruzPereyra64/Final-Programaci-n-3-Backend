from sqlalchemy.orm import Session
from models.category import CategoryModel
from repositories.category_repository import CategoryRepository
from services.base_service_impl import BaseServiceImpl

class CategoryService(BaseServiceImpl[CategoryModel]):
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)
        super().__init__(self.repository)
