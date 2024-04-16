# todolist/urls.py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodoItem, name='add'),
    path('completed/<todo_id>', views.completeTodoItem, name='completed'),
    path('delected_completed', views.deleteCompleted, name='deleteCompleted'),
    path('deleteall', views.deleteAll, name='deleteAll')
]
