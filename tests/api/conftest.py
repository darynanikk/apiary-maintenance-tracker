import json
import pytest

from users.models import User
from rest_framework.test import APIClient


@pytest.fixture
def user():
    """Verified user"""

    user_data = dict(
        first_name="Daryna",
        last_name="Nikitenko",
        phone="+380672533122",
        email="darynadobro@gmail.com",
        password="password",
        is_verified=True,
    )

    user = User.objects.create_user(**user_data)
    return user


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def auth_client(client):
    user_data = dict(
        email="darynadobro@gmail.com",
        password="password"
    )
    client.post("/users/auth/login/", data=json.dumps(user_data), content_type='application/json')
    return client


@pytest.fixture
def token(client):
    user_data = dict(
        email="darynadobro@gmail.com",
        password="password"
    )
    response = client.post("/users/auth/login/", data=json.dumps(user_data), content_type='application/json')
    return response.data["token"]
