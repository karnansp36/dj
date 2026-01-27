from django.db import models

# Create your models here.

class Signup(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField()
    profile = models.ImageField(upload_to='profile/' ,default="/media/profile.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    