from sqlalchemy import create_engine, text
from config.database import DATABASE_URI

engine = create_engine(DATABASE_URI)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM categories"))
    print("Categories in DB:")
    for row in result:
        print(row)
