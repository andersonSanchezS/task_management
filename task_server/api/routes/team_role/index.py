from django.urls import path
from task_server.api.views.team_role.index import getTeamRoles, createTeamRole, updateTeamRole, updateTeamRoleStatus

urlpatterns = [
    path('list', getTeamRoles, name='list-team-roles'),
    path('create', createTeamRole, name='create-team-role'),
    path('update/<int:pk>', updateTeamRole, name='update-team-role'),
    path('state/<int:pk>', updateTeamRoleStatus, name='update-team-role-status'),
]