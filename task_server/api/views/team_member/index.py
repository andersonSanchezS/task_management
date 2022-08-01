# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Roles and permissions
from rolepermissions.decorators import has_permission_decorator
# Models
from task_server.models import TeamMember
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
        team_member = TeamMember.objects.filter(team_id=pk, company_id=token['company_id'])
        serializer = TeamMemberReadOnlySerializer(team_member, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    except TeamMember.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@has_permission_decorator('view_team_member')
def getTeamMember(request, pk):
    try:
        token = decodeJWT(request)
        team_member = TeamMember.objects.get(pk=pk)
        if team_member.company_id == token['company_id']:
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
        if token['company_id'] == request.data['company'] and (token['is_admin']
                                                               or token['roles'].count('manager') == 1):
            serializer = TeamMemberSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
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
def updateTeamMember(request, pk):
    try:
        token = decodeJWT(request)
        if token['company_id'] == request.data['company'] and (token['is_admin']
                                                               or token['roles'].count('manager') == 1):
            team_member = TeamMember.objects.get(pk=pk, company_id=token['company_id'])
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
        if token['company_id'] == request.data['company'] and (token['is_admin']
                                                               or token['roles'].count('manager') == 1):
            team_member = TeamMember.objects.get(pk=pk, company_id=token['company_id'])
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