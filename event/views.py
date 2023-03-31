from datetime import datetime
import logging
from django.db.models import Q
from django.db.models.functions import Lower
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError, NotFound, ParseError
from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import Event
from .serializers import EventSerializer, EventDetailSerializer
from user.auth import CustomJWTAuthentication, isAuthenticated
from .swagger import get_user_events_list_scheme, get_user_events_retrieve_scheme, get_locais_eventos_usuario_list_scheme

logger = logging.getLogger(__name__)


@extend_schema_view(
    list=extend_schema(**get_user_events_list_scheme()),
    retrieve=extend_schema(**get_user_events_retrieve_scheme())
)
class EventosUsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    authentication_classes = (CustomJWTAuthentication,)
    permission_classes = [isAuthenticated]
    pagination_class = PageNumberPagination
    http_method_names = ['get']

    def list(self, request):
        name = request.GET.get('nome')
        period_init = request.GET.get('periodo_inicio')
        period_end = request.GET.get('periodo_fim')
        local = request.GET.get('local')

        self.queryset = Event.objects.filter(inscription__userid=request.user).order_by('-schedule')

        try:
            try:
                if period_init and period_end:
                    # Foi necessário utilizar raw na queryset para tornar a busca com datas compatível com o banco SQL SERVER.
                    self.queryset = Event.get_events_by_user_and_dates(request.user.id, period_init, period_end, previous_queryset=self.queryset)
            except ValueError as e:
                raise ParseError(detail=e)

            if name:
                self.queryset = self.queryset.filter(showid__name__contains=name)
            if local:
                self.queryset = self.queryset.filter(local__contains=local)

            page = self.paginate_queryset(self.queryset)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        except Exception as e:
            erro = {
                'caminho': 'EventosUsuarioViewSet > list',
                'mensagem': str(e)
            }
            logger.error('Erro: %r', erro)
            raise Exception(e)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        try:
            inscriptions = instance.inscription_set.filter(userid=request.user)
            if not inscriptions.exists():
                raise NotFound()
        except Exception as e:
            raise ValidationError(detail=e)

        serializer = EventDetailSerializer(instance)
        return Response(serializer.data)


@extend_schema(**get_locais_eventos_usuario_list_scheme())
class LocaisEventosUsuarioViewSet(viewsets.GenericViewSet):
    queryset = Event.objects.all()
    authentication_classes = (CustomJWTAuthentication,)
    permission_classes = [isAuthenticated]

    def list(self, request):
        termo = request.GET.get('termo')

        if not termo:
            raise ValidationError({'detail': 'Campo `termo` é obrigatório.'})

        if len(termo) < 3:
            raise ValidationError({'detail': 'Termo deve conter pelo menos 3 caracteres.'})

        locations = Event.objects.filter(inscription__userid=request.user,
                                         local__icontains=termo).values_list('local', flat=True).distinct()

        return Response(locations)
