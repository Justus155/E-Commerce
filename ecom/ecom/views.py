from django.http import HttpResponse 
import django.shortcuts
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

