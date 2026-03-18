from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import Post
# Create your views here.
def home_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES )
        if form.is_valid():
            form.save()
            return HttpResponse("Post created successfully")
    return render(request, "index.html", {'form': PostForm()})

def about_view(reqeust):
    post = Post.objects.all()
    return render(reqeust, 'pages/about.html', {'post': post})