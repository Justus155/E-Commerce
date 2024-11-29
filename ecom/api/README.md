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

