from typing import Optional
from schemas.base_schema import BaseSchema

class BillSchema(BaseSchema):
    client_id: int
    total_amount: float
    billing_date: Optional[str] = None
