import json

import pytest
from apiaries import models


@pytest.mark.django_db
def test_create_apiary(client, user, token):
    body = dict(
        name="test name",
        is_hidden=False
    )
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    response = client.post("/apiaries/create/", data=json.dumps(body), content_type='application/json')
    data = response.data
    instance = models.Apiary.objects.last()
    assert instance.name == data["name"]
    assert instance.is_hidden == data["is_hidden"]
    assert instance.user.email == data["user"]


@pytest.mark.django_db
def test_list_apiary(client, user, token):
    models.Apiary.objects.create(name="test name1", user=user)
    models.Apiary.objects.create(name="test name2", user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    response = client.get("/apiaries/list/")
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_update_apiary(client, user, token):
    instance = models.Apiary.objects.create(name="test name", user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    payload = dict(name="changed test name")
    response = client.put(f"/apiaries/update/{instance.pk}", data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 200
    assert response.data["name"] == "changed test name"


@pytest.mark.django_db
def test_delete_apiary(client, user, token):
    instance = models.Apiary.objects.create(name="test name", user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    response = client.delete(f"/apiaries/delete/{instance.pk}")
    assert response.status_code == 204
    assert response.data == instance.pk
