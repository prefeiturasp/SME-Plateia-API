from django.contrib.auth import authenticate, logout
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from .serializers import BaseUserSerializer, UserSerializer, SwaggerLoginSerializer


class JWTAuthenticationViewSet(viewsets.GenericViewSet):
    serializer_class = BaseUserSerializer
    http_method_names = ['post']
    authentication_classes = ()
    permission_classes = [AllowAny,]

    @extend_schema(request=SwaggerLoginSerializer,)
    @extend_schema(description='Autenticação', methods=["POST"])
    def authenticate(self, request, *args, **kwargs):
        rf = request.data.get('rf')
        password = request.data.get('password')

        if not (rf and password):
            raise ValidationError(detail='login e senha obrigatórios')
        try:
            user = authenticate(request, username=rf, password=password)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if user:
            refresh = RefreshToken.for_user(user)
            serializer = UserSerializer(user)

            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            raise AuthenticationFailed(detail='Credenciais de autenticação incorretas.')

    @extend_schema(description='Logout', methods=["POST"])
    def logout(self, request, *args, **kwargs):
        try:
            logout(request)
            return Response(status=status.HTTP_200_OK)
        except (AttributeError, KeyError):
            return Response({'detail': 'Não existe sessão ativa para fazer logout.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': 'Houve um erro ao realizar logout: {}'.format(str(e))}, status=status.HTTP_400_BAD_REQUEST)
