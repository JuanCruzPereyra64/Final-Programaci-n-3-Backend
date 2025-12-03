from sqlalchemy import create_engine, text
from config.database import DATABASE_URI

engine = create_engine(DATABASE_URI)

with engine.connect() as conn:
    # Check if it exists first
    result = conn.execute(text("SELECT * FROM categories WHERE name = 'Camperas'"))
    if result.first():
        print("Category 'Camperas' already exists.")
    else:
        conn.execute(text("INSERT INTO categories (name) VALUES ('Camperas')"))
        conn.commit()
        print("✅ Category 'Camperas' added successfully!")
