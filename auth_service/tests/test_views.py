from rest_framework.test import APITestCase, RequestsClient
from django.urls import reverse
from rest_framework import status
from apiary_maintenance_service import settings
import json
import os

from auth_service.utils import Util
from users.models import User

path = settings.BASE_DIR


def get_test_user(user):
    file_path = os.path.join(path, "auth_service/tests/test_data/models.json")
    with open(file_path, 'r') as f:
        data = json.load(f)
        user_data = data[user]
        return user_data


class TestViews(APITestCase):

    def setUp(self):
        self.client = RequestsClient()
        self.login_user_url = reverse('user_login')
        self.signup_user_url = reverse('user_signup')

    def test_user_signup(self):
        params = get_test_user('user')
        abs_url = f'http://127.0.0.1:8000{self.signup_user_url}'
        response = self.client.post(abs_url, params)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(User.objects.count(), 1)

    def test_user_login(self):
        user_test_data = get_test_user('user')
        user = User.objects.create_user(
            email=user_test_data['email'],
            first_name=user_test_data['first_name'],
            last_name=user_test_data['first_name'],
            phone=user_test_data['phone'],
            password=user_test_data['password'],
            role=user_test_data['role']
        )

        params = {
            "email": user.email,
            "password": "2F9SK32mkgJSrWfK"
        }
        abs_url = f'http://127.0.0.1:8000{self.login_user_url}'
        response = self.client.post(abs_url, params)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data["message"], "User logged in successfully")
        self.assertEquals(response_data["authenticatedUser"], {"email": user.email, "role": user_test_data['role']})
        self.assertEquals(user, Util.confirm_token(response_data["access"]))


