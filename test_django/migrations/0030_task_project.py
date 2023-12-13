# Generated by Django 4.2.5 on 2023-12-05 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0029_remove_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(blank=True, help_text='Выберите проект', null=True, on_delete=django.db.models.deletion.CASCADE, to='test_django.project', verbose_name='Проект'),
        ),
    ]
