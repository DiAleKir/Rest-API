import random
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
        self.get_object.check_objects_id(id_1, id_2)


class TestGetObjectNegative(BaseTest):

    def test_get_single_object_with_nonexistent_id(self):
        self.get_object_neg.get_single_object_with_non_existent_id()
        self.get_object_neg.check_response_is_404()

    @pytest.mark.parametrize("invalid_id", ["string", "+-$@&^!", " "])
    def test_get_single_object_with_invalid_id(self, invalid_id):
        self.get_object_neg.get_single_object_with_invalid_id(invalid_id)
        self.get_object_neg.check_response_is_404()

    def test_get_object_with_id_is_0(self):
        self.get_object_neg.get_single_object_with_id_is_0()
        self.get_object_neg.check_response_is_404()

    def test_get_objects_with_nonexistent_id(self):
        self.get_object_neg.get_objects_with_non_existent_id()
        self.get_object_neg.check_response_is_200()
        self.get_object_neg.check_response_body_is_empty_list()

    @pytest.mark.parametrize("id_1, id_2", [
        ("+-$@&^!", " "),
        (30.2, "string")
    ])
    def test_get_objects_with_invalid_id(self, id_1, id_2):
        self.get_object_neg.get_objects_with_invalid_id(id_1, id_2)
        self.get_object_neg.check_response_is_200()
        self.get_object_neg.check_response_body_is_empty_list()

    def test_get_objects_with_one_valid_id_and_one_non_existent_id(self):
        id_1 = self.get_object_neg.get_objects_with_one_valid_and_one_non_existent_id()
        self.get_object_neg.check_response_is_200()
        self.get_object_neg.check_single_object_id(id_1)

    def test_get_objects_with_one_valid_id_and_id_is_0(self):
        id_1 = self.get_object_neg.get_objects_with_one_valid_id_and_id_is_0()
        self.get_object_neg.check_response_is_200()
        self.get_object_neg.check_single_object_id(id_1)

