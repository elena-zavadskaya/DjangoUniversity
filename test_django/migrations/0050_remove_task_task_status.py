# Generated by Django 4.2.5 on 2023-12-06 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0049_task_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_status',
        ),
    ]
