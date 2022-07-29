from rest_framework import serializers

# Models
from task_server.models import TeamMember


class TeamMemberSerializer(serializers.Serializer):
    class Meta:
        model = TeamMember
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']
        required_fields = ['team', 'user', 'team_role']