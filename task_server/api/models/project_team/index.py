from django.db import models

# Models
from task_server.models import Project, Team


class ProjectTeam(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    state = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return str(self.project) + ' ' + str(self.team)