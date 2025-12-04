from sqlalchemy.orm import Session
from models.review import ReviewModel
from repositories.review_repository import ReviewRepository
from services.base_service_impl import BaseServiceImpl

class ReviewService(BaseServiceImpl[ReviewModel]):
    def __init__(self, db: Session):
        self.repository = ReviewRepository(db)
        super().__init__(self.repository)
