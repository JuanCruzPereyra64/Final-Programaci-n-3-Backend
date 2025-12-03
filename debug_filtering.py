import requests
import json

BASE_URL = "http://localhost:8000/products/"

def test_filtering():
    # Test with category_id=6 (Camperas)
    print("Testing filtering with category_id=6...")
    try:
        response = requests.get(f"{BASE_URL}?category_id=6")
        if response.status_code == 200:
            products = response.json()
            print(f"✅ Status 200. Found {len(products)} products.")
            for p in products:
                print(f" - ID: {p['id']}, Name: {p['name']}, Category ID: {p['category_id']}")
                if p['category_id'] != 6:
                    print("❌ ERROR: Product returned with wrong category!")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")

if __name__ == "__main__":
    test_filtering()
