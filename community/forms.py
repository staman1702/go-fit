from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.initial['user_profile'] = self.instance.user_profile        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'  

    class Meta:
        model = Post
        exclude = ('user_profile',)
        fields = ('title', 'content', 'excerpt',
                  'subjects',)
        widgets = {
            'subjects': forms.CheckboxSelectMultiple
        }
