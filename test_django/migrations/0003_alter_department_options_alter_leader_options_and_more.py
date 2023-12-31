# Generated by Django 4.2.5 on 2023-10-08 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import test_django.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test_django', '0002_leader_id_user_worker_id_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Отдел', 'verbose_name_plural': 'Отделы'},
        ),
        migrations.AlterModelOptions(
            name='leader',
            options={'verbose_name': 'Тимлид', 'verbose_name_plural': 'Тимлиды'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задание', 'verbose_name_plural': 'Задания'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Команда', 'verbose_name_plural': 'Команды'},
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='number',
        ),
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.TextField(help_text='Введите описание отдела', verbose_name='Описание отдела'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='id_user',
            field=models.ForeignKey(blank=True, help_text='Выберите id пользователя', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id пользователя'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_control',
            field=models.DateTimeField(help_text='Выберете дату и время сдачи', verbose_name='Дата и время сдачи'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=test_django.models.IntegerRangeField(default=0, help_text='Введите текущий статус задания: 0 или 1', verbose_name='Статус задания (1 - задание выполнено, 0 - задание не выполнено)'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='id_user',
            field=models.ForeignKey(blank=True, help_text='Выберите id пользователя', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id пользователя'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='last_name',
            field=models.CharField(help_text='Введите фамилию', max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='team',
            field=models.ForeignKey(help_text='Выберете номер команды', on_delete=django.db.models.deletion.CASCADE, to='test_django.team', verbose_name='Номер команды'),
        ),
    ]
