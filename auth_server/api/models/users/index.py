from django.db import models
from django.contrib.auth import models as auth_models
from task_server.api.models.companies.index import Company
# Role serializer
from rolepermissions.roles import assign_role


class UserManager(auth_models.BaseUserManager):

    def create_user(self, first_name, last_name, email,
                    password, company, role, is_staff=False, is_superuser=False):
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not password:
            raise ValueError('Users must have a password')
        if not company:
            raise ValueError('Users must have a company')
        if not role:
            raise ValueError('Users must have a role')

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.company = company
        user.save()
        try:
            assign_role(user, role)
        except Exception as e:
            user.delete()
            raise ValueError('invalid role')

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
        )
        user.save()
        return user


class User(auth_models.AbstractUser):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True, max_length=255)
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
