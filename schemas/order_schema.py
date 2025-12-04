from typing import Optional
from schemas.base_schema import BaseSchema

class OrderSchema(BaseSchema):
    client_id: int
    bill_id: Optional[int] = None
    status: str
    total: float
