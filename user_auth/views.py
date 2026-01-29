from django.shortcuts import render, redirect
from .forms import SignupForm, Postform
from django.http import HttpResponse
from  django.contrib import messages
from .models import Signup
# Create your views here.
def register(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            session_user = form.cleaned_data.get('username')
            request.session['user'] = session_user
            messages.success(request, f'Account created for {session_user}!')
            return redirect("home")
        else:
            messages.error(request, f'Account Not created!')
    return render(request, "register.html", {"form": SignupForm()})


def home(request):
    if 'user' in request.session:
        return render(request, "home.html")
    else:
        return redirect("register")
    
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = Signup.objects.filter(username=username, password=password).first()
        if not user:
            messages.error(request, "Invalid credentials!")
            return redirect("login")
        else:
            messages.success(request, "login successful!")
            request.session['user'] = username
            return redirect("home")
    return render(request, "login.html")

def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return redirect("login")

def explore(request):
     if 'user' in request.session:
        profiles = Signup.objects.all()
        return render(request, "explore.html" , {"profiles": profiles})
     else:
        return redirect("login")

def profile(request):
    if 'user' in request.session:
        username = request.session['user']
        user = Signup.objects.get(username=username)
        return render(request, "profile.html", {"user": user})
    else:
        return redirect("login")
    
def post_view(request):
    if 'user' in request.session:
        if request.method == "POST":
            form = Postform(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                username = request.session['user']
                user = Signup.objects.get(username=username)
                post.user = user
                post.save()
                messages.success(request, "Post created successfully!")
                return redirect("home")
            else:
                messages.error(request, "Failed to create post!")
        return render(request, "post/post.html", {"form": Postform()})
    else:
        return redirect("login")