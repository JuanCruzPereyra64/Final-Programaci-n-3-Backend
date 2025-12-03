from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import base

class ProductModel(base):
    __tablename__ = 'products'
    id_key = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id_key'), index=True)
    
    category = relationship("CategoryModel")
