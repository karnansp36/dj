from django import forms
from .models import Signup

class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        exclude = ['created_at', 'updated_at']
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}),
            
            }