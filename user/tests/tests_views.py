from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from unittest import TestCase
from user.models import User


class CustomUserAuthViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.get(rf='1845721')

    def test_authenticate_user(self):
        # Teste credenciais válidas
        response = self.client.post('/api/v1/autenticacao/entrar', {
            'rf': '1845721',
            'password': '12345678teste',
        })

        self.assertEqual(response.status_code, 200)

        # Checa se retorno contem access token
        self.assertIn('access', response.data)

        access_token = response.data['access']

        # Verifica token
        decoded_token = AccessToken(access_token)
        self.assertEqual(decoded_token['user_id'], self.user.id)

    def test_fail_authenticate_user(self):
        # Teste credenciais inválidas
        response = self.client.post('/api/v1/autenticacao/entrar', {
            'rf': '1845721',
            'password': '12345678wrong',
        })

        self.assertEqual(response.status_code, 401)

        # Checa se retorno não contem access token
        self.assertNotIn('access', response.data)
