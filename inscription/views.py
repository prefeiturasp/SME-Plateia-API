import logging
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, ValidationError
from drf_spectacular.utils import extend_schema

from user.auth import CustomJWTAuthentication, isAuthenticated

from .models import Inscription
from .serializers import InscriptionSerializer, TicketSerializer
from .utils import QRCode_generate, generate_ticket_voucher
from .swagger import get_retrieve_voucher_scheme,  get_pdf_scheme

logger = logging.getLogger(__name__)


class InscricaoVoucherViewSet(viewsets.GenericViewSet):
    serializer_class = InscriptionSerializer
    queryset = Inscription.objects.all()
    authentication_classes = (CustomJWTAuthentication,)
    permission_classes = [isAuthenticated]
    http_method_names = ['get']

    @extend_schema(**get_retrieve_voucher_scheme())
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if not (instance.userid.id == request.user.id):
            raise PermissionDenied()

        ticket_dict = instance.get_ticket_dict()
        ticket_str = instance.ticket_to_string(ticket_dict)

        qrcode = QRCode_generate(ticket_str)

        if not qrcode:
            raise ValidationError(detail='Não foi possível gerar QRcode')

        ticket_dict['qrcode'] = qrcode

        pdf = generate_ticket_voucher(ticket_dict)
        if not pdf:
            raise ValidationError(detail='Não foi possível retornar voucher')

        ticket_dict['voucher'] = pdf
        ticket_dict['inscricao_id'] = instance.id
        serializer = TicketSerializer(data=ticket_dict)

        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)

    @extend_schema(**get_pdf_scheme())
    def pdf(self, request, *args, **kwargs):
        instance = self.get_object()

        if not (instance.userid.id == request.user.id):
            raise PermissionDenied()

        ticket_dict = instance.get_ticket_dict()
        ticket_str = instance.ticket_to_string(ticket_dict)
        qrcode = QRCode_generate(ticket_str)

        if not qrcode:
            raise ValidationError(detail='Não foi possível gerar QRcode')

        ticket_dict['qrcode'] = qrcode

        pdf = generate_ticket_voucher(ticket_dict)
        if not pdf:
            raise ValidationError(detail='Não foi possível retornar voucher')

        return Response({'voucher': pdf})
