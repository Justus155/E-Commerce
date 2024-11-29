from django.http import HttpResponse 
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics






def homepage(request):
    return render(request, 'home.html')
    # return render(request, 'templates/home.html')



