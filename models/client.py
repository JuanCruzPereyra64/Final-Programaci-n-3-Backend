from sqlalchemy import Column, Integer, String
from models.base_model import base

class ClientModel(base):
    __tablename__ = 'clients'
    id_key = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True, index=True)
    telephone = Column(String)
