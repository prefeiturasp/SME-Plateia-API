import hashlib
import base64
from config.settings.base import env
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.settings import api_settings
from rest_framework import permissions

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from django.contrib.auth.hashers import BasePasswordHasher
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import User

TRIPLEDES_KEY = env('DJANGO_TRIPLEDES_KEY', default='')
TRIPLEDES_IV = env('DJANGO_TRIPLEDES_IV', default='')

TRIPLEDES = "1"
SHA512 = "3"


class CustomUserBackend(BaseBackend):
    def authenticate(self, request, rf=None, password=None, **kwargs):
        try:
            user = User.objects.get(rf=rf)
        except User.DoesNotExist:
            return None

        if user.crypt == SHA512:
            hash = PBKDF2SHA512PasswordHasher()
        elif user.crypt == TRIPLEDES:
            hash = TripleDESPasswordHasher()
        else:
            raise PermissionError()

        if hash.verify(password, user.password):
            return user

        return None


class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
            hash = PBKDF2SHA512PasswordHasher()
            if hash.verify(password, user.password):
                return user
        except UserModel.DoesNotExist:
            return None


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


class PBKDF2SHA512PasswordHasher(BasePasswordHasher):
    algorithm = "sha512"

    def verify(self, password, encoded):
        encoded_2 = self.encode(password)
        return encoded == encoded_2

    def encode(self, senha, salt=None):
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


class TripleDESPasswordHasher(BasePasswordHasher):
    algorithm = "tripleDES"

    def verify(self, password, encoded):
        encoded_2 = self.encode(password)
        return encoded == encoded_2

    def encode(self, senha, salt=None):
        try:
            senhaByte = senha.encode('utf-8')
            backend = default_backend()
            cipher = Cipher(algorithms.TripleDES(bytes(TRIPLEDES_KEY)), modes.CBC(bytes(TRIPLEDES_IV)), backend=backend)
            padder = padding.PKCS7(cipher.algorithm.block_size).padder()
            padded_data = padder.update(senhaByte) + padder.finalize()
            encryptor = cipher.encryptor()
            encrypted_bytes = encryptor.update(padded_data) + encryptor.finalize()
            return base64.b64encode(encrypted_bytes).decode('ascii')
        except Exception as e:
            raise ValueError(e)

    def safe_summary(self, encoded):
        return {'algorithm': self.algorithm}
