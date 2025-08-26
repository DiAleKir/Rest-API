import pytest

from tests.base_test import BaseTest


class TestGetObject(BaseTest):

    @pytest.mark.usefixtures("object_id")
    def test_get_single_object(self, object_id):
        self.get_object.get_single_object(object_id)
        self.get_object.check_response_is_200()

    def test_get_list_of_all_objects(self):
        self.get_object.get_all_object()
        self.get_object.check_response_is_200()
        self.get_object.check_response_body_is_not_empty()

    def test_get_objects_by_ids(self):
        id_1, id_2 = self.get_object.get_objects_by_ids()
        self.get_object.check_response_is_200()
        self.get_object.check_object_id(id_1, id_2)
