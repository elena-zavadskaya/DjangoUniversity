# Generated by Django 4.2.5 on 2023-11-26 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0019_task_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
    ]
