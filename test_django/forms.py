from . import models
from .models import Task, IntegerRangeField
from django.forms import ModelForm, DateTimeInput, IntegerField, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['number', 'worker', 'leader', 'task_status', 'date_control']

        widgets = {
            'number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер задания'
            }),
            'worker': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Работник'
            }),
            'leader': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тимлид команды'
            }),
            'task_status': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Статус задания (1 - задание выполнено, 0 - задание не выполнено)'
            }),
            'date_control': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата и время сдачи'
            }),
        }
