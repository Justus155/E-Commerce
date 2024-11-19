# E-Commerce
E-commerce is a type of business model that involves the buying and selling of goods and services over developed systems.

# setting up  the Environment for the development of the application
open terminal environment
switch terminal to git bash or powershell
for powershell input:
 # python -m venv .venv-set the environment
 # .venv\Scripts\activate-activate the environment
 # pip install django-install django into the environment
 # django-admin startproject ecom-start project called ecom
 # cd ecom - changing directory to the project
 # python manage.py runserver - run server to check if project is ready to run
 
 for git bash input:
 # python -m venv .venv
 # source .venv/bin/activate
 # pip install django
 # django-admin startproject ecom
 # cd ecom
 # python manage.py runserver
 # Creating the models
 # python manage.py makemigrations
 # python manage.py migrate
 # Creating the admin user
 # python manage.py createsuperuser
 # Creating the admin user

# models.py


- **Customer Model**: 
  - Contains fields for `name` and `email`. The `email` field is unique to ensure no two customers can register with the same email.
  
- **Order Model**: 
  - Contains a foreign key `customer` that links each order to a specific customer. The `on_delete=models.CASCADE` option means that if a customer is deleted, all their associated orders will also be deleted.
  - The `order_date` field automatically records when the order was created.
```python
class Customer(models.Model):
    # Customer's name
    name = models.CharField(max_length=100)
    # Unique email for each customer
    email = models.EmailField(unique=True)

class Order(models.Model):
    # Foreign key to link each order to a customer
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    # Automatically set the date when the order is created
    order_date = models.DateTimeField(auto_now_add=True)
    # Total amount for the order
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
```

This setup allows you to manage customers and their orders effectively, ensuring that each customer can have multiple orders while maintaining a clear relationship between the two models. If you have any questions or need further assistance, feel free to ask!
