import random

import allure
import requests

from methods.base_methods import BaseMethods
from models.object_model import UpdateObjectModel


class UpdateObject(BaseMethods):

    @allure.step("Обновить всю информацию об объекте")
    def update_object(self, obj_id):
        self.response = requests.put(
            url=self.endpoints.UPDATE_OBJECT(obj_id),
            json=self.payloads.update_object
        )
        UpdateObjectModel(**self.response.json())

    @allure.step("Обновить часть информации об объекте")
    def patch_object(self, obj_id):
        self.response = requests.patch(
            url=self.endpoints.UPDATE_OBJECT(obj_id),
            json=random.choice(self.payloads.patch_object)
        )
        UpdateObjectModel(**self.response.json())
