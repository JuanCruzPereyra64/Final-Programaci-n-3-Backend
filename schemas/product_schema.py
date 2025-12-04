from typing import Optional
from schemas.base_schema import BaseSchema

class ProductSchema(BaseSchema):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    category_id: int
    image_url: Optional[str] = None
