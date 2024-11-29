from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage)
    
]
