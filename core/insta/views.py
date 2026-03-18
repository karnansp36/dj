from django.shortcuts import render, redirect
from .models import Insta_sign, Post
from django.contrib import messages
from .forms import Post_form
# Create your views here.
def insta_signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if email == '' or password == '' or confirm_password == '':
            messages.error(request, "All fields are required.")
            return redirect('insta_signup')
        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('insta_signup')
        elif Insta_sign.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('insta_signup')
        else:
            Insta_sign.objects.create(email=email, password=password)
            messages.success(request, "Signup successful.")
            return redirect('/')
    return render(request, 'insta_signup_form.html')

def insta_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == '' or password == '' :
            messages.error(request, "All fields are required.")
            return redirect('insta_login')
        else:
            try:
                user = Insta_sign.objects.get(email=email, password=password)
                if not user:
                    raise Insta_sign.DoesNotExist
                else:
                    request.session['insta_user_id'] = user.id
                    messages.success(request, "Login successful.")
                    return redirect('insta_home')


            except Insta_sign.DoesNotExist:
                messages.error(request, "Invalid email or password.")
                return redirect('insta_signup')
    return render(request, 'insta_login_form.html')


def insta_home(request):
    if 'insta_user_id' not in request.session:
        return redirect('insta_login')
    else:
        return render(request, 'insta_home.html')
    
def insta_logout_view(request):
    try:
        del request.session['insta_user_id']
    except KeyError:
        pass
    return redirect('insta_login')


def insta_post_view(request):
    if 'insta_user_id' not in request.session:
        return redirect('insta_login')
    
    if request.method == 'POST':
        form = Post_form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.session['insta_user_id']
            post.save()
            messages.success(request, "Post created successfully.")
            return redirect('insta_home')
        else:
            messages.error(request, "Error creating post. Please check the form.")
            return render(request, 'insta_post_form.html', {'form': form})
    

    return render(request, 'insta_post_form.html',{'form': Post_form()})


def insta_post_list(request):
    if 'insta_user_id' not in request.session:
        return redirect('insta_login')
    id=request.session['insta_user_id']
    user_post = Post.objects.filter(user_id = id).order_by('-created_at')
    return render(request, 'insta_post_list.html', {'posts': user_post})