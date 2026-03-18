from django.urls import path
from . import views


urlpatterns =[
    path('signup/', views.insta_signup_view, name='insta_signup'),
    path('login/', views.insta_login_view, name='insta_login'),
    path('home/', views.insta_home, name='insta_home'),
    path('logout/', views.insta_logout_view, name='insta_logout'),
    path('create_post/', views.insta_post_view, name='create_post'),
    path('posts/', views.insta_post_list, name='post_list'),
]