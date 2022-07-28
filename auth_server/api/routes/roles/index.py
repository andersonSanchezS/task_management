from django.urls import path, include
from auth_server.api.views.roles.index import roleList, removeRole, addRole

urlpatterns = [
    path('list/', roleList, name='register-user'),
    path('add/<int:pk>/', addRole, name='add-role'),
    path('remove/<int:pk>/', removeRole, name='remove-role'),
]