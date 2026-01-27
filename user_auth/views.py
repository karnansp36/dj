from django.shortcuts import render
from .forms import SignupForm
from django.http import HttpResponse
# Create your views here.
def register(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            session_user = form.cleaned_data.get('username')
            request.session['user'] = session_user
            return HttpResponse("Registration successful!")
        else:
            return render(request, "register.html", {"form": form})
    return render(request, "register.html", {"form": SignupForm()})