# Generated by Django 4.2.5 on 2023-12-06 11:29

from django.db import migrations
import test_django.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0048_remove_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_status',
            field=test_django.models.IntegerRangeField(default=0, help_text='Введите текущий статус задания: 0 или 1', verbose_name='Статус задания (1 - задание выполнено, 0 - задание не выполнено)'),
        ),
    ]