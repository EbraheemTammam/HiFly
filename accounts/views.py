import jwt

from django.conf import settings
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
    """
    login api takes input 'email' and 'password'
    """
    user = authenticate(
        request, 
        email=request.data.get('email'),
        password=request.data.get('password')
    )
    if user:
        token = Token.objects.filter(user=user)
        token = token.first() if token.exists() else Token.objects.create(user=user)
        serializer = TokenSerializer(token).data
        encoded = jwt.encode(
            {'auth': serializer},
            settings.SECRET_KEY,
            algorithm='HS256'
        )
        response = Response()
        """
        response.set_cookie(
            key='accessToken', 
            value=encoded, 
            samesite='None',
            #secure=True,
            httponly=True
        )
        """
        response.data = {'accessToken': encoded}
        response.status = status.HTTP_200_OK
        return response
    return Response(
        {'error': 'no user with this credintials'},
        status=status.HTTP_404_NOT_FOUND
    )


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def login_verify_api_view(request):
    #token = request.COOKIES.get('hifly-access-token')
    token = request.data.get('accessToken')
    if not token:
        return Response({'details': 'token was not provided'})
    #    return Response({'details': 'no cookies provided'})
    data = jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms='HS256'
    )
    token = data.get('auth')
    user = CustomUser.objects.filter(email=token['user']['email'])
    if not user.exists():
        return Response({'details': 'no user with this credintials'})
    user = user.first()
    token = Token.objects.filter(key=token['key'], user=user)
    if token.exists():            
        return Response(data['auth'])
    return Response({'details': 'invalid token'})


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
    permission_classes = []

user_list_api_view = UserListApiView.as_view()

class UserDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, Admin]

user_detail_api_view = UserDetailApiView.as_view()