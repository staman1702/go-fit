from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required
def add_post(request):
    """ Add a post to the community """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only authenticated account can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_profile = request.user.userprofile  # Assuming UserProfile is linked to the User model
            post.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('add_post'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm(user=request.user)
    
    template = 'community/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_post(request, slug):
    """ Edit a post in community """
    post = get_object_or_404(Post, slug=slug)

    if not request.user.is_superuser and request.user != post.user_profile.user:
        messages.error(request, 'Sorry, only post creator/site admin can do that.')
        return redirect(reverse('home'))
        
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('post_detail', args=[slug]))
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'community/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)

@login_required
def delete_post(request, slug):
    """ Delete a product from the store """
    post = get_object_or_404(Post, slug=slug)

    if not request.user.is_superuser and request.user != post.user_profile.user:
        messages.error(request, 'Sorry, only post creator/site admin can do that.')
        return redirect(reverse('home'))
    
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('community'))
