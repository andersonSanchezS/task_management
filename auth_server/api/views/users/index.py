from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Serializers
from auth_server.api.serializers.users.index import UserSerializer


@api_view(['POST'])
def registerUser(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
