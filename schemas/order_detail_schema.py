from typing import Optional
from schemas.base_schema import BaseSchema

class OrderDetailSchema(BaseSchema):
    order_id: int
    product_id: int
    quantity: int
    unit_price: float
