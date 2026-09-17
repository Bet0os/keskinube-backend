from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class UserTests(APITestCase):

    def test_register_user(self):
        url = reverse('user-register')

        data = {
            'first_name': 'Alberto',
            'last_name': 'Camacho',
            'email': 'alberto@test.com',
            'password': 'Test12345!',
            'confirm_password': 'Test12345!'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(
            User.objects.filter(email='alberto@test.com').exists()
        )

    def test_passwords_do_not_match(self):
        url = reverse('user-register')

        data = {
            'first_name': 'Alberto',
            'last_name': 'Camacho',
            'email': 'alberto2@test.com',
            'password': 'Test12345!',
            'confirm_password': 'Different123!'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_login_returns_jwt_tokens(self):
        User.objects.create_user(
            username='alberto@test.com',
            email='alberto@test.com',
            password='Test12345!'
        )

        response = self.client.post(
            '/api/token/',
            {
                'email': 'alberto@test.com',
                'password': 'Test12345!'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)