from typing import Optional
from schemas.base_schema import BaseSchema

class CategorySchema(BaseSchema):
    name: str
    description: Optional[str] = None
