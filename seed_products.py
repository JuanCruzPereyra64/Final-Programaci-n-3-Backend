import logging
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.base_model import base
from models.category import CategoryModel
from models.product import ProductModel

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def seed_data():
    """Seed the database with initial categories and products."""
    db = SessionLocal()
    try:
        logger.info("Dropping existing tables...")
        base.metadata.drop_all(bind=engine)
        
        logger.info("Creating new tables...")
        base.metadata.create_all(bind=engine)

        # 1. Create Categories
        categories_data = [
            {"name": "Remera"},
            {"name": "Buzo"},
            {"name": "Zapatilla"},
            {"name": "Pantalon"},
            {"name": "Accesorios"}
        ]

        categories = {}
        for cat_data in categories_data:
            category = CategoryModel(name=cat_data["name"])
            db.add(category)
            categories[cat_data["name"]] = category
        
        db.commit()
        # Refresh to get IDs
        for cat in categories.values():
            db.refresh(cat)

        # 2. Create Products - SKIPPED (User requested empty product list)
        # products_data = [] 
        
        logger.info("Database seeded successfully with categories only!")

    except Exception as e:
        logger.error(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
