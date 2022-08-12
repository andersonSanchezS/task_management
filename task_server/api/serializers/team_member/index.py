from rest_framework import serializers

# Models
from task_server.models import TeamMember
# Serializers
from task_server.api.serializers.team.index import TeamSerializer
from task_server.api.serializers.team_role.index import TeamRoleSerializer
from auth_server.api.serializers.users.index import UserReadOonlySerializer


class TeamMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamMember
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']
        required_fields = ['team', 'user', 'team_role']


class TeamMemberReadOnlySerializer(serializers.ModelSerializer):
    user = UserReadOonlySerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    team_role = TeamRoleSerializer(read_only=True)

    class Meta:
        model = TeamMember
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']

