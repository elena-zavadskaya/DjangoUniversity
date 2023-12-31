# Generated by Django 4.2.5 on 2023-10-06 16:44

from django.db import migrations, models
import django.db.models.deletion
import test_django.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(help_text='Введите название отдела', max_length=50, primary_key=True, serialize=False, verbose_name='Название отдела')),
                ('description', models.TextField(verbose_name='Описание отдела')),
            ],
            options={
                'db_table': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя', max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Введите фамилию', max_length=100, verbose_name='Фамилия')),
                ('department', models.ForeignKey(help_text='Выберите отдел', on_delete=django.db.models.deletion.CASCADE, to='test_django.department', verbose_name='Название отдела')),
            ],
            options={
                'db_table': 'Leader',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите номер команды', max_length=20, verbose_name='Номер команды')),
            ],
            options={
                'db_table': 'Team',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, help_text='Введите имя', max_length=50, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Введите имя', max_length=100, verbose_name='Фамилия')),
                ('date_birth', models.DateField(help_text='Введите дату рождения', verbose_name='Дата рождения')),
                ('team', models.ForeignKey(help_text='Введите id команды', on_delete=django.db.models.deletion.CASCADE, to='test_django.team', verbose_name='Номер команды')),
            ],
            options={
                'db_table': 'Worker',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_status', test_django.models.IntegerRangeField(help_text='Введите текущий статус задания от 0 до 1', verbose_name='Статус задания (1 - задание выполнено, 0 - задание не выполнено)')),
                ('date_control', models.DateField(help_text='Введите дату сдачи', verbose_name='Дата сдачи')),
                ('leader', models.ForeignKey(help_text='Выберите тимлида', on_delete=django.db.models.deletion.CASCADE, to='test_django.leader', verbose_name='Тимлид команды')),
                ('worker', models.ForeignKey(help_text='Выберите работника', on_delete=django.db.models.deletion.CASCADE, to='test_django.worker', verbose_name='Работник')),
            ],
            options={
                'db_table': 'Task',
            },
        ),
    ]
