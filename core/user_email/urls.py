from django.urls import path
from . import views

urlpatterns = [
    path('email/', views.create_email)
]