from django.db import models
from task_server.models import Team


class Team_role(models.Model):
    description = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
    state = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return str(self.description)
