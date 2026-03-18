from django import forms
from .models import Task_model

class task_form(forms.ModelForm):
    class Meta:
        model = Task_model
        exclude= ['created_at']
        fields ='__all__'