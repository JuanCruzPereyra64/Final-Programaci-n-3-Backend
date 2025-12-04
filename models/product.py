from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base_model import base

class ProductModel(base):
    __tablename__ = 'products'
    id_key = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    image_url = Column(String)
    sizes = Column(String)
    is_active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey('categories.id_key'), index=True)
    
    category = relationship("CategoryModel")

    @property
    def id(self):
        return self.id_key
