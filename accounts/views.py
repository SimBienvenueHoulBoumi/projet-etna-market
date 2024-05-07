from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import UserProfileSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = TokenObtainPairSerializer().get_token(user)
        return Response(
            {
                'message': 'User created successfully',
                'token': str(token.access_token)
            }, 
            status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_superuser(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save(is_superuser=True)
        token = TokenObtainPairSerializer().get_token(user)
        return Response({'message': 'Superuser created successfully', 'token': str(token.access_token)}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  


# isauthenticate