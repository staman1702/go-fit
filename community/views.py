from django.shortcuts import render, get_object_or_404

from .models import Post, Subject

# Create your views here.

def all_posts(request):
    
    posts = Post.objects.filter(status=1)
    subjects = None    

    if request.GET:        
        if 'subject' in request.GET:
            subjects = request.GET['subject'].split(',')
            posts = posts.filter(subjects__name__in=subjects)
            subjects = Subject.objects.filter(name__in=subjects)


    context = {
        'posts': posts,
        'current_subjects': subjects,
    }

    return render(request, 'community/community.html', context)

def post_detail(request, slug):
    
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(request, "community/post_detail.html", {"post": post},)
