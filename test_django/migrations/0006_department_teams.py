# Generated by Django 4.2.5 on 2023-11-12 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0005_alter_task_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='teams',
            field=models.ManyToManyField(to='test_django.team'),
        ),
    ]
