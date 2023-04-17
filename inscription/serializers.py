from rest_framework import serializers
from .models import Inscription
from event.serializers import EventSerializer


class InscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inscription
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['eventid'] = '' if instance.eventid == "" or instance.eventid is None else EventSerializer(
            instance.eventid).data
        return response


class TicketSerializer(serializers.Serializer):
    inscricao_id = serializers.CharField()
    nome = serializers.CharField()
    rf = serializers.CharField()
    evento = serializers.CharField()
    data = serializers.CharField()
    horario = serializers.CharField()
    local = serializers.CharField()
    endereco = serializers.CharField()
    categoria = serializers.CharField()
    ingressos_por_membro = serializers.CharField()
    qrcode = serializers.CharField()
    voucher = serializers.CharField()
