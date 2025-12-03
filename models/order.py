from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import base

class OrderModel(base):
    __tablename__ = 'orders'
    id_key = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    total = Column(Float)
    delivery_method = Column(Integer)
    status = Column(Integer)
    client_id = Column(Integer, ForeignKey('clients.id_key'), index=True)
    bill_id = Column(Integer, ForeignKey('bills.id_key'), index=True)
    
    client = relationship("ClientModel")
    bill = relationship("BillModel")
