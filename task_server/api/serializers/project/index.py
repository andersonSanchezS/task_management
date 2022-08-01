from rest_framework import serializers
# Model
from task_server.models import Project

# Serializers
from task_server.api.serializers.team.index import TeamSerializer


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']
        required_fields = ['name', 'description', 'team', 'company']

