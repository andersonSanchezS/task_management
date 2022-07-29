from django.urls import path
from task_server.api.views.team_member.index import getTeamMembers, createTeamMember

urlpatterns = [
    path('list/<int:pk>', getTeamMembers, name='list-team-members'),
    path('create/<int:pk>', createTeamMember, name='create-team-member'),
]