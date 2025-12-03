import requests
import json

try:
    print("📡 Testing API: http://localhost:8000/products/")
    response = requests.get("http://localhost:8000/products/")
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Response JSON ({len(data)} items):")
        print(json.dumps(data, indent=2))
    else:
        print(f"❌ Error Response: {response.text}")

except Exception as e:
    print(f"❌ Connection Error: {e}")
    print("Make sure 'python main.py' is running!")
