from django.db import models

# Models
from task_server.models import Company
from auth_server.models import User


class Project(models.Model):
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, null=True, default=None, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    start_date = models.DateField(default='2020-01-01')
    end_date = models.DateField(default=None, null=True, blank=True)
    state = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return str(self.team) + ' ' + str(self.company) + ' ' + str(self.description)
