from django.db import models
from task_server.models import Company


class Team(models.Model):
    description = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    state = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return str(self.description)
