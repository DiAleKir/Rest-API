import requests

from methods.base_methods import BaseMethods


class DeleteObject(BaseMethods):

    def delete_object(self, obj_id):
        self.response = requests.delete(self.endpoints.DELETE_OBJECT(obj_id))
