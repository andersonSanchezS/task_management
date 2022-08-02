from django.db import models
from task_server.models import Team, Team_role
from auth_server.models import User


class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_role = models.ForeignKey(Team_role, on_delete=models.CASCADE)
    state = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return str(self.user) + ' ' + str(self.team) + ' ' + str(self.team_role)
