from django.urls import path
from .views import InscriptionsViewSet

app_name = "inscription"

routeList = (
    (r'inscription', InscriptionsViewSet),
)