# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Roles and permissions
from rolepermissions.decorators import has_permission_decorator
# Models
from task_server.models import Team_role
# Serializers
from task_server.api.serializers.team_role.index import TeamRoleSerializer
# Utils
from auth_server.utils.decodeJWT import decodeJWT
from datetime import datetime as dt


@api_view(['GET'])
@has_permission_decorator('view_team_role')
def getTeamRoles(request):
    try:
        token = decodeJWT(request)
        team_role = Team_role.objects.filter(company_id=token['company_id'])
        serializer = TeamRoleSerializer(team_role, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    except Team_role.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@has_permission_decorator('add_team_role')
def createTeamRole(request):
    try:
        token = decodeJWT(request)
        if token['is_admin'] or (token['company_id'] == request.data['company']
                                 and token['roles'].count('manager') == 1):
            serializer = TeamRoleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Team_role.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_team_role')
def updateTeamRole(request, pk):
    try:
        token = decodeJWT(request)
        if token['is_admin'] or (token['company_id'] == request.data['company']
                                 and token['roles'].count('manager') == 1):
            team_role = Team_role.objects.get(pk=pk)
            serializer = TeamRoleSerializer(team_role, data=request.data)
            if serializer.is_valid():
                team_role.updated_at = dt.utcnow()
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Team_role.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_team_role')
def updateTeamRoleStatus(request, pk):
    try:
        token = decodeJWT(request)
        if token['company_id'] == request.data['company'] and (token['is_admin']
                                                               or token['roles'].count('manager') == 1):
            team_role = Team_role.objects.get(pk=pk)
            team_role.updated_at = dt.utcnow()
            team_role.state = request.data['state']
            team_role.save()
            return Response({'data': 'team state updated'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Team_role.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)