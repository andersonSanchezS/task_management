# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Roles and permissions
from rolepermissions.decorators import has_permission_decorator
# Models
from task_server.models import Team
# Serializers
from task_server.api.serializers.team.index import TeamSerializer, TeamReadOnlySerializer
# Utils
from auth_server.utils.decodeJWT import decodeJWT
from datetime import datetime as dt


@api_view(['GET'])
@has_permission_decorator('view_team')
def getTeams(request):
    try:
        token = decodeJWT(request)
        team = Team.objects.filter(company_id=token['company_id'])
        serializer = TeamReadOnlySerializer(team, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    except Team.DoesNotExist:
        return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@has_permission_decorator('view_team')
def getTeam(request, pk):
    try:
        token = decodeJWT(request)
        team = Team.objects.get(pk=pk, company_id=token['company_id'])
        if team.company_id == token['company_id']:
            serializer = TeamReadOnlySerializer(team)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Team.DoesNotExist:
        return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@has_permission_decorator('add_team')
def createTeam(request):
    try:
        token = decodeJWT(request)
        request.data['company'] = token['company_id']
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_team')
def updateTeam(request, pk):
    try:
        token = decodeJWT(request)
        team = Team.objects.get(pk=pk)
        company = token['company_id'] == team.company_id
        request.data['company'] = token['company_id']
        if (token['is_admin'] and company) or (token['roles'].count('manager') == 1 and company):
            serializer = TeamSerializer(team, data=request.data)
            team.updated_at = dt.utcnow()
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authorized to update this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Team.DoesNotExist:
        return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_team')
def updateState(request, pk):
    try:
        token = decodeJWT(request)
        team = Team.objects.get(pk=pk)
        company = token['company_id'] == team.company_id
        if (token['is_admin'] and company) or (token['roles'].count('manager') == 1 and company):
            team.state = request.data['state']
            team.updated_at = dt.utcnow()
            team.save()
            return Response({'message': 'Team state updated'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to update this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Team.DoesNotExist:
        return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
