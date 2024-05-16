from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Challenge, GalleryImage
from .forms import ChallengeForm, GalleryImageFormSet
from community.models import Subject

def all_challenges(request):
    
    challenges = Challenge.objects.filter(status=0)
    subjects = None    

    if request.GET:        
        if 'subject' in request.GET:
            subjects = request.GET['subject'].split(',')
            challenges = challenges.filter(subjects__name__in=subjects)
            subjects = Subject.objects.filter(name__in=subjects)

    template = 'challenges/challenges.html'
    context = {
        'challenges': challenges,
        'current_subjects': subjects,
    }
    
    return render(request, template, context)

@login_required
def create_challenge(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        challenge_form = ChallengeForm(request.POST, request.FILES)
        formset = GalleryImageFormSet(request.POST, request.FILES)
        if challenge_form.is_valid() and formset.is_valid():
            challenge = challenge_form.save()
            for form in formset:
                if form.cleaned_data:
                    image = form.cleaned_data['image']
                    GalleryImage.objects.create(challenge=challenge, image=image)
            return redirect('challenge_detail', slug=challenge.slug)
        else:
            messages.error(request, 'Failed to add challenge. Please ensure the form is valid.')
    else:
        challenge_form = ChallengeForm()
        formset = GalleryImageFormSet()

    template = 'challenges/create_challenge.html'
    context = {
        'challenge_form': challenge_form,
        'formset': formset
        }

    return render(request, template, context )


def challenge_detail(request, slug):
    challenge = get_object_or_404(Challenge, slug=slug)

    template = 'challenges/challenge_detail.html'
    context = {
        'challenge': challenge
        }
    
    return render(request, template, context )

@login_required
def edit_challenge(request, slug):
    challenge = get_object_or_404(Challenge, slug=slug)

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owner can edit challenges.')
        return redirect(reverse('challenge_detail', args=[slug]))
    
    if request.method == 'POST':
        challenge_form = ChallengeForm(request.POST, request.FILES, instance=challenge)
        formset = GalleryImageFormSet(request.POST, request.FILES, instance=challenge)
        if challenge_form.is_valid() and formset.is_valid():
            challenge = challenge_form.save()
            formset.save()
            messages.success(request, 'Challenge updated successfully.')
            return redirect(reverse('challenge_detail', args=[slug]))
        else:
            messages.error(request, 'Failed to update challenge. Please ensure the form is valid.')
    else:
        challenge_form = ChallengeForm(instance=challenge)
        formset = GalleryImageFormSet(instance=challenge)

    template = 'challenges/edit_challenge.html'
    context = {
        'challenge_form': challenge_form,
        'formset': formset,
        'challenge': challenge,
    }

    return render(request, template, context)

@login_required
def delete_challenge(request, slug):
    """ Delete a challenge from workouts """
    challenge = get_object_or_404(Challenge, slug=slug)

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only post creator/site admin can do that.')
        return redirect(reverse('home'))
    
    challenge.delete()
    messages.success(request, 'Challenge deleted!')
    return redirect(reverse('challenges'))