import random
import requests

from methods.base_methods import BaseMethods
from models.object_model import UpdateObjectModel


class UpdateObject(BaseMethods):

    def update_object(self, obj_id):
        self.response = requests.put(
            url=self.endpoints.UPDATE_OBJECT(obj_id),
            json=self.payloads.update_object
        )
        UpdateObjectModel(**self.response.json())

    def patch_object(self, obj_id):
        self.response = requests.patch(
            url=self.endpoints.UPDATE_OBJECT(obj_id),
            json=random.choice(self.payloads.patch_object)
        )
        UpdateObjectModel(**self.response.json())
