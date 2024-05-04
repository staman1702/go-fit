from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'excerpt',
                  'subjects', 'image_url', 'image',)
        widgets = {
            'subjects': forms.CheckboxSelectMultiple
        }
