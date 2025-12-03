import sys
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models.product import ProductModel
from config.database import DATABASE_URI

# Setup DB connection
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

try:
    print("🔍 Inspecting Products Table...")
    
    # Check raw SQL first to see everything
    result = db.execute(text("SELECT id, name, is_active, stock FROM products"))
    products = result.fetchall()
    
    if not products:
        print("❌ No products found in the database!")
    else:
        print(f"✅ Found {len(products)} products:")
        for p in products:
            print(f"   - ID: {p.id} | Name: {p.name} | Active: {p.is_active} | Stock: {p.stock}")

except Exception as e:
    print(f"❌ Error: {e}")
finally:
    db.close()
