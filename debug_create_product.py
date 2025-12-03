import logging
from config.database import SessionLocal
from services.product_service import ProductService
from schemas.product_schema import ProductSchema

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def debug_create_product():
    db = SessionLocal()
    try:
        logger.info("Starting debug product creation...")
        
        # 1. Check if category exists
        from models.category import CategoryModel
        category = db.query(CategoryModel).filter(CategoryModel.id == 1).first()
        if not category:
            logger.error("❌ Category with ID 1 does not exist! Run seed_products.py first.")
            return

        logger.info(f"✅ Found category: {category.name} (ID: {category.id})")

        # 2. Create Product Schema
        product_data = ProductSchema(
            name="Debug Product",
            description="Test description",
            price=100.0,
            stock=10,
            category_id=1,
            image_url="http://example.com/image.jpg",
            sizes="S,M,L"
        )

        # 3. Attempt to save via Service
        service = ProductService(db)
        created_product = service.save(product_data)
        
        logger.info(f"✅ Product created successfully: {created_product.name} (ID: {created_product.id})")

    except Exception as e:
        logger.error(f"❌ Error creating product: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    debug_create_product()
