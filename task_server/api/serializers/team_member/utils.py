from rest_framework import serializers

# Models
from task_server.models import TeamMember
# Serializers
from auth_server.api.serializers.users.index import UserReadOonlySerializer


class TeamMemberForTeamSerializer(serializers.ModelSerializer):
    user = UserReadOonlySerializer(read_only=True)

    class Meta:
        model = TeamMember
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']
