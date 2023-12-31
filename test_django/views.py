import hashlib
from pathlib import Path

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import render, redirect

from test_django.forms import TaskForm, WorkerForm
from test_django.models import Worker, Task, Leader, Project, Team

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


def worker_info(request, id_team, id_worker):
    return render(request, 'workerInfoFromLeader.html',
                  {"worker": Worker.objects.get(id=id_worker),
                   "tasks": Task.objects.filter(worker_id=id_worker),
                   "id_team": id_team
                   })


def show_info(request):
    user = request.user

    if user.is_authenticated:
        if user.groups.filter(name="Тимлиды").exists():
            leader = Leader.objects.get(id_user_id=user.id)
            project = list(Project.objects.filter(leader_id=leader.id))
            return render(request, 'leaderView.html', {"project": project})
        else:
            worker = Worker.objects.get(id_user_id=user.id)
            tasks = Task.objects.filter(worker=worker.id)
            tasks = list(tasks)
            return render(request,
                          'workerInfo.html',
                          {"worker": worker,
                           "tasks": tasks
                           })
    else:
        return redirect("/")


def show_worker(request, id_team, id_user):
    user = request.user
    if user.is_authenticated and user.groups.filter(name="Тимлиды").exists():
        worker = Worker.objects.get(id_user_id=id_user)
        tasks = Task.objects.filter(worker=worker.id)
        tasks = list(tasks)
        return render(request,
                      'workerInfo.html',
                      {"worker": worker,
                       "link_img": hashlib.md5(
                           User.objects.get(id=worker.id_user_id).email.encode('utf-8')).hexdigest(),
                       "tasks": tasks,
                       "id_team": id_team,
                       })
    else:
        return render(request, 'notAccess.html')


def sign_up_log_in(request):
    if request.method == 'GET':
        cur_user = request.user
        if cur_user.is_authenticated:
            return redirect("/info")
        else:
            return render(request, 'signUpLogIn.html')

    else:
        if (request.POST.get("email") != None):
            email = request.POST.get("email")
            password = request.POST.get("password")
            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)

            try:
                login(request, user)
                return render(request, 'workerInfo.html', {'worker': Worker.objects.get(id_user_id=user.id),
                                                           'tasks': Task.objects.filter(
                                                               worker_id=Worker.objects.get(id_user_id=user.id).id),
                                                           'id_team': Worker.objects.get(id_user_id=user.id).team_id})
            except Exception:
                print("Not correct email or pass")
                return redirect("/signup_login/")
        else:
            email = request.POST.get("create_email")
            username = request.POST.get("create_user_name")
            password = request.POST.get("create_password")
            user = User.objects.create_user(email=email, username=username, password=password)
            login(request, user)
            Worker.objects.create(id_user_id=user.id)
            return redirect("/register_worker")


def register_worker(request):
    if request.method == 'GET':
        form = WorkerForm()
        return render(request, 'registerWorker.html', {'form': form})
    else:
        form = WorkerForm(request.POST)
        if form.is_valid():
            Worker.objects.filter(id_user_id=request.user).update(first_name=form.cleaned_data['name'],
                                                                  last_name=form.cleaned_data['surname'],
                                                                  date_birth=form.cleaned_data['birth_date'],
                                                                  team_id=form.cleaned_data['team'])
            return redirect('/info')
        else:
            print("asdfasdfasdf")


def create(request, id_team, id_user):
    if request.method == "GET":
        taskForm = TaskForm()
        return render(request, "create.html",
                      {"form": taskForm, "id_worker": Worker.objects.get(id_user=id_user).id})
    else:
        taskform = TaskForm(request.POST)
        if taskform.is_valid():
            obj = Task()
            obj.worker = Worker.objects.get(id_user_id=id_user)
            obj.number = taskform.cleaned_data['number']
            obj.task_status = taskform.cleaned_data['task_status']
            obj.date_control = taskform.cleaned_data['date_control']
            obj.save()
            if User.objects.get(id=id_user).groups.filter(name="Тимлиды").exists():
                return redirect(f"/leaderView/{name}/{id_team}/{id_user}")
            else:
                return render(request, 'workerInfoFromLeader.html', {'worker': Worker.objects.get(id_user_id=id_user),
                                                                     'tasks': Task.objects.filter(
                                                                         worker_id=Worker.objects.get(
                                                                             id_user_id=id_user).id),
                                                                     'id_team': Worker.objects.get(
                                                                         id_user_id=id_user).team_id})
        else:
            return redirect("/")


def delete_task(request, id_team, id_user, number_task):
    worker_id = Worker.objects.get(id_user_id=id_user).id
    task = Task.objects.filter(number=number_task, worker_id=worker_id).delete()
    if User.objects.get(id=id_user).groups.filter(name="Тимлиды").exists():
        return redirect(f"/leaderView/{name}/{id_team}/{id_user}")
    else:
        return render(request, 'workerInfoFromLeader.html', {'worker': Worker.objects.get(id_user_id=id_user),
                                                             'tasks': Task.objects.filter(
                                                                 worker_id=Worker.objects.get(id_user_id=id_user).id),
                                                             'id_team': id_team})


def tasks_home(request):
    tasks = Task.objects.order_by('-date_control')
    return render(request, 'tasks_home.html', {'tasks': tasks})


def show_team_ofProject(request, name):
    project = Project.objects.get(name=name)
    team = project.team.filter(project=project.name)
    return render(request, 'leaderViewTeam.html', {"team": team, "name": name})


def show_workerFromTeam(request, id_team, name):
    workers = Worker.objects.filter(team_id=id_team)
    workerAllTasks = []
    workerLastTasks = []
    for worker in workers:
        workerTasks = Task.objects.filter(worker_id=worker.id)
        if workerTasks:
            task_status = worker.task_set.values_list('task_status', flat=True)
            sumStatus = sum(task_status)
            workerAllTasks.append(sumStatus)
            workerLastTasks.append(max(map(lambda x: x.number, workerTasks)))

    workers = zip(workers, workerAllTasks, workerLastTasks)
    return render(request, 'leaderViewWorker.html',
                  {"workers": workers, "id_team": id_team})


# AJAX view
def validate_username(request):
    username = request.GET.get('create_user_name', None)
    response = {
        'taken': User.objects.filter(username__exact=username).exists()
    }
    return JsonResponse(response)


def validate_email(request):
    email = request.GET.get('create_email', None)
    response = {
        'taken': User.objects.filter(email__exact=email).exists()
    }
    return JsonResponse(response)


def check_numberTask(request, id_worker):
    number = int(request.GET.get('number', None))
    if (number == ""):
        number = 0
    response = {
        'exist': Task.objects.filter(number=number, worker_id=id_worker).exists()
    }
    return JsonResponse(response)


def change(request, id_worker, task_number, task_status, date_control):
    if request.method == "GET":
        taskForm = TaskForm()
        return render(request, "change.html",
                      {"form": taskForm,
                       "id_worker": id_worker,
                       "task_number": task_number,
                       "task_status": task_status,
                       "date_control": date_control})
    else:
        taskform = TaskForm(request.POST)
        if taskform.is_valid():
            task = Task.objects.get(number=task_number, worker_id=id_worker)
            task.number = taskform.cleaned_data['number']
            task.task_status = taskform.cleaned_data['task_status']
            task.date_control = taskform.cleaned_data['date_control']
            task.save()

            return render(request, 'workerInfoFromLeader.html',
                          {"worker": Worker.objects.get(id=id_worker),
                           "tasks": Task.objects.filter(worker_id=id_worker),
                           "id_team": Worker.objects.get(id=id_worker).team_id
                           })
        else:
            return redirect("/")
