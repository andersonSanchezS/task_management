from django.db import models

# Models
from task_server.models import Project, TeamMember


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    responsible = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    informer = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name='informer')
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    start_date = models.DateField(default='2020-01-01')
    limit_date = models.DateField(default='2020-01-01')
    hours = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    state = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return str(self.project) + ' ' + str(self.title) + ' ' + str(self.responsible) + ' ' + str(self.informer)