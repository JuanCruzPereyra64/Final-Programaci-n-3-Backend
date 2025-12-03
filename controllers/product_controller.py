"""Product controller with proper dependency injection."""
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.base_controller_impl import BaseControllerImpl
from schemas.product_schema import ProductSchema
from services.product_service import ProductService


class ProductController(BaseControllerImpl):
    """Controller for Product entity with CRUD operations."""

    def __init__(self):
        super().__init__(
            schema=ProductSchema,
            service_factory=lambda db: ProductService(db),
            tags=["Products"]
        )
        # Override get_all route to include category_id
        self.router.routes = [r for r in self.router.routes if r.path != "/"]
        
        @self.router.get("/", response_model=List[ProductSchema], status_code=200)
        async def get_all(
            skip: int = 0,
            limit: int = 100,
            category_id: int = None,
            db: Session = Depends(get_db)
        ):
            """Get all products with optional category filtering."""
            service = ProductService(db)
            return service.get_all(skip=skip, limit=limit, category_id=category_id)