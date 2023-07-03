from drf_spectacular.utils import OpenApiExample, OpenApiResponse, OpenApiParameter, OpenApiTypes
from .serializers import EventSerializer


def get_events_list_scheme():
    return {
        'description': 'Busca eventos.',
        'responses': {
            200: OpenApiResponse(
                description='200',
                response=EventSerializer,
                examples=[
                    OpenApiExample(
                        name='Retorno 1',
                        value={
                            "IdEvento": 1767,
                            "TipoEspetaculo": "TEATRO",
                            "Titulo": "Hip Hop Blues - Espólio das águas",
                            "Sintese": "\"Núcleo Bartolomeu de Depoimentos apresentará, no Teatro de Arena  Eugênio Kusnet, a peça “Hip Hop Blues Espólio das águas”, resultado de um processo pós-  pandêmico em diálogo com a reflexão sobre os 20 anos de pesquisa continuada do Núcleo  Bartolomeu.  Chovia, chovia muito. Os rios transbordaram e ocuparam São Paulo, reivindicando seu lugar  de fala, de existência. \"\"Hip-Hop Blues - Espólio das águas\"\" é um espetáculo tecido em  fragmentos onde seis atores buscam dar contorno as águas que correram nesses tempos.  Num jogo cênico que fricciona depoimento e ficção, o centro da ágora é permeado por  histórias e ancestralidades que revelam e contrapõem o racismo, a moralidade, a  lgtqia+fobia, a intolerância, a supremacia branca e patriarcal e seus inúmeros braços  estruturais.\"",
                            "Data": "09/07/2023",
                            "StatusInscricao": "Inscrições abertas"
                        }
                    )
                ]
            ),
            400: OpenApiResponse(
                description='400',
                response=EventSerializer,
                examples=[
                    OpenApiExample(
                        name='Erro formato parâmetro de data',
                        value={
                            "detail": "['O valor “20/23/20” tem um formato inválido. Deve estar no formato YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ].']"
                        }
                    )
                ]
            ),
        },
        'parameters': [
            OpenApiParameter(name='nome', description='Nome do evento', required=False, type=OpenApiTypes.STR),
            OpenApiParameter(name='periodo_inicio', description='Data início período de busca. formato: YYYY-MM-DD HH:MM',
                             required=False, type=OpenApiTypes.DATETIME),
            OpenApiParameter(name='periodo_fim', description='Data fim período de busca. formato: YYYY-MM-DD HH:MM',
                             required=False, type=OpenApiTypes.DATETIME),
        ]

    }


def get_events_retrieve_scheme():
    return {
        'description': 'Busca evento por ID.',
        'responses': {
            200: OpenApiResponse(
                description='200',
                response=EventSerializer,
                examples=[
                    OpenApiExample(
                        name='Retorno 1',
                        value={
                            "IdEvento": 1767,
                            "TipoEspetaculo": "TEATRO",
                            "Titulo": "Hip Hop Blues - Espólio das águas",
                            "Sintese": "\"Núcleo Bartolomeu de Depoimentos apresentará, no Teatro de Arena  Eugênio Kusnet, a peça “Hip Hop Blues Espólio das águas”, resultado de um processo pós-  pandêmico em diálogo com a reflexão sobre os 20 anos de pesquisa continuada do Núcleo  Bartolomeu.  Chovia, chovia muito. Os rios transbordaram e ocuparam São Paulo, reivindicando seu lugar  de fala, de existência. \"\"Hip-Hop Blues - Espólio das águas\"\" é um espetáculo tecido em  fragmentos onde seis atores buscam dar contorno as águas que correram nesses tempos.  Num jogo cênico que fricciona depoimento e ficção, o centro da ágora é permeado por  histórias e ancestralidades que revelam e contrapõem o racismo, a moralidade, a  lgtqia+fobia, a intolerância, a supremacia branca e patriarcal e seus inúmeros braços  estruturais.\"",
                            "Data": "09/07/2023",
                            "StatusInscricao": "Inscrições abertas"
                        }
                    )
                ]
            ),
            404: OpenApiResponse(
                description='404',
                response=EventSerializer,
                examples=[
                    OpenApiExample(
                        name='ID não encontrado',
                        value={
                            "detail": "Não encontrado."
                        }
                    )
                ]
            ),
        },
    }


