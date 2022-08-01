# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Roles and permissions
from rolepermissions.decorators import has_permission_decorator
# Models
from task_server.models import Task
# Serializers
from task_server.api.serializers.task.index import TaskSerializer, TaskReadOnlySerializer
# Utils
from auth_server.utils.decodeJWT import decodeJWT
from datetime import datetime as dt


@api_view(['POST'])
@has_permission_decorator('add_task')
def createTask(request):
    try:
        token = decodeJWT(request)
        if (token['is_admin'] and token['company_id'] == request.data['company']) \
                or (token['company_id'] == request.data['company'] and token['roles'].count('manager') == 1):

            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Task.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@has_permission_decorator('view_task')
def getTasks(request, pk):
    try:
        token = decodeJWT(request)
        if (token['is_admin'] and token['company_id'] == request.data['company']) \
                or (token['company_id'] == request.data['company'] and token['roles'].count('manager') == 1):
            task = Task.objects.filter(project_id=pk)
            serializer = TaskReadOnlySerializer(task, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Task.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_task')
def updateTask(request, pk):
    try:
        print(request.data)
        token = decodeJWT(request)
        if (token['is_admin'] and token['company_id'] == request.data['company']) \
                or (token['company_id'] == request.data['company'] and token['roles'].count('manager') == 1):
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(instance=task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Task.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_task')
def updateTaskState(request, pk):
    try:
        token = decodeJWT(request)
        if (token['is_admin'] and token['company_id'] == request.data['company']) \
                or (token['company_id'] == request.data['company'] and token['roles'].count('manager') == 1):
            task = Task.objects.get(id=pk)
            task.state = request.data['state']
            task.save()
            return Response({'data': 'Task state updated'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Task.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)