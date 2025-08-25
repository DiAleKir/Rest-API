import pytest

from methods.create_object import CreateObject
from methods.delete_object import DeleteObject


@pytest.fixture()
def object_id():
    create_object = CreateObject()
    delete_object = DeleteObject()

    create_object.create_object()
    print(create_object.response.json()['id'])
    yield create_object.response.json()['id']
    delete_object.delete_object(create_object.response.json()['id'])