from django.db import models

# Create your models here.
class Insta_sign(models.Model):
    email = models.EmailField(unique=True)
    role= models.CharField(default='user', max_length=10)
    password =models.CharField()
    
class Post(models.Model):
    user = models.ForeignKey(Insta_sign, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)