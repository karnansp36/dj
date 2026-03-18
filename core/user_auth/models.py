from django.db import models

# Create your models here.

class User_data(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    phone = models.IntegerField()
    
class Task_model(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)