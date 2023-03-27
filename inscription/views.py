from rest_framework.response import Response
from rest_framework import viewsets

from user.auth import CustomJWTAuthentication, isAuthenticated
from .models import Inscription
from .serializers import InscriptionsSerializer

class InscriptionsViewSet(viewsets.GenericViewSet):
    serializer_class = InscriptionsSerializer
    queryset = Inscription.objects.all()
    authentication_classes = (CustomJWTAuthentication,)
    permission_classes = [isAuthenticated]
    http_method_names = ['get']

    def list(self, request):
        self.queryset = Inscription.objects.filter(userid=request.user)
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)
