from .views import InscriptionsViewSet

app_name = "inscricao"

routeList = (
    (r'inscricao', InscriptionsViewSet),
)
