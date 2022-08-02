# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Roles and permissions
from rolepermissions.decorators import has_permission_decorator
# Models
from task_server.models import TaskComment
# Serializers
from task_server.api.serializers.comments.index import TaskCommentSerializer, TaskCommentReadOnlySerializer
# Utils
from auth_server.utils.decodeJWT import decodeJWT
from datetime import datetime as dt


@api_view(['POST'])
@has_permission_decorator('add_comment')
def createTaskComment(request):
    try:
        token = decodeJWT(request)
        if (token['is_admin'] and token['company_id'] == request.data['company']) \
                or (token['company_id'] == request.data['company'] and token['roles'].count('manager') == 1):
            serializer = TaskCommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@has_permission_decorator('view_comment')
def getTaskComments(request, pk):
    try:
        task_comments = TaskComment.objects.filter(task_id=pk)
        serializer = TaskCommentReadOnlySerializer(task_comments, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_comment')
def updateTaskComment(request):
    try:
        token = decodeJWT(request)
        if (token['is_admin'] and token['company_id'] == request.data['company']) \
                or (token['company_id'] == request.data['company'] and token['roles'].count('manager') == 1):
            task_comment = TaskComment.objects.get(pk=request.data['task'])
            serializer = TaskCommentSerializer(task_comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_comment')
def updateTaskState(request):
    try:
        token = decodeJWT(request)
        if (token['is_admin'] and token['company_id'] == request.data['company']) \
                or (token['company_id'] == request.data['company'] and token['roles'].count('manager') == 1):
            task_comment = TaskComment.objects.get(pk=request.data['task'])
            task_comment.state = request.data['state']
            task_comment.save()
            return Response({'data': 'task state updated'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
