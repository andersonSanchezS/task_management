from django.urls import path
from task_server.api.views.project_team.index import createProjectTeam, getProjectTeams, updateProjectTeamState

urlpatterns = [
    path('create', createProjectTeam, name='create-project-team'),
    path('list/<int:pk>', getProjectTeams, name='get-project-teams'),
    path('update/<int:pk>', updateProjectTeamState, name='update-project-team-state'),
]