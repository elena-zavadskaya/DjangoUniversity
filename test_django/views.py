import hashlib
from pathlib import Path

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from test_django.forms import TaskForm
from test_django.models import Worker, Task

BASE_DIR = Path(__file__).resolve().parent.parent


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'index.html', data)


def show_info(request):
    user = request.user
    if user.is_authenticated:
        worker = Worker.objects.get(id_user_id=user.id)
        tasks = Task.objects.filter(worker=worker.id)
        tasks = list(tasks)
        return render(request, 'workerInfo.html',
                      {"worker": worker,
                       "link_img": hashlib.md5(user.email.encode('utf-8')).hexdigest(),
                       "tasks": tasks})
    else:
        return render(request, 'notAccess.html')


def sign_up_log_in(request):
    if request.method == 'GET':
        return render(request, 'signUpLogIn.html')

    else:
        if (request.POST.get("email") != None):
            email = request.POST.get("email")
            password = request.POST.get("password")
            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)

            try:
                login(request, user)
                return redirect("/info")
            except Exception:
                print("Not correct email or pass")
                return redirect("")
        else:
            email = request.POST.get("create_email")
            username = request.POST.get("create_user_name")
            password = request.POST.get("create_password")
            user = User.objects.create_user(email=email, username=username, password=password)
            login(request, user)
            return redirect("/info")


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_home')
        else:
            error = "Форма заполнена некорректно"

    form = TaskForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'create.html', data)


def tasks_home(request):
    tasks = Task.objects.order_by('-date_control')
    return render(request, 'tasks_home.html', {'tasks': tasks})
