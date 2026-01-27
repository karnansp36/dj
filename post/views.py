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
    post = Post.objects.all()
    post2 = [{"title":"john", "description": "this is django"} ,
            {"title":"peter", "description": "this is django"} ,
            {"title":"john", "description": "this is django"} ]
    return render(request, "index.html", {"posts":post , "role":"guest"})

def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, "post.html", {"post":post})

def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponse("Post deleted successfully!")

def update_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")
        email = request.POST.get("email")

        post.title = title
        post.description = description  
        post.email = email
        post.save()
        
        return HttpResponse("Post update successfully!")
    return render(request, "signup.html", {"post": post})
