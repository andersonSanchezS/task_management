from rest_framework import serializers

# Models
from task_server.models import Task
# Serializers
from task_server.api.serializers.team_member.index import TeamMemberSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']
        required_fields = ['title', 'description', 'status', 'project', 'informer', 'responsible']



class TaskReadOnlySerializer(serializers.ModelSerializer):
    informer = TeamMemberSerializer(read_only=True)
    responsible = TeamMemberSerializer(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']
