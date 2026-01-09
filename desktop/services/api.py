import requests
from config import API_URL

token = None

def login(email, password):
    global token
    response = requests.post(
        f"{API_URL}/auth/login",
        data={
            "username": email,
            "password": password
        }
    )

    if response.status_code == 200:
        token = response.json()["access_token"]
        return True

    return False

def get_products():
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(f"{API_URL}/products", headers=headers)
    return response.json()

def create_product(product):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(
        f"{API_URL}/products",
        json=product,
        headers=headers
    )

    return response.status_code == 200
