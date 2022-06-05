import json

import pytest
from hives.models import Hive
from apiaries.models import Apiary


@pytest.mark.django_db
def test_create_hive(client, user, token):
    apiary_instance = Apiary.objects.create(name="test apiary", user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    response = client.post("/hives/create/", data=json.dumps({
        "type": "test hive",
        "number": 1,
        "apiary": apiary_instance.pk
    }), content_type='application/json')
    hive_instance = Hive.objects.last()
    data = response.data
    assert hive_instance.type == data["type"]
    assert hive_instance.number == data["number"]
    assert hive_instance.apiary.pk == data["apiary"]


@pytest.mark.django_db
def test_list_hive(client, user, token):
    apiary_instance = Apiary.objects.create(name="test apiary1", user=user)
    Hive.objects.create(type="test hive 1", number=1, apiary=apiary_instance)
    Hive.objects.create(type="test hive 2", number=2, apiary=apiary_instance)
    Hive.objects.create(type="test hive 3", number=3, apiary=apiary_instance)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    response = client.get("/hives/list/")
    assert response.status_code == 200
    assert len(response.data) == 3


@pytest.mark.django_db
def test_update_hive(client, user, token):
    apiary_instance = Apiary.objects.create(name="test apiary", user=user)
    hive_instance = Hive.objects.create(type="test hive", number=1, apiary=apiary_instance)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    response = client.put(f"/hives/update/{hive_instance.pk}", data=json.dumps(dict(type="changed hive")),
                          content_type='application/json')
    assert response.status_code == 200
    assert response.data["type"] == "changed hive"


@pytest.mark.django_db
def test_delete_hive(client, user, token):
    apiary_instance = Apiary.objects.create(name="test name", user=user)
    hive_instance = Hive.objects.create(type="test hive", number=1, apiary=apiary_instance)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    response = client.delete(f"/apiaries/delete/{hive_instance.pk}")
    assert response.status_code == 204
    assert response.data == hive_instance.pk
