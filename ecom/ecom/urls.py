from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from . import views
from api import views
import  api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    # API endpoints
    path('products/', views.ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),

    
]
