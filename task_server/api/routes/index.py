from django.urls import path, include

urlpatterns = [
    path('companies/', include('task_server.api.routes.company.index')),
    path('teams/', include('task_server.api.routes.team.index')),
    path('team_roles/', include('task_server.api.routes.team_role.index')),
    path('team_members/', include('task_server.api.routes.team_member.index')),
]