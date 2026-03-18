from django import forms
from .models import Insta_sign, Post

class Post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']
        widgets = {
            'caption': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'caption-text'}),
           
        }