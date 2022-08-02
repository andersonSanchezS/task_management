# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Roles and permissions
from rolepermissions.decorators import has_permission_decorator
# Models
from task_server.models import ProjectTeam, Project
# Serializers
from task_server.api.serializers.project_team.index import ProjectTeamSerializer, ProjectTeamReadOnlySerializer
# Utils
from auth_server.utils.decodeJWT import decodeJWT
from datetime import datetime as dt


@api_view(['GET'])
@has_permission_decorator('view_project_team')
def getProjectTeams(request, pk):
    try:
        token = decodeJWT(request)
        project_team = ProjectTeam.objects.filter(project_id=pk)
        project = Project.objects.get(id=pk)
        if project.company_id == token['company_id']:
            serializer = ProjectTeamReadOnlySerializer(project_team, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to view this data'}, status=status.HTTP_401_UNAUTHORIZED)
    except ProjectTeam.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@has_permission_decorator('add_project_team')
def createProjectTeam(request):
    try:
        token = decodeJWT(request)
        project = Project.objects.get(id=request.data['project'])
        company = token['company_id'] == project.company_id
        if (token['is_admin'] and company) or (company and token['roles'].count('manager') == 1):
            serializer = ProjectTeamSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except ProjectTeam.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_project_team')
def updateProjectTeamState(request, pk):
    try:
        token = decodeJWT(request)
        project_team = ProjectTeam.objects.get(id=pk)
        project = Project.objects.get(id=project_team.project_id)
        company = token['company_id'] == project.company_id
        if (token['is_admin'] and company) or (company and token['roles'].count('manager') == 1):
            project_team.state = request.data['state']
            project_team.updated_at = dt.now()
            project_team.save()
            return Response({'msg': 'project team status updated'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except ProjectTeam.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)