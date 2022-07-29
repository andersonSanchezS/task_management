from rest_framework import serializers

# Models
from task_server.models import Team_role


class TeamRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_role
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']
        required_fields = ['description', 'company']