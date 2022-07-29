from django.urls import path
from task_server.api.views.team_role.index import getTeamRoles, createTeamRole, updateTeamRole, deleteTeamRole, \
                                                  activateTeamRole

urlpatterns = [
    path('list', getTeamRoles, name='list-team-roles'),
    path('create', createTeamRole, name='create-team-role'),
    path('update/<int:pk>', updateTeamRole, name='update-team-role'),
    path('delete/<int:pk>', deleteTeamRole, name='delete-team-role'),
    path('activate/<int:pk>', activateTeamRole, name='activate-team-role'),
]