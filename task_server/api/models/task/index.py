from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Models
from task_server.models import Project, TeamMember
from auth_server.models import User


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
    responsible = models.ForeignKey(TeamMember, on_delete=models.CASCADE, null=True, blank=True, related_name='responsible')
    informer = models.ForeignKey(TeamMember, on_delete=models.CASCADE, null=True, blank=True, related_name='informer')
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    start_date = models.DateField(default='2020-01-01', null=True)
    limit_date = models.DateField(default='2020-01-01', null=True)
    hours = models.IntegerField(default=0, null=True)
    points = models.IntegerField(default=0, null=True)
    priority = models.IntegerField(default=0, null=True)
    state = models.IntegerField(default=1, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return str(self.project) + ' ' + str(self.title) + ' ' + str(self.responsible) + ' ' + str(self.informer)