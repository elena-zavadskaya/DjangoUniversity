# Generated by Django 4.2.5 on 2023-11-26 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0020_remove_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(db_column='project', default='Service app', help_text='Выберите проект', on_delete=django.db.models.deletion.CASCADE, to='test_django.project', verbose_name='Проект'),
        ),
    ]
