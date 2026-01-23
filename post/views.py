from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.



def signup(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        email = request.POST.get("email")
        
        post = Post(title=title, description=description, email=email)
        post.save()
        return HttpResponse("Signup successful!")
    return render(request, "signup.html")

def home(request):
    return render(request, "index.html")
