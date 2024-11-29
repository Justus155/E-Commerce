# This is a simple example of how to set up the environment and run the API server.
# open terminal
# switch terminal to powershell
--activate enviroment 
.\.venv\scripts\activate.ps1

--download django and djangorestframework
*pip install djangorestframework*
*pip install django*

--change directory to your project--
cd ecom

--run migrations--(check if there is any changes before starting)
python manage.py makemigrations

--startapp within the project--
python manage.py startapp api

--pull in build requests and  requirements--
pip install -r requirements.txt
pip install requests

--start coding--
go to settings.py on your project
add 
INSTALLED_APPS=['rest_framework'] 


# Testing the API endpoints manually or with the provided Python script.

### Manually Using cURL

- **Add a new product**:

    ```bash
    curl -X POST http://127.0.0.1:8000/api/products/ -H "Content-Type: application/json" -d '{"name": "Sample Product", "description": "This is a sample product.", "price": 19.99}'
    ```

- **Retrieve all products**:

    ```bash
    curl http://127.0.0.1:8000/ecom/api/
    ```

### Using the Provided Python Script

1. **Create a file named `client.py`**:

    ```python
    import requests
    import json

    BASE_URL = 'http://127.0.0.1:8000/api/products/'

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

    def get_products():
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            products = response.json()
            print('List of products:')
            for product in products:
                print(f"ID: {product['id']}, Name: {product['name']}, Description: {product['description']}, Price: {product['price']}")
        else:
            print('Failed to retrieve products:', response.status_code)

    if __name__ == '__main__':
        add_product('Product 1', 'Description for product 1', 10.99)
        add_product('Product 2', 'Description for product 2', 20.99)
        get_products()
    ```

2. **Run the script**:

    ```bash
    python client.py
    ```

This script will add new products and retrieve the list of all products from the API.

---

