from rest_framework.test import APITestCase, RequestsClient
from django.urls import reverse
from rest_framework import status
from apiary_maintenance_service import settings
import json
import os
from users.models import User
from users.serializers import UserSerializer

path = settings.BASE_DIR

def get_test_user():
    file_path = os.path.join(path, "auth_service/tests/test_data/models.json")
    with open(file_path, 'r') as f:
        data = json.load(f)
        user_data = data['user']
        return user_data


class TestViews(APITestCase):

    def setUp(self):
        self.client = RequestsClient()
        self.email_verify_url = reverse('email-verify')
        self.signup_user_url = reverse('user_signup')

    def test_user_signup(self):
        params = get_test_user()
        abs_url = f'http://127.0.0.1:8000{self.signup_user_url}'
        response = self.client.post(abs_url, params)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(User.objects.count(), 1)

