import requests
import json

# Base URL of the API
BASE_URL = 'http://127.0.0.1:8000/ecom/api/'


# Function to add a new product
def add_product(name, description, price):
    product_data = {
        'name': name,
        'description': description,
        'price': price
    }
    response = requests.post(BASE_URL, json=product_data)
    if response.status_code == 201:
        print('Product created successfully:', response.json())
    else:
        print('Failed to create product:', response.status_code, response.json())

# Function to retrieve and print all products
def get_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        products = response.json()
        print('List of products:')
        for product in products:
            print(f"ID: {product['id']}, Name: {product['name']}, Description: {product['description']}, Price: {product['price']}")
    else:
        print('Failed to retrieve products:', response.status_code)

# Example usage
if __name__ == '__main__':
    # Add new products
    add_product('Product 1', 'Description for product 1', 10.99)
    add_product('Product 2', 'Description for product 2', 20.99)

    # Retrieve and print all products
    get_products()