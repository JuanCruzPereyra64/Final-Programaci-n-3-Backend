from sqlalchemy import Column, Integer, String
from models.base_model import base

class CategoryModel(base):
    __tablename__ = 'categories'
    id_key = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    @property
    def id(self):
        return self.id_key
