from django.urls import path
from .views import EventosUsuarioViewSetViewSet, LocaisEventosUsuarioViewSetViewSet

app_name = "eventos"

urlpatterns = [
    path('locais_meus_eventos', LocaisEventosUsuarioViewSetViewSet.as_view({'get': 'list'}), name='locais_eventos_usuario'),
    path('meus_eventos', EventosUsuarioViewSetViewSet.as_view({'get': 'list'}), name='meus_eventos'),
    path('meus_eventos/<int:pk>/', EventosUsuarioViewSetViewSet.as_view({'get': 'retrieve'}), name='meus_eventos_item'),
]
