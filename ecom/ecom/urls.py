from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from . import views

# Create your views here.

# def homepage(request):
#     return HttpResponse("Welcome to the E-Commerce website!")

# Define the URL patterns for the application
urlpatterns = [
    path('', views.homepage)
    
]
