from typing import Optional
from schemas.base_schema import BaseSchema

class ReviewSchema(BaseSchema):
    product_id: int
    client_id: int
    rating: int
    comment: Optional[str] = None
