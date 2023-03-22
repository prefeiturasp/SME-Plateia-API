from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Inscription
from .serializers import InscriptionsSerializer


class InscriptionsViewSet(viewsets.ModelViewSet):
    serializer_class = InscriptionsSerializer
    queryset = Inscription.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = (JWTAuthentication,)
    http_method_names = ['get']

    def list(self, request):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)
