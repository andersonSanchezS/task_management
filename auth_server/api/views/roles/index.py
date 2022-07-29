# Utils
import importlib
import inspect
# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Permissions
from rolepermissions.decorators import has_permission_decorator
from rolepermissions.roles import assign_role, remove_role
# Models
from auth_server.models import User


@api_view(['GET'])
@has_permission_decorator('view_role')
def roleList(request, *args, **kwargs):
    try:
        roles = []
        for name, cls in inspect.getmembers(importlib.import_module("task_management.roles"), inspect.isclass):
            if name != "AbstractUserRole":
                roles.append(name.lower())
        return Response({'roles': roles}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@has_permission_decorator('add_role')
def addRole(request, pk):
    try:
        role = request.data['role']
        user = User.objects.get(pk=pk)
        assign_role(user, role)
        return Response({'message': 'Role added'}, status=status.HTTP_200_OK)
    except Exception as e:
        if str(e) == 'User matching query does not exist.':
            return Response({'Error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@has_permission_decorator('delete_role')
def removeRole(request, pk):
    try:
        role = request.data['role']
        user = User.objects.get(pk=pk)
        remove_role(user, role)
        return Response({'message': 'Role deleted'}, status=status.HTTP_200_OK)
    except Exception as e:
        if str(e) == 'User matching query does not exist.':
            return Response({'Error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)