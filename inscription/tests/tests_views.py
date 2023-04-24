from rest_framework import status
from rest_framework.test import APIClient
from unittest import TestCase
from user.models import User
from inscription.utils import is_base64


class InscricaoVoucherViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.url_base = '/api/v1/inscricao'

        # Busca e autentica usuário existente.
        self.user = User.objects.get(rf='1845721')
        self.client.force_authenticate(user=self.user)

    def test_retrieve(self):
        id = '41584'
        response = self.client.get(self.url_base + '/{}/voucher'.format(id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
