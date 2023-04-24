from config.schema import *
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from user import urls as user_urls
from event import urls as event_urls
from inscription import urls as inscription_urls

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = routers.DefaultRouter()

routeLists = []

for routeList in routeLists:
    for route in routeList:
        router.register(route[0], route[1])

urlpatterns = [
    path('admin/', admin.site.urls),
    # api
    path('api/v1/', include(router.urls)),
    path('api/v1/',  include(user_urls.urlpatterns)),
    path('api/v1/',  include(event_urls.urlpatterns)),
    path('api/v1/',  include(inscription_urls.urlpatterns)),
    # swagger
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
