# Generated by Django 4.0.6 on 2022-08-01 15:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_server', '0008_remove_project_end_date_remove_project_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 1, 15, 41, 11, 368880)),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 1, 15, 41, 11, 368863)),
        ),
    ]
