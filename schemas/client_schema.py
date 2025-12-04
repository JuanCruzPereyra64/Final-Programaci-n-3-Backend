from typing import Optional
from schemas.base_schema import BaseSchema

class ClientSchema(BaseSchema):
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
