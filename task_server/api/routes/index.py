from django.urls import path, include

urlpatterns = [
    path('companies/', include('task_server.api.routes.company.index')),
    path('teams/', include('task_server.api.routes.team.index')),
    path('team_roles/', include('task_server.api.routes.team_role.index')),
    path('team_members/', include('task_server.api.routes.team_member.index')),
    path('projects/', include('task_server.api.routes.project.index')),
    path('project_teams/', include('task_server.api.routes.project_team.index')),
    path('tasks/', include('task_server.api.routes.task.index')),
    path('tasks/comments/', include('task_server.api.routes.task_comments.index')),
    path('incidences/', include('task_server.api.routes.incidence.index')),
]