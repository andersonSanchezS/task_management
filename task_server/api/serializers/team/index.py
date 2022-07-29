from rest_framework import serializers

# Models
from task_server.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']
        required_fields = ['description', 'company']