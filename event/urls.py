from .views import UserEventsViewSetViewSet

app_name = "eventos"

routeList = (
    (r'eventos_por_usuario', UserEventsViewSetViewSet),
)
