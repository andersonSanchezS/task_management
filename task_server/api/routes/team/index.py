from django.urls import path
from task_server.api.views.team.index import createTeam, getTeams, getTeam, updateTeam, updateState

urlpatterns = [
    path('create', createTeam, name='create-team'),
    path('list', getTeams, name='get-teams'),
    path('<int:pk>', getTeam, name='get-team'),
    path('update/<int:pk>', updateTeam, name='update-team'),
    path('state/<int:pk>', updateState, name='update-state'),
]