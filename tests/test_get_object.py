from tests.base_test import BaseTest


class TestGetObject(BaseTest):

    def test_get_single_object(self, object_id):
        self.response = self.get_object.get_single_object(object_id)
        self.get_object.check_response_is_200()