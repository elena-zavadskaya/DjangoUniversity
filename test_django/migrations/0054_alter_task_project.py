# Generated by Django 4.2.5 on 2023-12-06 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0053_task_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(blank=True, help_text='Выберите проект', null=True, on_delete=django.db.models.deletion.CASCADE, to='test_django.leader', verbose_name='Проект'),
        ),
    ]
