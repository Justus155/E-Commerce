from django.shortcuts import render,get_list_or_404
from.models import post

def home(request):
    posts = post.objects.all()
    return render(request, 'admin/home.html', {'posts': posts})

def post_detail(request):
    post = get_list_or_404(post, id=id)
    return render(request, 'admin/post_detail.html.html')