from django.urls import path
from .views import EventosUsuarioViewSet, LocaisEventosUsuarioViewSet

app_name = "eventos"

urlpatterns = [
    path('locais_meus_eventos', LocaisEventosUsuarioViewSet.as_view({'get': 'list'}), name='locais_eventos_usuario'),
    path('meus_eventos', EventosUsuarioViewSet.as_view({'get': 'list'}), name='meus_eventos'),
    path('meus_eventos/<int:pk>/', EventosUsuarioViewSet.as_view({'get': 'retrieve'}), name='meus_eventos_item'),
]
