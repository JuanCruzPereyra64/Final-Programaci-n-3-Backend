from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import base

class OrderDetailModel(base):
    __tablename__ = 'order_details'
    id_key = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    price = Column(Float)
    order_id = Column(Integer, ForeignKey('orders.id_key'), index=True)
    product_id = Column(Integer, ForeignKey('products.id_key'), index=True)
    
    order = relationship("OrderModel")
    product = relationship("ProductModel")
