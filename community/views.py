from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Post, Subject
from .forms import PostForm

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

def add_post(request):
    """ Add a post to the community """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('add_post'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()
    
    template = 'community/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
