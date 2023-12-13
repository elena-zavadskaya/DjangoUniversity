# Generated by Django 4.2.5 on 2023-12-05 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0024_task_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leader',
            name='department',
        ),
        migrations.AddField(
            model_name='department',
            name='leader',
            field=models.ForeignKey(default='Отдел backend-разработки', help_text='Выберите тимлида', on_delete=django.db.models.deletion.CASCADE, to='test_django.leader', verbose_name='Тимлид'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
