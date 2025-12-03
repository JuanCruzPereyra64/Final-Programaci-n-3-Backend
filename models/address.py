from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import base

class AddressModel(base):
    __tablename__ = 'addresses'
    id_key = Column(Integer, primary_key=True, index=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    client_id = Column(Integer, ForeignKey('clients.id_key'), index=True)
    
    client = relationship("ClientModel")
