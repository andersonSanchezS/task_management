from rest_framework import serializers

# Models
from task_server.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        read_only_fields = ['state', 'created_at', 'updated_at']
        required_fields = ['description']
