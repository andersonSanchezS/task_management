from django.contrib import admin
from . import models


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'company', 'is_staff', 'is_superuser')


admin.site.register(models.User, UserAdmin)
