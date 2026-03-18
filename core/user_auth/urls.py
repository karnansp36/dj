from django.urls import path
from .views import home, create_user,task_delete, user_view, task_view, task_list, task_data, task_edit
urlpatterns = [
    path('home/', home),
    path('create/', create_user),
    path('view/', user_view),
    path('task/', task_view),
    path('list/', task_list),
    path('data/<int:id>', task_data),
    path('edit/<int:id>', task_edit),
    path('delete/<int:id>',task_delete)
]

