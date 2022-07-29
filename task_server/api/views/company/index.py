# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Roles and permissions
from rolepermissions.decorators import has_permission_decorator
# Models
from auth_server.models import User
from task_server.models import Company
# Serializers
from task_server.api.serializers.company.index import CompanySerializer
# Utils
from auth_server.utils.decodeJWT import decodeJWT


@api_view(['GET'])
def getCompany(request, pk):
    try:
        token = decodeJWT(request)
        if token['company_id'] == pk:
            company = Company.objects.get(pk=pk)
            serializer = CompanySerializer(company)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authorized to access this resource'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def createCompany(request):
    try:
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)