from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from random import randint
# Create your views here.
def create_email(request):
    if request.method =="POST":
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        content = request.POST.get('content')
        otp = randint(1000,9999)
        print(otp)
        if email:
            send_mail(
            subject,
            content,
            "reviewmaster36@gmail.com",
            [email],
            fail_silently=True,
        )
            HttpResponse('mail send success')
        else:
            HttpResponse('mail send failed')
    return render(request, 'email.html' )