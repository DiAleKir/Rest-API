import requests

from methods.base_methods import BaseMethods


class GetObject(BaseMethods):

    def get_single_object(self, obj_id):
        self.response = requests.get(self.endpoints.GET_OBJECT_SINGLE(obj_id))