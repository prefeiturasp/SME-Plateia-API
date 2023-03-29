from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError
from user.auth import CustomJWTAuthentication, isAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse, OpenApiParameter
from .models import Inscription
from .serializers import InscriptionsSerializer


@extend_schema(
    request={
        'headers': {
            'Authorization': 'Bearer <access_token>'
        }
    },
    responses={
        200: {
            'description': 'Ok',
            'content': {
                'application/json': {
                    'example': {'message': 'Exemplo de resposta'}
                }
            }
        },
        400: {
            'description': 'Erro de validação',
            'content': {
                'application/json': {
                    'example': {'error': 'Mensagem de erro'}
                }
            }
        }
    },
    summary="Lista de inscrições por usuário",
    description="Retorna listagem de inscrições do usuário logado",
)
class InscriptionsViewSet(viewsets.GenericViewSet):
    serializer_class = InscriptionsSerializer
    queryset = Inscription.objects.all()
    authentication_classes = (CustomJWTAuthentication,)
    permission_classes = [isAuthenticated]
    pagination_class = PageNumberPagination
    http_method_names = ['get']

    def list(self, request):
        self.queryset = Inscription.objects.filter(userid=request.user)
        page = self.paginate_queryset(self.queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
