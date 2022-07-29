from django.urls import path
from auth_server.api.views.permissions.index import userPermissions, addPermission, removePermission

urlpatterns = [
    path('user/<int:pk>/', userPermissions, name='register-user'),
    path('add/<int:pk>/', addPermission, name='add-permission'),
    path('remove/<int:pk>/', removePermission, name='remove-permission'),
]