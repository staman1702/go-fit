from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post, Subject, Comment
from .forms import PostForm, CommentForm, AdminPostForm, AdminCommentForm


def all_posts(request):
    
    posts = Post.objects.all()
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
    
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user_profile = request.user.userprofile
            comment.post = post
            comment.save()

            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
        else:
            messages.error(request, 'Failed to comment. Please ensure the form is valid.')

    comment_form = CommentForm()

    return render(
        request, 
        "community/post_detail.html", 
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

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
            post.user_profile = request.user.userprofile  
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
        if request.user.is_superuser:
            form = AdminPostForm(request.POST, request.FILES, instance=post)
        else:
            form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('post_detail', args=[slug]))
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid.')
    else:
        if request.user.is_superuser:
            form = AdminPostForm(instance=post)
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

@login_required
def edit_comment(request, comment_id):
    """ Edit a comment """
    comment = get_object_or_404(Comment, id=comment_id)

    if not request.user.is_superuser and request.user != comment.user_profile.user:
        messages.error(request, 'Sorry, only comment creator/site admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        if request.user.is_superuser:
            form = AdminCommentForm(request.POST, request.FILES, instance=comment)
        else:
            form = CommentForm(request.POST, request.FILES, instance=comment)

        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully.')
            return redirect('community')
        else:
            messages.error(request, 'Failed to update comment. Please ensure the form is valid.')
    else:
        if request.user.is_superuser:
            form = AdminCommentForm(instance=comment)
        else:
            form = CommentForm(instance=comment)

    template = 'community/edit_comment.html'
    context = {
        'form': form,
        'comment': comment,
    }

    return render(request, template, context)

@login_required
def delete_comment(request, comment_id):
    """ Delete a comment """
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user.is_superuser and request.user != comment.user_profile.user:
        messages.error(request, 'You do not have permission to delete this comment.')
        return redirect(reverse('home'))
    
    comment.delete()
    messages.success(request, 'Comment deleted successfully.')
    return redirect('community')

