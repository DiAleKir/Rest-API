from methods.create_object import CreateObject, CreateObjectNegative
from methods.delete_object import DeleteObject, DeleteObjectNegative
from methods.get_object import GetObject, GetObjectNegative
from methods.update_object import UpdateObject


class BaseTest:

    def setup_method(self):
        self.get_object = GetObject()
        self.create_object = CreateObject()
        self.delete_object = DeleteObject()
        self.update_object = UpdateObject()
        self.create_object_neg = CreateObjectNegative()
        self.get_object_neg = GetObjectNegative()
        self.delete_object_neg = DeleteObjectNegative()
