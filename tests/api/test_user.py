import json
import pytest


@pytest.mark.django_db(transaction=True)
def test_register_user(client):
    payload = dict(
        first_name="Daryna",
        last_name="Nikitenko",
        phone="+380672533122",
        email="darynadobro@gmail.com",
        password="password"
    )

    response = client.post("/users/auth/register/", data=json.dumps(payload), content_type='application/json')

    data = response.data
    assert data["user"] == payload["email"]
    assert "password" not in data


@pytest.mark.django_db(transaction=True)
def test_login_user(user, client):
    user_data = dict(
        email="darynadobro@gmail.com",
        password="password"
    )
    response = client.post("/users/auth/login/", data=json.dumps(user_data), content_type='application/json')
    data = response.data
    assert response.status_code == 200
    assert data["user"]["email"] == "darynadobro@gmail.com"
    assert user_data["password"] not in data["user"]
    assert data["token"]
    assert data["expiry"]


@pytest.mark.django_db
def test_logout_user(user, client, token):
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    response = client.post("/users/auth/logout/")
    assert response.status_code == 204


@pytest.mark.django_db
def test_set_new_password(user, auth_client):
    obj = user.auth_token_set.last()

    user_data = dict(password="new_password")
    response = auth_client.put(f"/users/auth/password-reset/{obj.digest}",
                               data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 200
    assert response.data == {'success': 'Password Reset Successfully'}
