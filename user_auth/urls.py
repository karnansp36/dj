from django.urls import path
from .views import register, home, login, logout, explore, profile, post_view

urlpatterns =[
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('explore/', explore, name='explore'),
    path('profile/', profile, name='profile'),
    path('post/', post_view, name='post'),
]