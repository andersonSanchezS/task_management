from rest_framework import serializers

# Models
from task_server.models import Incidence
# Serializers
from task_server.api.serializers.team_member.index import TeamMemberSerializer
from task_server.api.serializers.task.index import TaskSerializer


class IncidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidence
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']
        required_fields = ['description']


class IncidenceReadOnlySerializer(serializers.ModelSerializer):
    responsible = TeamMemberSerializer(read_only=True)
    informer = TeamMemberSerializer(read_only=True)
    task = TaskSerializer(read_only=True)

    class Meta:
        model = Incidence
        fields = "__all__"
