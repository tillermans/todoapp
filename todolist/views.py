from django.shortcuts import render

from todolist.models import Todolist


# Create your views here.

def index(request):
    todo_items = Todolist.objects.order_by('id')
    context = {'todo_items': todo_items}
    return render(request, 'todolist/index.html', context)
