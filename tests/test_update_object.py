import pytest

from tests.base_test import BaseTest


class TestUpdateObject(BaseTest):

    @pytest.mark.usefixtures("object_id")
    def test_update_object(self, object_id):
        self.update_object.update_object(object_id)
        self.update_object.check_response_is_200()

    @pytest.mark.usefixtures("object_id")
    def test_patch_object(self, object_id):
        self.update_object.patch_object(object_id)
        self.update_object.check_response_is_200()
