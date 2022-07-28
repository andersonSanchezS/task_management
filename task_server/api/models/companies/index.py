from django.db import models


class Company(models.Model):
    description = models.CharField(max_length=255)
    state = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return str(self.description)
