from rest_framework import serializers

# Models
from task_server.models import IncidenceComment, TaskComment
# Serializers
from task_server.api.serializers.team_member.index import TeamMemberSerializer


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']
        required_fields = ['description']




class IncidenceCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidenceComment
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']
        required_fields = ['description']


class TaskCommentReadOnlySerializer(serializers.ModelSerializer):
    teamMember = TeamMemberSerializer(read_only=True)
    class Meta:
        model = TaskComment
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']
        required_fields = ['description']




class IncidenceCommentReadOnlySerializer(serializers.ModelSerializer):
    teamMember = TeamMemberSerializer(read_only=True)
    class Meta:
        model = IncidenceComment
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']
        required_fields = ['description']
