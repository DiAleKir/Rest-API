from tests.base_test import BaseTest


class TestUpdateObject(BaseTest):

    def test_update_object(self, object_id):
        self.update_object.update_object(object_id)
        self.update_object.check_response_is_200()