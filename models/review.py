from sqlalchemy import Column, Integer, String, Float, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from models.base_model import base

class ReviewModel(base):
    __tablename__ = 'reviews'
    id_key = Column(Integer, primary_key=True, index=True)
    rating = Column(Float, nullable=False)
    comment = Column(String)
    product_id = Column(Integer, ForeignKey('products.id_key'), index=True)
    
    __table_args__ = (
        CheckConstraint('rating >= 1.0 AND rating <= 5.0', name='check_rating_range'),
    )
    
    product = relationship("ProductModel")
