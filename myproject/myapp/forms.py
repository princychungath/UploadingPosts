from django import forms
from myapp.models import PostModel

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'description', 'image']