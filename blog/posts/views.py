from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request, post_id: int):
    specific_post = Post.objects.get(id = post_id)
    return render(request, 'post.html', {'specific_post': specific_post})