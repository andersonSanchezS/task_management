# Generated by Django 4.0.6 on 2022-08-08 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_server', '0022_alter_project_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_role',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='task_server.company'),
        ),
    ]
