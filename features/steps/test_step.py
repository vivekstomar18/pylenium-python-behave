from multiprocessing import get_logger
import requests
from behave import given, when, then


logger = get_logger()
BASE_URL = "https://fakestoreapi.com"
product_id = None

@given('New product is created with "{title}", price "{price}", description "{description}", and category "{category}"')
def step_create_product(context, title, price, description, category):
    global product_id
    context.payload = {
        "title": title,
        "price": float(price),
        "description": description,
        "category": category,
    }
    response = requests.post(f"{BASE_URL}/products", json=context.payload)
    context.response = response
    product_id = response.json().get("id")
    logger.info(f"Created product with ID: {product_id}")

@when("the created product is retrieved")
def step_get_product(context):
    response = requests.get(f"{BASE_URL}/products/{product_id}")
    context.get_response = response
    logger.info(f"Retrieved product: {response.json()}")

@then('Correct product details are displayed containing title "{title}" and price "{price}"')
def step_validate_product(context, title, price):
    json_data = context.get_response.json()
    assert context.get_response.status_code == 200
    assert json_data["title"] == title, f'Expected title "{title}", got "{json_data["title"]}"'
    assert float(json_data["price"]) == float(price), f'Expected price {price}, got {json_data["price"]}'

@when("the product is added to the cart")
def step_add_to_cart(context):
    # user_data2 = test_data()["data2"]
    response = requests.post(f"{BASE_URL}/carts",json=context.payload)
    context.cart_response = response
    logger.info(f"Added to cart: {response.json()}")

@then("Verify that the product is added and displayed in the cart details page.")
def step_validate_cart(context):
    assert context.cart_response.status_code == 200
    products = context.cart_response.json().get("products", [])
    product_ids = [p["productId"] for p in products]
    assert product_id in product_ids, f"Product ID {product_id} not found in cart items"



