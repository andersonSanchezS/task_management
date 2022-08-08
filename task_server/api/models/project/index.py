from django.db import models

# Models
from task_server.models import Company


class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    start_date = models.DateField(default='2020-01-01')
    end_date = models.DateField(default=None, null=True, blank=True)
    state = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return str(self.team) + ' ' + str(self.company) + ' ' + str(self.description)