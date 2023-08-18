import requests
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import MultipleObjectsReturned
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.settings import api_settings
from rest_framework import permissions
from config.settings.base import env
from .models import User

AUTENTICA_CORESSO_API_TOKEN = env('AUTENTICA_CORESSO_API_TOKEN', default='')
AUTENTICA_CORESSO_API_URL = env('AUTENTICA_CORESSO_API_URL', default='')


class AuthBackend():
    @classmethod
    def authenticate(self, rf, password):
        DEFAULT_HEADERS = {
            'Content-Type': 'application/json',
            'Authorization': f'Token {AUTENTICA_CORESSO_API_TOKEN}'
        }
        DEFAULT_TIMEOUT = 10

        payload = {'login': rf, 'senha': password}

        try:
            response = requests.post(
                f"{AUTENTICA_CORESSO_API_URL}/autenticacao/",
                headers=DEFAULT_HEADERS,
                timeout=DEFAULT_TIMEOUT,
                json=payload
            )

            if response.status_code == 200 and 'login' in response.json():
                try:
                    user = User.objects.get(rf=rf)
                except MultipleObjectsReturned:
                    user = None
                    users = User.objects.filter(rf=rf)
                    for _user in users:
                        if _user.isadmin is False:
                            user = _user
                except User.DoesNotExist:
                    user = None

                if user:
                    return user
                else:
                    raise ValidationError(detail={'detail': f"Usuário {rf} CORESSO não foi encontrado na base do Plateia."})
            else:
                raise ValidationError(detail=response.json())
        except Exception as e:
            raise e


class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        response = AuthBackend().authenticate(username, password)
        return response


class CustomJWTAuthentication(JWTAuthentication):

    def get_user(self, validated_token):
        """
        Returns the user model instance associated with the token, if one exists.
        """

        try:
            user_id = validated_token.payload[api_settings.USER_ID_CLAIM]
        except KeyError:
            raise AuthenticationFailed('Invalid token')

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise AuthenticationFailed('User not found')

        return user


class isAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return False
        if request.user:
            return True
