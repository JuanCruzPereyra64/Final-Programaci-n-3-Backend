from sqlalchemy.orm import Session
from models.review import ReviewModel
from repositories.base_repository_impl import BaseRepositoryImpl

class ReviewRepository(BaseRepositoryImpl[ReviewModel]):
    def __init__(self, db: Session):
        super().__init__(db, ReviewModel)
