# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Roles and permissions
from rolepermissions.permissions import grant_permission
from rolepermissions.permissions import available_perm_status
# Models
from auth_server.models import User


@api_view(['GET'])
def userPermissions(request, pk):
    try:
        user = User.objects.get(pk=pk)
        roles = available_perm_status(user)
        return Response({'roles': roles}, status=status.HTTP_200_OK)
    except user.DoesNotExist:
        return Response({'Error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
