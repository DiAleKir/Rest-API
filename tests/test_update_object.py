from tests.base_test import BaseTest


class TestUpdateObject(BaseTest):

    def test_update_object(self):
        self.update_object.update_object("ff8081819782e69e0198dc8d26621e16")
        self.update_object.check_response_is_200()