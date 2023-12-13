# Generated by Django 4.2.5 on 2023-12-06 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0045_remove_task_date_control_remove_task_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='worker',
            field=models.ForeignKey(blank=True, help_text='Выберите работника', null=True, on_delete=django.db.models.deletion.CASCADE, to='test_django.worker', verbose_name='Работник'),
        ),
    ]
