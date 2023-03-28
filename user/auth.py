import hashlib
import base64
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

        hash = PBKDF2SHA512PasswordHasher()
        if hash.verify(password, user.password):
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


class PBKDF2SHA512PasswordHasher(BasePasswordHasher):
    algorithm = "sha512"

    def verify(self, password, encoded):
        encoded_2 = self.encode(password)
        return encoded == encoded_2

    def encode(self, senha):
        try:
            senhaByte = senha.encode('utf-8')
            sha512 = hashlib.sha512()
            sha512.update(senhaByte)
            pwd = base64.b64encode(sha512.digest()).decode()
            return pwd.lstrip('/')
        except Exception as e:
            raise ValueError(e)

    def safe_summary(self, encoded):
        return {'algorithm': self.algorithm}
