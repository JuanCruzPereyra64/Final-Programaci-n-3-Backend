import json
import logging
import os
from sqlalchemy.orm import Session
from sqlalchemy import text
from config.database import SessionLocal, engine
from models.category import CategoryModel
from models.product import ProductModel

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def import_data():
    db = SessionLocal()
    try:
        if not os.path.exists("data.json"):
            logger.error("data.json not found. Please run export_data.py first.")
            return

        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        logger.info("Starting data import...")

        # Import Categories
        for cat_data in data.get("categories", []):
            # Check if exists
            existing = db.query(CategoryModel).filter(CategoryModel.id_key == cat_data["id"]).first()
            if not existing:
                category = CategoryModel(
                    id_key=cat_data["id"],
                    name=cat_data["name"]
                )
                db.add(category)
            else:
                existing.name = cat_data["name"]
        
        db.flush() # Flush to ensure categories exist for foreign keys
        logger.info("Categories processed.")

        # Import Products
        for prod_data in data.get("products", []):
            existing = db.query(ProductModel).filter(ProductModel.id_key == prod_data["id"]).first()
            if not existing:
                product = ProductModel(
                    id_key=prod_data["id"],
                    name=prod_data["name"],
                    description=prod_data["description"],
                    price=prod_data["price"],
                    stock=prod_data["stock"],
                    image_url=prod_data["image_url"],
                    sizes=prod_data["sizes"],
                    is_active=prod_data["is_active"],
                    category_id=prod_data["category_id"]
                )
                db.add(product)
            else:
                existing.name = prod_data["name"]
                existing.description = prod_data["description"]
                existing.price = prod_data["price"]
                existing.stock = prod_data["stock"]
                existing.image_url = prod_data["image_url"]
                existing.sizes = prod_data["sizes"]
                existing.is_active = prod_data["is_active"]
                existing.category_id = prod_data["category_id"]

        db.commit()
        
        # Reset sequences (Postgres specific, important for auto-increment)
        try:
            db.execute(text("SELECT setval('categories_id_key_seq', (SELECT MAX(id_key) FROM categories));"))
            db.execute(text("SELECT setval('products_id_key_seq', (SELECT MAX(id_key) FROM products));"))
            db.commit()
            logger.info("Sequences reset.")
        except Exception as e:
            logger.warning(f"Could not reset sequences (might be expected if not Postgres or different seq name): {e}")

        logger.info("Data imported successfully!")

    except Exception as e:
        logger.error(f"Error importing data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    import_data()
