from blog.models import Post
from django.views.generic import ListView, DetailView

class PostsListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
