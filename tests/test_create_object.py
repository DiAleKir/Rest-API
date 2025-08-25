import pytest

from tests.base_test import BaseTest


class TestCreateObject(BaseTest):

    @pytest.mark.skip("При работе с фикстурой создаёт лишний объект")
    def test_create_object(self):
        self.create_object.create_object()
        self.create_object.check_response_is_200()
        self.create_object.check_name()