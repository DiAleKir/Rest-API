import random

import allure
import requests

from methods.base_methods import BaseMethods


class DeleteObject(BaseMethods):

    @allure.step("Удалить объект")
    def delete_object(self, obj_id):
        self.response = requests.delete(self.endpoints.DELETE_OBJECT(obj_id))


class DeleteObjectNegative(BaseMethods):

    @allure.step("Удалить объект c id равным 0")
    def delete_object_with_id_is_0(self):
        self.response = requests.delete(self.endpoints.DELETE_OBJECT(0))

    @allure.step("Удалить объект с несуществующим id")
    def delete_object_with_non_existed_id(self):
        self.response = requests.delete(self.endpoints.DELETE_OBJECT(random.randint(30, 100)))
