# Generated by Django 4.2.5 on 2023-12-05 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0032_task_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(db_column='project', default=2, help_text='Выберите проект', on_delete=django.db.models.deletion.CASCADE, to='test_django.project', verbose_name='Проект'),
            preserve_default=False,
        ),
    ]
