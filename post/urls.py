from django.urls import path
from .views import signup , home
urlpatterns =[
    path("signup/", signup, name="signup"),
    path("home/", home)
]