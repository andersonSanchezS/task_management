from django.db import models

# Models
from task_server.api.models.task.index import Task
from task_server.api.models.incidence.index import Incidence
from task_server.api.models.team_member.index import TeamMember


class TaskComment(models.Model):
    teamMember = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    state = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return str(self.description)


class IncidenceComment(models.Model):
    teamMember = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    incidence = models.ForeignKey(Incidence, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    state = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return str(self.description)