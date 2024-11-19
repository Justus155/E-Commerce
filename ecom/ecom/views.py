from django.http import HttpResponse 
from django.shortcuts import render
from django.shortcuts import render
from models import post

def home(request):
    posts = post.objects.all()
    return render(request, 'admin/home.html', {'posts': posts})


