from tests.base_test import BaseTest


class TestDeleteObject(BaseTest):

    def test_delete_object(self):
        self.delete_object.delete_object("ff8081819782e69e0198dc5a92ec1d8e")
        self.delete_object.check_response_is_200()
        self.get_object.get_single_object("ff8081819782e69e0198dc5a92ec1d8e")
        self.get_object.check_response_is_404()