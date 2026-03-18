from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import User_data, Task_model
from .forms import task_form

def home(request):
    return HttpResponse("Hello, welcome to the User Authentication App!")

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        if username == "" and password =="":
            HttpResponse('username is empty')
        
        else:
            try:
                user = User_data(username=username, email=email, password=password, phone=phone)
                user.save()
            except:
                HttpResponse('error in save')
    return render(request, 'userdata.html' )

def user_view(request):
    users = User_data.objects.all()
    return render(request, "userview.html", {'userdata':users})

def task_view(request):
    if request.method =="POST":
        form = task_form(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'task.html', {'form':task_form()})


def task_list(request):
    tas = [{'title':'django', 'desc':'django'},{'title':'django', 'desc':'django'}]
    task = Task_model.objects.all()
    return render(request, 'task_list.html',{'task':task, 'role':'trainer'} )

def task_data(request, id):
    task = Task_model.objects.get(id = id)
    return render(request, 'task_data.html', {'task':task})

def task_edit(request, id):
    task = Task_model.objects.get(id = id)
    if request.method=="POST":
        form = task_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
    return render(request, 'task.html', {"form":task_form(instance=task)})

def task_delete(request, id):
    task = Task_model.objects.get(id = id)
    if task:
        task.delete()
        return HttpResponse('task deleted')
  
   