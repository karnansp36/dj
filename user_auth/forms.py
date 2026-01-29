from django import forms
from .models import Signup, User_post

class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        exclude = ['created_at', 'updated_at']
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}),
            
            }

class Postform(forms.ModelForm):
    class Meta:
        model = User_post
        exclude = ['created_at', 'updated_at', 'user']
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'content'}),
            
            }