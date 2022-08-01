from django.urls import path
from task_server.api.views.team_member.index import getTeamMembers, createTeamMember, updateTeamMember,\
                                                    updateState, getTeamMember

urlpatterns = [
    path('list/<int:pk>', getTeamMembers, name='list-team-members'),
    path('create', createTeamMember, name='create-team-member'),
    path('update/<int:pk>', updateTeamMember, name='update-team-member'),
    path('state/<int:pk>', updateState, name='update-state'),
    path('<int:pk>', getTeamMember, name='get-team-member'),
]