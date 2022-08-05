#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk' # 최신 포스트 보여주기
    template_name = 'blog/index.html'

class PostDetail(DetailView):
    model = Post


