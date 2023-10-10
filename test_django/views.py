import hashlib
import os
from pathlib import Path

from django.shortcuts import render, redirect

from test_django.forms import TaskForm
from test_django.models import Worker, Task

BASE_DIR = Path(__file__).resolve().parent.parent


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
        # print(BASE_DIR / "static")
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
        pass


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
