# Generated by Django 4.2.5 on 2023-11-26 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0017_remove_leader_team_remove_task_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
    ]
