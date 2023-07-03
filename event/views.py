import datetime
import logging
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError, NotFound, ParseError
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view

from user.auth import CustomJWTAuthentication, isAuthenticated

from .models import Event
from .serializers import EventSerializer, EventDetailSerializer
from .swagger import (get_user_events_list_scheme, get_user_events_retrieve_scheme, 
                      get_locais_eventos_usuario_list_scheme, get_events_list_scheme, get_events_retrieve_scheme)

logger = logging.getLogger(__name__)


@extend_schema_view(
    list=extend_schema(**get_events_list_scheme()),
    retrieve=extend_schema(**get_events_retrieve_scheme())
)
class EventosViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [AllowAny]
    pagination_class = None
    http_method_names = ['get']

    def list(self, request):
        name = request.GET.get('nome')
        period_init = request.GET.get('periodo_inicio')
        period_end = request.GET.get('periodo_fim')

        from datetime import datetime, timedelta

        if not (period_init and period_end):
            period_init = datetime.now().date()
            period_end = period_init + timedelta(days=6)

        queryset = Event.objects.filter(ticketavailable__gt=0).order_by('-presentationdate')

        try:
            try:
                # Foi necessário utilizar raw query para tornar a busca com datas compatível com o banco SQL SERVER.
                queryset = Event.get_events_by_dates(period_init, period_end, previous_queryset=queryset)
            except ValueError as e:
                raise ParseError(detail=e)

            if name:
                queryset = queryset.filter(showid__name__contains=name)

        except Exception as e:
            erro = {
                'caminho': 'EventosViewSet > list',
                'mensagem': str(e)
            }
            logger.error('Erro: %r', erro)
            raise Exception(e)

        lista_eventos = []
        for item in queryset:
            lista_eventos.append({
                'IdEvento': item.showid.id,
                'TipoEspetaculo': item.showid.showtypeid.name,
                'Titulo': item.showid.name,
                'Sintese': item.showid.synopsis,
                'Data': item.presentationdate.strftime('%d/%m/%Y'),
                'StatusInscricao': 'Inscrições abertas'
            })

        return Response(lista_eventos)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response({
                'IdEvento': instance.showid.id,
                'TipoEspetaculo': instance.showid.showtypeid.name,
                'Titulo': instance.showid.name,
                'Sintese': instance.showid.synopsis,
                'Data': instance.presentationdate.strftime('%d/%m/%Y'),
                'StatusInscricao': 'Inscrições abertas'
            })


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

        queryset = Event.objects.filter(inscription__userid__id=request.user.id).order_by('-schedule')

        try:
            try:
                if period_init and period_end:
                    # Foi necessário utilizar raw query para tornar a busca com datas compatível com o banco SQL SERVER.
                    queryset = Event.get_events_by_user_and_dates(request.user.id, period_init, period_end, previous_queryset=queryset)
                else:
                    period_init = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
                    queryset = Event.get_events_by_user_and_dates(request.user.id, period_init, previous_queryset=queryset)
            except ValueError as e:
                raise ParseError(detail=e)

            if name:
                queryset = queryset.filter(showid__name__contains=name)
            if local:
                queryset = queryset.filter(local__contains=local)

        except Exception as e:
            erro = {
                'caminho': 'EventosUsuarioViewSet > list',
                'mensagem': str(e)
            }
            logger.error('Erro: %r', erro)
            raise Exception(e)

        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        try:
            inscriptions = instance.inscription_set.filter(userid=request.user)
            if not inscriptions.exists():
                raise NotFound()
        except Exception as e:
            raise ValidationError(detail=e)

        serializer = EventDetailSerializer(instance, context={'request': request})
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
