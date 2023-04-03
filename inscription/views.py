import logging
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from user.auth import CustomJWTAuthentication, isAuthenticated

from .models import Inscription
from .serializers import InscriptionSerializer
from .utils import dia_da_semana

logger = logging.getLogger(__name__)


class InscricaoVoucherViewSet(viewsets.GenericViewSet):
    serializer_class = InscriptionSerializer
    queryset = Inscription.objects.all()
    authentication_classes = (CustomJWTAuthentication,)
    permission_classes = [isAuthenticated]
    http_method_names = ['get']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if not (instance.userid.id == request.user.id):
            raise PermissionDenied()

        try:
            ticket = {
                'inscricao_id': str(instance.id),
                'nome': instance.userid.name,
                'rf': instance.userid.rf,
                'evento':  instance.eventid.showid.name,
                'data': '{} - {}'.format(instance.eventid.presentationdate.strftime("%d/%m/%Y"), dia_da_semana(instance.eventid.presentationdate)),
                'horario': instance.eventid.schedule.strftime("%H:%M"),
                'local': instance.eventid.local,
                'endereco': instance.eventid.address,
                'categoria': instance.eventid.showid.showtypeid.name,
                'vale': 'Vale ' + instance.eventid.ticketbymember + ' ingresso(s)'
            }
        except Exception as e:
            erro = {
                'caminho': 'InscricaoVoucherViewSet > retrieve',
                'mensagem': str(e)
            }
            logger.error('Erro: %r', erro)
            raise Exception(e)

        return Response(ticket)
