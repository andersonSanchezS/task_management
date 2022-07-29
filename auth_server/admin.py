from django.contrib import admin
from django.contrib.auth.models import Permission
from . import models
from task_server import models as task_server_models


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'company', 'is_staff', 'is_superuser')


admin.site.register(models.User, UserAdmin)
admin.site.register(Permission)
admin.site.register(task_server_models.Company)
