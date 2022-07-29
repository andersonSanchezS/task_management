from django.urls import path, include

urlpatterns = [
    path('', include('auth_server.api.routes.users.index')),
    path('roles/', include('auth_server.api.routes.roles.index')),
    path('permissions/', include('auth_server.api.routes.permissions.index')),
]