def get_user_events_list_scheme():
    return {
        'description': 'Busca meus eventos.',
        'request': {
            'headers': {
                'Authorization': 'Bearer <access_token>'
            }
        },
        'responses': {
            200: OpenApiResponse(
                description='200',
                response=EventSerializer,
                examples=[
                    OpenApiExample(
                        name='Retorno 1',
                        value={
                            "count": 1,
                            "next": None,
                            "previous": None,
                            "results": [
                                {
                                    "id": 1,
                                    "local": "TESTE",
                                    "schedule": "2023-03-28T16:55:11-03:00",
                                    "showid": {
                                        "name": "Rayane Maria dos Santos",
                                        "files": []
                                    },
                                    "presentationdate": "2023-03-28T16:55:09-03:00",
                                    "cityid": {
                                        "id": "0861D9B3-8EC3-E011-9B36-00155D033206",
                                        "name": "SP",
                                        "state": 1,
                                        "createdate": "2023-03-28T16:55:00-03:00",
                                        "updatedate": "2023-03-28T16:55:02-03:00"
                                    }
                                }
                            ]
                        }
                    )
                ]
            ),
            400: OpenApiResponse(
                description='400',
                response=EventSerializer,
                examples=[
                    OpenApiExample(
                        name='Erro formato parâmetro de data',
                        value={
                            "detail": "['O valor “20/23/20” tem um formato inválido. Deve estar no formato YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ].']"
                        }
                    )
                ]
            ),
            401: OpenApiResponse(
                description='401',
                response=EventSerializer,
                examples=[
                    OpenApiExample(
                        name='Token inválido/expirado',
                        value={
                            "detail": "O token informado não é válido para qualquer tipo de token",
                            "code": "token_not_valid",
                            "messages": [
                                {
                                    "token_class": "AccessToken",
                                    "token_type": "access",
                                    "message": "O token é inválido ou expirado"
                                }
                            ]
                        }
                    ),
                    OpenApiExample(
                        name='Token não enviado/mal formatado',
                        value={
                            "detail": "As credenciais de autenticação não foram fornecidas."
                        }
                    )
                ]
            ),
            404: OpenApiResponse(
                description='404',
                response=EventSerializer,
                examples=[
                    OpenApiExample(
                        name='Página inválida',
                        value={
                            "detail": "Página inválida."
                        }
                    )
                ]
            ),
        },
        'parameters': [
            OpenApiParameter(name='nome', description='Nome do evento', required=False, type=OpenApiTypes.STR),
            OpenApiParameter(name='periodo_inicio', description='Data início período de busca. formato: YYYY-MM-DD HH:MM',
                             required=False, type=OpenApiTypes.DATETIME),
            OpenApiParameter(name='periodo_fim', description='Data fim período de busca. formato: YYYY-MM-DD HH:MM',
                             required=False, type=OpenApiTypes.DATETIME),
            OpenApiParameter(name='local', description='Local do evento', required=False, type=OpenApiTypes.STR),
            OpenApiParameter(name='page', description='Um número de página dentro do conjunto de resultados paginados',
                             required=False, type=OpenApiTypes.INT),
        ]

    }


def get_user_events_retrieve_scheme():
    return {
        'description': 'Busca evento por ID.',
        'request': {
            'headers': {
                'Authorization': 'Bearer <access_token>'
            }
        },
        'responses': {
            200: OpenApiResponse(
                description='200',
                response=EventSerializer,
                examples=[
                    OpenApiExample(
                        name='Retorno 1',
                        value={
                            "id": 1,
                            "local": "TESTE",
                            "address": "TESTE",
                            "partnercompany": None,
                            "presentationdate": "2023-03-28T16:55:09-03:00",
                            "schedule": "2023-03-28T16:55:11-03:00",
                            "enrollstartat": "2023-03-28T16:55:14-03:00",
                            "enrollendat": "2023-03-28T16:55:15-03:00",
                            "ticketquantity": 1,
                            "ticketavailable": 1,
                            "ticketbymember": 1,
                            "queuesize": 1,
                            "queueremaining": 1,
                            "state": 1,
                            "createdate": "2023-03-28T16:55:25-03:00",
                            "updatedate": "2023-03-28T16:55:27-03:00",
                            "showid": {
                                "id": 1,
                                "name": "Rayane Maria dos Santos",
                                "synopsis": "Show",
                                "classification": None,
                                "duration": 1,
                                "postscript": None,
                                "video": None,
                                "highlight": None,
                                "state": 1,
                                "createdate": "2023-03-28T16:54:45-03:00",
                                "updatedate": "2023-03-28T16:54:46-03:00",
                                "showtypeid": {
                                    "id": 1,
                                    "name": "Rayane Maria dos Santos",
                                    "state": 1,
                                    "createdate": "2023-03-28T16:54:21-03:00",
                                    "updatedate": "2023-03-28T16:54:23-03:00"
                                },
                                "genreid": {
                                    "id": 1,
                                    "name": "sdsd",
                                    "state": 1,
                                    "createdate": "2023-03-28T16:54:36-03:00",
                                    "updatedate": "2023-03-28T16:54:37-03:00"
                                },
                                "files": []
                            },
                            "cityid": {
                                "id": "0861D9B3-8EC3-E011-9B36-00155D033206",
                                "name": "SP",
                                "state": 1,
                                "createdate": "2023-03-28T16:55:00-03:00",
                                "updatedate": "2023-03-28T16:55:02-03:00"
                            }
                        }
                    )
                ]
            ),
            401: OpenApiResponse(
                description='401',
                response=EventSerializer,
                examples=[
                    OpenApiExample(
                        name='Token inválido/expirado',
                        value={
                            "detail": "O token informado não é válido para qualquer tipo de token",
                            "code": "token_not_valid",
                            "messages": [
                                {
                                    "token_class": "AccessToken",
                                    "token_type": "access",
                                    "message": "O token é inválido ou expirado"
                                }
                            ]
                        }
                    ),
                    OpenApiExample(
                        name='Token não enviado/mal formatado',
                        value={
                            "detail": "As credenciais de autenticação não foram fornecidas."
                        }
                    )
                ]
            ),
            404: OpenApiResponse(
                description='404',
                response=EventSerializer,
                examples=[
                    OpenApiExample(
                        name='ID não encontrado',
                        value={
                            "detail": "Não encontrado."
                        }
                    )
                ]
            ),
        },
    }


def get_locais_eventos_usuario_list_scheme():
    return {
        'parameters': [
            OpenApiParameter(name='termo', description='Termo de pesquisa', required=True, type=OpenApiTypes.STR),
        ],
        'description': 'Listagem de locais dos eventos de um usuário para autocomplete mediante entrada de algum termo de pesquisa.'

    }
