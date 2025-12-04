from sqlalchemy import text
from config.database import engine
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def update_schema():
    try:
        with engine.connect() as connection:
            logger.info("Starting schema update...")
            
            # Add image_url column
            try:
                connection.execute(text("ALTER TABLE products ADD COLUMN image_url VARCHAR"))
                logger.info("Added image_url column.")
            except Exception as e:
                logger.warning(f"Could not add image_url (might exist): {e}")

            # Add sizes column
            try:
                connection.execute(text("ALTER TABLE products ADD COLUMN sizes VARCHAR"))
                logger.info("Added sizes column.")
            except Exception as e:
                logger.warning(f"Could not add sizes (might exist): {e}")

            # Add is_active column
            try:
                connection.execute(text("ALTER TABLE products ADD COLUMN is_active BOOLEAN DEFAULT TRUE"))
                logger.info("Added is_active column.")
            except Exception as e:
                logger.warning(f"Could not add is_active (might exist): {e}")

            connection.commit()
            logger.info("Schema update completed successfully!")

    except Exception as e:
        logger.error(f"Error updating schema: {e}")

if __name__ == "__main__":
    update_schema()
