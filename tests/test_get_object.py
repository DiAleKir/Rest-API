from tests.base_test import BaseTest


class TestGetObject(BaseTest):

    def test_get_single_object(self):
        self.get_object.get_single_object("ff8081819782e69e0198dc5a92ec1d8e")
        self.get_object.check_response_is_200()
