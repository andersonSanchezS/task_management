from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('auth_server.api.routes.index')),
    path('api/task/', include('task_server.api.routes.index')),
]
