from datetime import date

from django.core.exceptions import ValidationError

from . import models
from .models import Task, IntegerRangeField
from django.forms import ModelForm, DateTimeInput, IntegerField, TextInput, DateInput, NumberInput

from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

# class TaskForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['number', 'worker', 'project', 'task_status', 'date_control']
#
#         widgets = {
#             'number': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Номер задания'
#             }),
#             'worker': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Работник'
#             }),
#             'project': TextInput(attrs={
#                'class': 'form-control',
#                 'placeholder': 'Проект'
#             }),
#             # 'department': TextInput(attrs={
#             #     'class': 'form-control',
#             #     'placeholder': 'Department'
#             # }),
#             'task_status': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Статус задания (1 - задание выполнено, 0 - задание не выполнено)'
#             }),
#             'date_control': DateTimeInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Дата и время сдачи'
#             }),
#         }
class TaskForm(forms.Form):
    number = forms.IntegerField(help_text="Введите номер задания", min_value=1)
    task_status = forms.IntegerField(help_text="Введите статус задания (1 - задание выполнено, 0 - задание не выполнено)", min_value=0, max_value=1)
    date_control = forms.DateField(help_text="Выберите дату сдачи задания", widget=DatePickerInput())
#
# """
#     def clean_date_control(self):
#         date_local = self.cleaned_data['date_control']
#         mark = self.cleaned_data['mark']
#         if date.today().day - date_local.day > 7 and mark == 7:
#             raise ValidationError("Вы уверены, что 7 баллов?")
#         return date_local
# """

from .models import Worker
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class WorkerForm(forms.Form):
    name = forms.CharField(help_text="Введите имя")
    surname = forms.CharField(help_text="Введите фамилию")
    birth_date = forms.DateField(help_text="Выберите дату рождения", widget=DatePickerInput())
    team = forms.IntegerField(help_text="Введите номер команды")
