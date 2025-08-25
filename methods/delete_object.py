import requests

from methods.base_methods import BaseMethods
from models.object_model import ObjectModel


class DeleteObject(BaseMethods):

    def delete_object(self, obj_id):
        self.response = requests.delete(self.endpoints.DELETE_OBJECT(obj_id))
