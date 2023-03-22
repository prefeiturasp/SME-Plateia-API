from django.contrib.auth.backends import BaseBackend
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, login=None, password=None, **kwargs):
        try:
            user = User.objects.get(login=login)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        
        return None
    
class CustomUserJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        try:
            user, token = super().authenticate(request)
        except AuthenticationFailed:
            return None

        print(user)
        # Verifica se o usuário é uma instância do modelo personalizado
        if not isinstance(user, User):
            raise AuthenticationFailed('Invalid user.')

        return (user, token)