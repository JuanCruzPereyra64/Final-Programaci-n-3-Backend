from sqlalchemy.orm import Session
from models.category import CategoryModel
from repositories.base_repository_impl import BaseRepositoryImpl

class CategoryRepository(BaseRepositoryImpl[CategoryModel]):
    def __init__(self, db: Session):
        super().__init__(db, CategoryModel)
