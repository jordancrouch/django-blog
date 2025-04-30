from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


class PostListView(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'post_list.html'
