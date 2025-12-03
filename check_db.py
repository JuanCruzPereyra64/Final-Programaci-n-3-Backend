from sqlalchemy import inspect
from config.database import engine

def check_schema():
    inspector = inspect(engine)
    columns = inspector.get_columns('products')
    print("Columns in 'products' table:")
    for col in columns:
        print(f"- {col['name']} ({col['type']})")

if __name__ == "__main__":
    check_schema()
