from django.contrib.auth import authenticate, logout

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from drf_spectacular.utils import extend_schema

from .serializers import BaseUserSerializer, UserSerializer, SwaggerLogin

class JWTAuthenticationViewSet(viewsets.GenericViewSet):
    serializer_class = BaseUserSerializer
    http_method_names = ['post']
    
    @extend_schema(request=SwaggerLogin)
    @extend_schema(description='Autenticação', methods=["POST"])
    def authenticate(self, request, *args, **kwargs):
        login = request.data['login']
        password = request.data['password']

        if not (login and password):
            return Response({'errors': {'login e senha obrigatórios'}}, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(request, login=login, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            serializer = UserSerializer(user)

            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({'errors': {'login ou senha incorretos'}}, status=status.HTTP_401_UNAUTHORIZED)

    def logout(self, request, *args, **kwargs):
        try:
            logout(request)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)