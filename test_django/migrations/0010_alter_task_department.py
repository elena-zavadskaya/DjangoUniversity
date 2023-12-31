# Generated by Django 4.2.5 on 2023-11-22 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0009_alter_leader_department_alter_task_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='department',
            field=models.ForeignKey(db_column='department', default='Отдел backend-разработки', help_text='Выберите отдел', on_delete=django.db.models.deletion.CASCADE, to='test_django.department', verbose_name='Отдел'),
        ),
    ]
