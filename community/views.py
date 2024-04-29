from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    """ A view to show all post """
    queryset = Post.objects.filter(status=1)
    template_name = "community/community.html"
    paginate_by = 6