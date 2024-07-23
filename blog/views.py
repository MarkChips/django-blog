from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    # We can remove the model = Post as it is made redundant by the queryset explicitly stating all posts are displayed.
    # model = Post
    queryset = Post.objects.all()
    template_name = "post_list.html"