# Generated by Django 4.2.5 on 2023-11-26 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0015_remove_worker_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='team',
            field=models.ForeignKey(default='327', help_text='Выберете номер команды', on_delete=django.db.models.deletion.CASCADE, to='test_django.team', verbose_name='Номер команды'),
        ),
    ]
