from django.urls import path, include

urlpatterns = [
    path('companies/', include('task_server.api.routes.company.index')),
    path('teams/', include('task_server.api.routes.team.index')),
]