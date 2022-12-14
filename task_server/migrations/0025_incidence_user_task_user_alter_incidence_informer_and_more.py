# Generated by Django 4.0.6 on 2022-08-08 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task_server', '0024_project_user_alter_project_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidence',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='incidence',
            name='informer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='incidence_informer', to='task_server.teammember'),
        ),
        migrations.AlterField(
            model_name='incidence',
            name='responsible',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='incidence_responsible', to='task_server.teammember'),
        ),
    ]
