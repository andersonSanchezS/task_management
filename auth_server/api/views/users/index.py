from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
# Models
from auth_server.models import User
from task_server.models import Company
# Serializers
from auth_server.api.serializers.users.index import UserSerializer
from task_server.api.serializers.company.index import CompanySerializer
# Permissions
from rolepermissions.decorators import has_permission_decorator
# Utils
from auth_server.utils.decodeJWT import decodeJWT
from datetime import datetime as dt


@api_view(['POST'])
def registerUser(request):
    try:
        validate_company = Company.objects.filter(description=request.data['company'])
        user = User.objects.filter(email=request.data['email'])
        if len(validate_company) == 0 and len(user) == 0:
            if request.data['company'] is not None:
                request.data['description'] = request.data['company']
                company_serializer = CompanySerializer(data=request.data)
                if company_serializer.is_valid():
                    company_serializer.save()
                    request.data['company'] = company_serializer.data['id']
                    user_serializer = UserSerializer(data=request.data)
                    if user_serializer.is_valid():
                        user_serializer.save()
                        return Response(user_serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response({'error': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': company_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                request.data['company'] = None
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():
                    user_serializer.save()
                    return Response(user_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if len(user) > 0:
                return Response({'error': 'Ya hay un usuario registrado con este correo'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Ya existe una empresa con este nombre'},
                                status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@has_permission_decorator('delete_user')
def deleteUser(request):
    try:
        token = decodeJWT(request)
        user = User.objects.get(id=request.data['id'], is_active=True)
        company = token['company_id'] == user.company.id
        if (token['is_admin'] and company) or (token['user_id'] == user.id and company):
            user.is_active = False
            user.updated_at = dt.utcnow()
            user.save()
            return Response({'message': 'User deleted'}, status=status.HTTP_200_OK)
        return Response({'error': 'You are not authorized to delete this user'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        if str(e) == 'User matching query does not exist.':
            return Response({'error': 'User is actually deactivated or not exists'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@has_permission_decorator('update_user')
def activateUser(request):
    try:
        token = decodeJWT(request)
        user = User.objects.get(id=request.data['id'], is_active=False)
        company = token['company_id'] == user.company.id
        if (token['is_admin'] and company) or (token['user_id'] == user.id and company):
            user.is_active = True
            user.updated_at = dt.utcnow()
            user.save()
            return Response({'message': 'User Activated'}, status=status.HTTP_200_OK)
        return Response({'error': 'You are not authorized to activate this user'},
                        status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        if str(e) == 'User matching query does not exist.':
            return Response({'error': 'User is actually activated'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_user')
def updateUser(request):
    try:
        token = decodeJWT(request)
        user = User.objects.get(id=request.data['id'], is_active=True)
        company = token['company_id'] == user.company.id
        if (token['is_admin'] and company) or (token['user_id'] == user.id and company):
            if request.data['email']:
                user.email = request.data['email']
            if request.data['password'] != "":
                user.set_password(request.data['password'])
            user.updated_at = dt.utcnow()
            user.save()
            return Response({'message': 'User updated'}, status=status.HTTP_200_OK)
        return Response({'error': 'You are not authorized to update this user'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        if str(e) == 'User matching query does not exist.':
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
