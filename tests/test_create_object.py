from tests.base_test import BaseTest


class TestCreateObject(BaseTest):

    def test_create_object(self):
        obj_id = self.create_object.create_object()
        self.create_object.check_response_is_200()
        self.create_object.check_name()
        self.delete_object.delete_object(obj_id)
        self.delete_object.check_response_is_200()
        self.get_object.get_single_object(obj_id)
        self.get_object.check_response_is_404()
