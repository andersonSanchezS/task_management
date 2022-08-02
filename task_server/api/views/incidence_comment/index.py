# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Roles and permissions
from rolepermissions.decorators import has_permission_decorator
# Models
from task_server.models import IncidenceComment
# Serializers
from task_server.api.serializers.comments.index import IncidenceCommentSerializer, IncidenceCommentReadOnlySerializer
# Utils
from auth_server.utils.decodeJWT import decodeJWT
from datetime import datetime as dt


@api_view(['POST'])
@has_permission_decorator('add_comment')
def createIncidenceComment(request):
    try:
        token = decodeJWT(request)
        if (token['is_admin'] and token['company_id'] == request.data['company']) \
                or (token['company_id'] == request.data['company'] and token['roles'].count('manager') == 1):
            serializer = IncidenceCommentSerializer(data=request.data)
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
def getIncidenceComments(request, pk):
    try:
        incidence_comments = IncidenceComment.objects.filter(incidence_id=pk)
        serializer = IncidenceCommentReadOnlySerializer(incidence_comments, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_comment')
def updateIncidenceComment(request):
    try:
        token = decodeJWT(request)
        if token['company_id'] == request.data['company']:
            incidence_comment = IncidenceComment.objects.get(pk=request.data['incidence'])
            serializer = IncidenceCommentSerializer(incidence_comment, data=request.data)
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
def updateIncidenceState(request):
    try:
        token = decodeJWT(request)
        if token['company_id'] == request.data['company']:
            incidence_comment = IncidenceComment.objects.get(pk=request.data['incidence'])
            incidence_comment.state = request.data['state']
            incidence_comment.save()
            return Response({'data': 'Incidence state updated'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)