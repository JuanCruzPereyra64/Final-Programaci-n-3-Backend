import json
import logging
from sqlalchemy.orm import Session
from config.database import SessionLocal
from models.category import CategoryModel
from models.product import ProductModel
# Import other models to ensure registry is complete and avoid FK errors
from models.order_detail import OrderDetailModel
from models.order import OrderModel
from models.client import ClientModel
from models.address import AddressModel
from models.bill import BillModel
from models.review import ReviewModel

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def export_data():
    db = SessionLocal()
    try:
        data = {"categories": [], "products": []}

        # Export Categories
        categories = db.query(CategoryModel).all()
        for cat in categories:
            data["categories"].append({
                "id": cat.id_key,
                "name": cat.name
            })
        logger.info(f"Exported {len(data['categories'])} categories.")

        # Export Products
        products = db.query(ProductModel).all()
        for prod in products:
            data["products"].append({
                "id": prod.id_key,
                "name": prod.name,
                "description": prod.description,
                "price": prod.price,
                "stock": prod.stock,
                "image_url": prod.image_url,
                "sizes": prod.sizes,
                "is_active": prod.is_active,
                "category_id": prod.category_id
            })
        logger.info(f"Exported {len(data['products'])} products.")

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        logger.info("Data exported to data.json successfully.")

    except Exception as e:
        logger.error(f"Error exporting data: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    export_data()
