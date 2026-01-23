from django.urls import path
from .views import signup , home, detail, delete_post, update_post
urlpatterns =[
    path("signup/", signup, name="signup"),
    path("home/", home),
    path("detail/<int:id>", detail),
    path("delete/<int:id>", delete_post),
    path('update/<int:id>', update_post),
]