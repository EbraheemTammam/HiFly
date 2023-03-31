from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view, 
    authentication_classes,
    permission_classes,    
)
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .models import CustomUser
from .serializers import TokenSerializer, UserSerializer
from .permissions import Admin


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def login_api_view(request):
    user = authenticate(
        request, 
        email=request.data.get('email'),
        password=request.data.get('password')
    )
    if user:
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        serializer = TokenSerializer(token).data
        return Response(serializer, status=status.HTTP_200_OK)
    return Response(
        {'error': 'no user with this credintials'},
        status=status.HTTP_404_NOT_FOUND
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_api_view(request):
    token = Token.objects.get(user=request.user)
    token.delete()
    return Response(
        {'details': 'logged out successfully'},
        status=status.HTTP_200_OK
    )

class UserListApiView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, Admin]

user_list_api_view = UserListApiView.as_view()

class UserDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, Admin]

user_detail_api_view = UserDetailApiView.as_view()