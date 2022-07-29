from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Models
from auth_server.models import User
# Serializers
from auth_server.api.serializers.users.index import UserSerializer
# Permissions
from rolepermissions.decorators import has_permission_decorator
# Utils
from auth_server.utils.decodeJWT import decodeJWT


@api_view(['POST'])
def registerUser(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@has_permission_decorator('delete_user')
def deleteUser(request, pk):
    try:
        token = decodeJWT(request)
        user = User.objects.get(pk=pk, is_active=True)
        if token['is_admin'] or token['user_id'] == user.id:
            user.is_active = False
            user.save()
            return Response({'msg': 'User deleted'}, status=status.HTTP_200_OK)
        return Response({'msg': 'You are not authorized to delete this user'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        if str(e) == 'User matching query does not exist.':
            return Response({'Error': 'User is actually deactivated or not exists'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@has_permission_decorator('update_user')
def activateUser(request, pk):
    try:
        user = User.objects.get(pk=pk, is_active=False)
        user.is_active = True
        user.save()
        return Response({'message': 'User Activated'}, status=status.HTTP_200_OK)
    except Exception as e:
        if str(e) == 'User matching query does not exist.':
            return Response({'Error': 'User is actually activated'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_user')
def updateUser(request, pk):
    try:
        token = decodeJWT(request)
        user = User.objects.get(pk=pk, is_active=True)
        if token['is_admin'] or token['user_id'] == user.id:
            user = User.objects.get(pk=pk)
            if request.data['email']:
                user.email = request.data['email']
            if request.data['password'] != "":
                user.set_password(request.data['password'])
            user.save()
            return Response({'message': 'User updated'}, status=status.HTTP_200_OK)
        return Response({'message': 'You are not authorized to update this user'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        if str(e) == 'User matching query does not exist.':
            return Response({'Error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)