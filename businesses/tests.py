from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from .models import Business


class BusinessTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='alberto@test.com',
            email='alberto@test.com',
            password='Test12345!'
        )

        self.client.force_authenticate(user=self.user)

    def test_create_business(self):
        response = self.client.post(
            '/api/businesses/',
            {
                'name': 'Beto Company'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        business = Business.objects.get(name='Beto Company')

        self.assertEqual(business.user, self.user)