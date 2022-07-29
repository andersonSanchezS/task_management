# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Roles and permissions
from rolepermissions.decorators import has_permission_decorator
# Models
from task_server.models import Team
# Serializers
from task_server.api.serializers.team.index import TeamSerializer
# Utils
from auth_server.utils.decodeJWT import decodeJWT


@api_view(['POST'])
@has_permission_decorator('add_team')
def createTeam(request):
    try:
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)