import pytest

from tests.base_test import BaseTest


class TestDeleteObject(BaseTest):

    @pytest.mark.usefixtures("object_id")
    def test_delete_object(self, object_id):
        self.delete_object.delete_object(object_id)
        self.delete_object.check_response_is_200()
        self.get_object.get_single_object(object_id)
        self.get_object.check_response_is_404()


class TestDeleteObjectNegative(BaseTest):

    def test_delete_object_with_id_is_0(self):
        self.delete_object_neg.delete_object_with_id_is_0()
        self.delete_object_neg.check_response_is_404()

    def test_delete_object_with_non_existed_id(self):
        self.delete_object_neg.delete_object_with_non_existed_id()
        self.delete_object_neg.check_response_is_404()