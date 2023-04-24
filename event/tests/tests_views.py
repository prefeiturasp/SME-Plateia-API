from django.http import HttpRequest
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.test import APIClient
from unittest import TestCase

from event.models import Event
from event.serializers import EventSerializer, EventDetailSerializer
from user.models import User


class EventosUsuarioViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.url_base = '/api/v1/meus_eventos'

        # Busca e autentica usuário existente.
        self.user = User.objects.get(rf='1845721')
        self.client.force_authenticate(user=self.user)

        # Pagina manualmente
        self.paginator = PageNumberPagination()
        # Mock de request
        self.request = HttpRequest()
        self.request.query_params = {'page': 1, 'page_size': 10}

        # Eventos do usuário autenticado
        self.user_events = Event.objects.filter(inscription__userid=self.user).order_by('-schedule')

    def test_list_events(self):
        response = self.client.get(self.url_base + '?page=1')
        paginated_events = self.paginator.paginate_queryset(self.user_events, request=self.request)
        serializer = EventSerializer(paginated_events, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def test_filter_by_name(self):
        response = self.client.get(self.url_base + '?page=1&nome=La Mancha')
        events = self.user_events.filter(showid__name__contains='La Mancha')
        paginated_events = self.paginator.paginate_queryset(events, request=self.request)
        serializer = EventSerializer(paginated_events, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def test_filter_by_date_range(self):
        periodo_inicio = '2017-06-12 14:00:00'
        periodo_fim = '2017-06-12 14:00:00'
        response = self.client.get(self.url_base + '?page={}&periodo_inicio={}&periodo_fim={}'.format('1', periodo_inicio, periodo_fim))
        events = Event.get_events_by_user_and_dates(self.user.id, periodo_inicio, periodo_fim, self.user_events)
        paginated_events = self.paginator.paginate_queryset(events, request=self.request)
        serializer = EventSerializer(paginated_events, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def test_filter_by_location(self):
        response = self.client.get(self.url_base + '?page=1&local=Teatro')
        events = self.user_events.filter(local__icontains='Teatro')
        paginated_events = self.paginator.paginate_queryset(events, request=self.request)
        serializer = EventSerializer(paginated_events, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def test_retrieve_event(self):
        event = self.user_events.first()
        response = self.client.get(self.url_base + '/' + str(event.id) + '/')

        serializer = EventDetailSerializer(self.user_events.first())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class LocaisEventosUsuarioViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.url_base = '/api/v1/locais_meus_eventos'

        # Busca e autentica usuário existente.
        self.user = User.objects.get(rf='1845721')
        self.client.force_authenticate(user=self.user)

        # Eventos do usuário autenticado
        self.user_events = Event.objects.filter(inscription__userid=self.user).order_by('-schedule')

    def test_list(self):
        termo = 'Teatro'
        response = self.client.get(self.url_base + '?termo={}'.format(termo))

        locations = self.user_events.filter(local__icontains=termo).values_list('local', flat=True).distinct()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), locations.count())
