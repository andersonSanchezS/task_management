from rest_framework import serializers

# Models
from task_server.models import Team, TeamMember

# Serializers Utils
from task_server.api.serializers.team_member.utils import TeamMemberForTeamSerializer


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']
        required_fields = ['description', 'company']


class TeamReadOnlySerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']
        required_fields = ['description', 'company']

    def get_members(self, obj):
        result = TeamMember.objects.filter(team=obj)
        return TeamMemberForTeamSerializer(result, many=True).data
