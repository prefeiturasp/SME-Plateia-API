from drf_spectacular.utils import OpenApiExample, OpenApiResponse
from .serializers import InscriptionSerializer


def get_retrieve_voucher_scheme():
    return {
        'description': 'Retorna informações do ingresso com QRcode',
        'responses': {
            200: OpenApiResponse(
                description='200',
                response=InscriptionSerializer,
                examples=[
                    OpenApiExample(
                        name='Retorno 1',
                        value={
                            "inscricao_id": "41584",
                            "nome": "MARIA ISABEL NOGUEIRA DA CRUZ",
                            "rf": "1845721",
                            "evento": "O Homem de La Mancha",
                            "data": "17/06/2017 - sábado",
                            "horario": "17:00",
                            "local": "Teatro Alfa",
                            "endereco": "R. Bento Branco de Andrade Filho, 722 - Santo Amaro",
                            "categoria": "TEATRO",
                            "ingressos_por_membro": "Vale 2 ingresso(s)",
                            "qrcode": "<base64>"
                        }
                    )
                ]
            ),
        },
    }
