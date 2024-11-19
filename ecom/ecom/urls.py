from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage)
]
