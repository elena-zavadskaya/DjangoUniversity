# Generated by Django 4.2.5 on 2023-12-06 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0065_task_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='department',
        ),
    ]
