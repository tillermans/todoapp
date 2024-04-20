# todolist/urls.py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodoItem, name='add'),
    path('completed/<todo_id>', views.completeTodoItem, name='completed'),
    path('delected_completed', views.deleteCompleted, name='deleteCompleted'),
    path('deleteall', views.deleteAll, name='deleteAll'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
