from tests.base_test import BaseTest


class TestDeleteObject(BaseTest):

    def test_delete_object(self, object_id):
        self.delete_object.delete_object(object_id)
        self.delete_object.check_response_is_200()
        self.get_object.get_single_object(object_id)
        self.get_object.check_response_is_404()