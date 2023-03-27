from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import JWTAuthenticationViewSet
app_name = "auth"


urlpatterns = [
    path('login', JWTAuthenticationViewSet.as_view(
        {'post': 'authenticate'}), name="login"),
    path('logout', JWTAuthenticationViewSet.as_view(
        {'post': 'logout'}), name="logout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
