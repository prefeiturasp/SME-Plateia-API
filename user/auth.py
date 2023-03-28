import base64
import hashlib
from django.contrib.auth.hashers import BasePasswordHasher
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.settings import api_settings
from rest_framework import permissions
from .models import User


class CustomUserBackend(BaseBackend):
    def authenticate(self, request, rf=None, password=None, **kwargs):
        try:
            user = User.objects.get(rf=rf)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None


class CustomJWTAuthentication(JWTAuthentication):

    def authenticate(self, request):
        header = self.get_header(request)

        if header is None:
            return None

        raw_token = self.get_raw_token(header)

        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token

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


class SHA512PasswordHasher(BasePasswordHasher):
    algorithm = "sha512"

    def criptografar_senha_sha512(senha):
        senha_byte = senha.encode('utf-16le')
        sha512 = hashlib.sha512()
        sha512.update(senha_byte)
        senha_criptografada = sha512.digest()
        senha_base64 = base64.b64encode(senha_criptografada).decode('utf-8')
        return senha_base64.strip('/')

    def encode(self, senha, salt):
        return self.criptografar_senha_sha512(senha)

    def verify(self, senha, criptografada):
        return criptografada == self.encode(senha, '')

    def safe_summary(self, criptografada):
        return {'description': self.algorithm}
