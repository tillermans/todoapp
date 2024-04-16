from django.shortcuts import render, redirect

from todolist.models import Todolist

from .forms import TodoForm

from django.views.decorators.http import require_POST


# Create your views here.

def index(request):
    todo_items = Todolist.objects.order_by('id')
    form = TodoForm()
    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'todolist/index.html', context)


@require_POST
def addTodoItem(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_item = Todolist(text=request.POST['text'])
        new_item.save()

    return redirect("index")


def completeTodoItem(request, todo_id):
    item = Todolist.objects.get(pk=todo_id)
    item.completed = True
    item.save()

    return redirect("index")


def deleteCompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()

    return redirect("index")


def deleteAll(request):
    Todolist.objects.all().delete()

    return redirect('index')
