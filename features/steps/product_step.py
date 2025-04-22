import pandas as pd
import requests
from datetime import datetime
from behave import given, when, then
from multiprocessing import get_logger

logger = get_logger()

BASE_URL = "https://fakestoreapi.com"

@given('test data is loaded from "{filename}"')
def step_load_test_data(context, filename):

    path = f"features/test_data/{filename}"
    context.df = pd.read_csv(path)
    logger.info(f"Loaded test data from {path}")

@when("each product is created, retrieved, validated, and added to cart")
def step_process_products(context):
    context.results = []
    for _, row in context.df.iterrows():
        # Create product
        product_payload = {
            "title": row["title"],
            "price": float(row["price"]),
            "description": row["description"],
            "category": row["category"]
        }
        create_resp = requests.post(f"{BASE_URL}/products", json=product_payload)
        product_id = create_resp.json().get("id")

        # Retrieve product
        get_resp = requests.get(f"{BASE_URL}/products/{product_id}")
        data = get_resp.json()

        # Validate fields
        assert get_resp.status_code == 200
        assert data["title"] == row["title"]
        assert float(data["price"]) == float(row["price"])

        # Add to cart
        cart_payload = {
            "userId": 1,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "products": [{"productId": product_id, "quantity": 1}]
        }
        cart_resp = requests.post(f"{BASE_URL}/carts", json=cart_payload)

        # Store result for validation
        context.results.append({
            "product_id": product_id,
            "cart_response": cart_resp.json(),
            "cart_status": cart_resp.status_code
        })

@then("all products should appear in their respective cart responses")
def step_validate_cart_responses(context):
    for result in context.results:
        assert result["cart_status"] == 200
        products = result["cart_response"].get("products", [])
        product_ids = [p["productId"] for p in products]
        assert result["product_id"] in product_ids, f'Product {result["product_id"]} not found in cart'
