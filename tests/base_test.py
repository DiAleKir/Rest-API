from methods.create_object import CreateObject
from methods.delete_object import DeleteObject
from methods.get_object import GetObject
from methods.update_object import UpdateObject


class BaseTest:

    def setup_method(self):
        self.get_object = GetObject()
        self.create_object = CreateObject()
        self.delete_object = DeleteObject()
        self.update_object = UpdateObject()