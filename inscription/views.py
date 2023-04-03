import logging
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, ValidationError

from user.auth import CustomJWTAuthentication, isAuthenticated

from .models import Inscription
from .serializers import InscriptionSerializer
from .utils import QRCode_generate

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
            ticket_dict = instance.get_ticket_dict()
            ticket_str = instance.ticket_to_string(ticket_dict)
            qrcode = QRCode_generate(200, 200, ticket_str)

            if not qrcode:
                raise ValidationError(detail='Não foi possível gerar QRcode')

            ticket_dict['qrcode'] = qrcode
        except Exception as e:
            erro = {
                'caminho': 'InscricaoVoucherViewSet > retrieve',
                'mensagem': str(e)
            }
            logger.error('Erro: %r', erro)
            raise Exception(e)

        return Response(ticket_dict)
