# Generated by Django 4.2.5 on 2023-11-26 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0014_alter_worker_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='team',
        ),
    ]