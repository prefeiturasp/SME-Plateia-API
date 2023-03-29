from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import JWTAuthenticationViewSet

app_name = "autenticacao"

urlpatterns = [
    path('entrar', JWTAuthenticationViewSet.as_view(
        {'post': 'authenticate'}), name="entrar"),
    path('sair', JWTAuthenticationViewSet.as_view(
        {'post': 'logout'}), name="sair"),
    path('token/atualizar/', TokenRefreshView.as_view(), name='token_atualizar'),
]
