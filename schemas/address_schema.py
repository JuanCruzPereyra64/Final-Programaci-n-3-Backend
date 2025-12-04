from typing import Optional
from schemas.base_schema import BaseSchema

class AddressSchema(BaseSchema):
    street: str
    city: str
    state: str
    zip_code: str
    country: str
    client_id: int
