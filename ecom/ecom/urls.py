from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from.models import post
def homepage(request):
    posts = post.objects.all()
    return render(request, 'home.html', {request: ''})

def post_detail(request):
    return render(request, 'post.html', {request: ''})
