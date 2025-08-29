import random

import allure
import requests

from methods.base_methods import BaseMethods


class GetObject(BaseMethods):

    @allure.step("Найти объект по id")
    def get_single_object(self, obj_id):
        self.response = requests.get(self.endpoints.GET_OBJECT_SINGLE(obj_id))

    @allure.step("Найти все объекты")
    def get_all_object(self):
        self.response = requests.get(self.endpoints.GET_ALL_OBJECTS)

    @allure.step("Найти несколько объектов по id")
    def get_objects_by_ids(self):
        id_1 = random.randint(1, 6)
        id_2 = random.randint(7, 13)
        self.response = (requests.get
                         (self.endpoints.GET_OBJECTS_BY_IDS(id_1, id_2)))
        return id_1, id_2
