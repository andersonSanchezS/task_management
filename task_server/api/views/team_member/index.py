# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Roles and permissions
from rolepermissions.decorators import has_permission_decorator
# Models
from task_server.models import TeamMember, Team
from auth_server.models import User
# Serializers
from task_server.api.serializers.team_member.index import TeamMemberSerializer, TeamMemberReadOnlySerializer
# Utils
from auth_server.utils.decodeJWT import decodeJWT
from datetime import datetime as dt


@api_view(['GET'])
@has_permission_decorator('view_team_member')
def getTeamMembers(request, pk):
    try:
        token = decodeJWT(request)
        team_member = TeamMember.objects.filter(team_id=pk)
        team = Team.objects.get(id=team_member[0].team_id)
        company = team.company.id == token['company_id']
        if company:
            serializer = TeamMemberReadOnlySerializer(team_member, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to view this'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except TeamMember.DoesNotExist:
        return Response({'Error': 'Team Member Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@has_permission_decorator('view_team_member')
def getTeamMember(request, pk):
    try:
        token = decodeJWT(request)
        team_member = TeamMember.objects.get(pk=pk)
        team = Team.objects.get(id=team_member.team_id)
        company = team.company.id == token['company_id']
        if company:
            serializer = TeamMemberReadOnlySerializer(team_member)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except TeamMember.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@has_permission_decorator('add_team_member')
def createTeamMember(request):
    try:
        token = decodeJWT(request)
        user = User.objects.get(id=request.data['user'])
        company = token['company_id'] == user.company_id and (token['is_admin'] or token['roles'].count('manager') == 1)
        if company:
            serializer = TeamMemberSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'Error': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_team_member')
def updateTeamMember(request, pk):
    try:
        token = decodeJWT(request)
        team_member = TeamMember.objects.get(id=pk)
        team = Team.objects.get(id=team_member.team_id)
        company = team.company.id == token['company_id'] and (token['is_admin'] or token['roles'].count('manager') == 1)
        if company:
            team_member = TeamMember.objects.get(pk=pk)
            serializer = TeamMemberSerializer(team_member, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except TeamMember.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_team_member')
def updateState(request, pk):
    try:
        token = decodeJWT(request)
        team_member = TeamMember.objects.get(pk=pk)
        team = Team.objects.get(id=team_member.team_id)
        company = team.company.id == token['company_id'] and (token['is_admin'] or token['roles'].count('manager') == 1)
        if company:
            team_member.state = request.data['state']
            team_member.save()
            serializer = TeamMemberSerializer(team_member)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except TeamMember.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
