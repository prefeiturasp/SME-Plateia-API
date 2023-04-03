from django.contrib.auth import authenticate, logout

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from .serializers import BaseUserSerializer, UserSerializer, SwaggerLoginSerializer


class JWTAuthenticationViewSet(viewsets.ModelViewSet):
    serializer_class = BaseUserSerializer
    http_method_names = ['post']
    authentication_classes = ()
    permission_classes = [AllowAny,]

    @extend_schema(request=SwaggerLoginSerializer,)
    @extend_schema(description='Autenticação', methods=["POST"])
    def authenticate(self, request, *args, **kwargs):
        rf = request.data['rf']
        password = request.data['password']
        if not (rf and password):
            return Response({'errors': {'login e senha obrigatórios'}}, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(request, rf=rf, password=password)
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

    @extend_schema(description='Logout', methods=["POST"])
    def logout(self, request, *args, **kwargs):
        try:
            logout(request)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
