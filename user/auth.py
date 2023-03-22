from django.contrib.auth.backends import BaseBackend
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