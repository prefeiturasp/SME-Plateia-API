from django.urls import path
from .views import EventosUsuarioViewSet, LocaisEventosUsuarioViewSet, EventosViewSet

app_name = "eventos"

urlpatterns = [
    path('locais_meus_eventos', LocaisEventosUsuarioViewSet.as_view({'get': 'list'}), name='locais_eventos_usuario'),
    path('eventos', EventosViewSet.as_view({'get': 'list'}), name='eventos'),
    path('eventos/<int:pk>/', EventosViewSet.as_view({'get': 'retrieve'}), name='eventos_item'),
    path('meus_eventos', EventosUsuarioViewSet.as_view({'get': 'list'}), name='meus_eventos'),
    path('meus_eventos/<int:pk>/', EventosUsuarioViewSet.as_view({'get': 'retrieve'}), name='meus_eventos_item'),
]
