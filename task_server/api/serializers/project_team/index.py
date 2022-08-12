from rest_framework import serializers

# Models
from task_server.models import ProjectTeam

# Serializers
from task_server.api.serializers.team.index import TeamSerializer, TeamReadOnlySerializer
from task_server.api.serializers.project.index import ProjectSerializer


class ProjectTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTeam
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']
        required_fields = ['project', 'team']


class ProjectTeamReadOnlySerializer(serializers.ModelSerializer):
    team = TeamReadOnlySerializer(read_only=True)

    class Meta:
        model = ProjectTeam
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']
        required_fields = ['project', 'team']