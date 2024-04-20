from django.shortcuts import render, redirect

from todolist.models import Todolist

from .forms import TodoForm

from django.views.decorators.http import require_POST

from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate

from django.contrib.auth.forms import UserCreationForm



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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

def profile(request):
    return render(request, 'profile.html')



