# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Roles and permissions
from rolepermissions.decorators import has_permission_decorator
# Models
from task_server.models import Project
# Serializers
from task_server.api.serializers.project.index import ProjectSerializer
# Utils
from auth_server.utils.decodeJWT import decodeJWT
from datetime import datetime as dt


@api_view(['GET'])
@has_permission_decorator('view_project')
def getProjects(request):
    try:
        token = decodeJWT(request)
        projects = Project.objects.filter(company_id=token['company_id'])
        serializer = ProjectSerializer(projects, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@has_permission_decorator('view_project')
def getProject(request, pk):
    try:
        token = decodeJWT(request)
        project = Project.objects.get(id=pk, company_id=token['company_id'])
        serializer = ProjectSerializer(project)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    except Project.DoesNotExist:
        return Response({'message': 'Project Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@has_permission_decorator('add_project')
def createProject(request):
    try:
        token = decodeJWT(request)
        if token['is_admin'] or token['roles'].count('manager') == 1:
            request.data['company'] = token['company_id']
            serializer = ProjectSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_project')
def updateProject(request, pk):
    try:
        token = decodeJWT(request)
        project = Project.objects.get(pk=pk, company_id=token['company_id'])
        if token['is_admin'] or token['roles'].count('manager') == 1:
            serializer = ProjectSerializer(instance=project, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Project.DoesNotExist:
        return Response({'error': 'project not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_project')
def updateState(request, pk):
    try:
        token = decodeJWT(request)
        project = Project.objects.get(pk=pk, company_id=token['company_id'])
        if token['is_admin'] or token['roles'].count('manager') == 1:
            project.state = request.data['state']
            project.save()
            return Response({'message': 'state updated'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Project.DoesNotExist:
        return Response({'error': 'project not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)