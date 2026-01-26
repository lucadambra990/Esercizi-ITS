import requests
BASE_URL="http://127.0.0.1:5000"
headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }

response = requests.get(f"{BASE_URL}/", headers=headers)
print(response.status_code,response.json())



payload = {
    "id": 1,
    "name": "Fire",
    "min_height_cm": 160,
    "inversions": 4
}

response = requests.post(
    "http://localhost:5000/parco/rollercoaster",
    json=payload
)

print(response.json())




payload = {
    "id": 2,
    "name": "Ice",
    "min_height_cm": 100,
    "animals": ["horse", "lion"]
}

response = requests.post(
    "http://localhost:5000/parco/carousel",
    json=payload
)

print(response.json())