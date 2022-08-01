# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Roles and permissions
from rolepermissions.decorators import has_permission_decorator
# Models
from task_server.models import Incidence
# Serializers
from task_server.api.serializers.incidence.index import IncidenceSerializer, IncidenceReadOnlySerializer
# Utils
from auth_server.utils.decodeJWT import decodeJWT
from datetime import datetime as dt


@api_view(['POST'])
@has_permission_decorator('add_incidence')
def createIncidence(request):
    try:
        token = decodeJWT(request)
        if (token['is_admin'] and token['company_id'] == request.data['company']) \
                or (token['company_id'] == request.data['company'] and token['roles'].count('manager') == 1):

            serializer = IncidenceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Incidence.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@has_permission_decorator('view_incidence')
def getIncidences(request, pk):
    try:
        token = decodeJWT(request)
        if (token['is_admin'] and token['company_id'] == request.data['company']) \
                or (token['company_id'] == request.data['company'] and token['roles'].count('manager') == 1):
            incidence = Incidence.objects.filter(task_id=pk)
            serializer = IncidenceReadOnlySerializer(incidence, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Incidence.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_incidence')
def updateIncidence(request, pk):
    try:
        token = decodeJWT(request)
        if (token['is_admin'] and token['company_id'] == request.data['company']) \
                or (token['company_id'] == request.data['company'] and token['roles'].count('manager') == 1):
            incidence = Incidence.objects.get(id=pk)
            serializer = IncidenceSerializer(incidence, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Incidence.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@has_permission_decorator('update_incidence')
def updateIncidenceStatus(request, pk):
    try:
        token = decodeJWT(request)
        if (token['is_admin'] and token['company_id'] == request.data['company']) \
                or (token['company_id'] == request.data['company'] and token['roles'].count('manager') == 1):
            incidence = Incidence.objects.get(id=pk)
            incidence.state = request.data['state']
            incidence.updated_at = dt.utcnow()
            incidence.save()
            return Response({'data': 'Incidence updated'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Incidence.DoesNotExist:
        return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)