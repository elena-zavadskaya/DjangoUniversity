# Generated by Django 4.2.5 on 2023-12-06 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0062_task_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
    ]
