from django.urls import path
from auth_server.api.views.permissions.index import userPermissions

urlpatterns = [
    path('user/<int:pk>/', userPermissions, name='register-user'),
]