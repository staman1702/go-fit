from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.initial['user_profile'] = self.instance.user_profile       

    class Meta:
        model = Post
        exclude = ('user_profile',)
        fields = ('title', 'content', 'excerpt',
                  'subjects', 'image_url', 'image',)
        widgets = {
            'subjects': forms.CheckboxSelectMultiple
        }
