from django import forms
from django.forms.models import inlineformset_factory
from django.forms.widgets import DateTimeInput
from .models import Challenge, GalleryImage

class ChallengeForm(forms.ModelForm):

    start_date = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}))
    end_date = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Challenge
        fields = ('title', 'content', 'start_date',
                  'end_date', 'main_image_url', 'main_image',
                  'status',)
        widgets = {
            'subjects': forms.CheckboxSelectMultiple,
        }

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(),
        }

GalleryImageFormSet = inlineformset_factory(
    Challenge,
    GalleryImage,
    form=GalleryImageForm,
    fields=('image',),
    extra=11,
    max_num=11,
    can_delete=True
)