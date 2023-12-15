"""
URL configuration for newProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from test_django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.show_info, name='info'),

    path('signup_login/', views.sign_up_log_in),
    path('register_worker/', views.register_worker, name='register_worker'),
    path('', views.index, name='home'),
    path('show_worker/<int:id_team>/<int:id_user>/addtask/', views.create, name='create'),
    path('show_worker/<int:id_team>/<int:id_user>/<int:number_task>/deletetask/',
         views.delete_task, name='delete_task'),
    path('tasks_home/', views.tasks_home, name='tasks_home'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('user_logout', views.logout_user, name='logout_user'),

    path('leaderfView/<str:name>/', views.show_team_ofProject, name='worker_ofProject'),
    path('leaderView/<str:name>/<int:id_team>/', views.show_workerFromTeam, name='worker_fromTeam'),
    path('leaderView/<int:id_team>/<int:id_user>/', views.show_worker, name='show_worker'),
    path('leaderWorkerView/<int:id_team>/<int:id_worker>/', views.worker_info, name='worker_info'),

    # ajax url
    path('ajax/validate_username', views.validate_username, name='validate_username'),
    path('ajax/validate_email', views.validate_email, name='validate_email'),
    path('ajax/check_task_number/<int:id_worker>/', views.check_numberTask,
         name='check_task_number'),

]
