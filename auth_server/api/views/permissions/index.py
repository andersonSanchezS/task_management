# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Roles and permissions
from rolepermissions.permissions import grant_permission, revoke_permission
from rolepermissions.permissions import available_perm_status
from rolepermissions.decorators import has_permission_decorator
# Models
from auth_server.models import User
# Utils
from auth_server.utils.decodeJWT import decodeJWT


@api_view(['GET'])
@has_permission_decorator('view_permission')
def userPermissions(request, pk):
    try:
        token = decodeJWT(request)
        user = User.objects.get(pk=pk)
        if token['is_admin'] or token['user_id'] == user.id:
            permissions = available_perm_status(user)
            return Response({'data': permissions}, status=status.HTTP_200_OK)
        return Response({'msg': 'You are not authorized to view this user permissions'},
                        status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        if str(e) == 'User matching query does not exist.':
            return Response({'Error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@has_permission_decorator('add_permission')
def addPermission(request, pk):
    try:
        token = decodeJWT(request)
        user = User.objects.get(pk=pk)
        if token['is_admin'] or token['roles'].count('manager') == 1:
            grant_permission(user, request.data['permission'])
            return Response({'msg': 'Permission granted'}, status=status.HTTP_200_OK)
        return Response({'msg': 'You are not authorized to add this permission'})
    except Exception as e:
        if str(e) == 'User matching query does not exist.':
            return Response({'Error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@has_permission_decorator('delete_permission')
def removePermission(request, pk):
    try:
        token = decodeJWT(request)
        user = User.objects.get(pk=pk)
        if token['is_admin'] or token['roles'].count('manager') == 1:
            revoke_permission(user, request.data['permission'])
            return Response({'msg': 'Permission granted'}, status=status.HTTP_200_OK)
        return Response({'msg': 'You are not authorized to delete this permission'})
    except Exception as e:
        if str(e) == 'User matching query does not exist.':
            return Response({'Error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
