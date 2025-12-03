from sqlalchemy import Column, Integer, String, Float, Date
from models.base_model import base

class BillModel(base):
    __tablename__ = 'bills'
    id_key = Column(Integer, primary_key=True, index=True)
    bill_number = Column(String, unique=True, index=True)
    discount = Column(Float)
    date = Column(Date)
    total = Column(Float)
    payment_type = Column(Integer)
