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
        self.response = (requests.get(self.endpoints.GET_OBJECTS_BY_IDS(id_1, id_2)))
        return id_1, id_2

class GetObjectNegative(BaseMethods):

    @allure.step("Найти объект с несуществующим id")
    def get_single_object_with_non_existent_id(self):
        self.response = requests.get(self.endpoints.GET_OBJECT_SINGLE(random.randint(30, 100)))

    @allure.step("Найти объект с невалидным id")
    def get_single_object_with_invalid_id(self, invalid_id):
        self.response = requests.get(self.endpoints.GET_OBJECT_SINGLE(invalid_id))

    @allure.step("Найти объект с id равным 0")
    def get_single_object_with_id_is_0(self):
        self.response = requests.get(self.endpoints.GET_OBJECT_SINGLE(0))

    @allure.step("Найти объекты с несуществующими id")
    def get_objects_with_non_existent_id(self):
        self.response = requests.get(self.endpoints.GET_OBJECTS_BY_IDS(
            random.randint(30, 100), random.randint(30, 100)))

    @allure.step("Найти объекты с невалидными id")
    def get_objects_with_invalid_id(self, id_1, id_2):
        self.response = requests.get(self.endpoints.GET_OBJECTS_BY_IDS(id_1, id_2))

    @allure.step("Найти объекты с валидным и несуществующим id")
    def get_objects_with_one_valid_and_one_non_existent_id(self):
        id_1 = random.randint(1, 10)
        id_2 = random.randint(30, 100)
        self.response = requests.get(self.endpoints.GET_OBJECTS_BY_IDS(id_1, id_2))
        return id_1

    @allure.step("Найти объекты с валидным id и id равным 0")
    def get_objects_with_one_valid_id_and_id_is_0(self):
        id_1 = random.randint(1, 10)
        self.response = requests.get(self.endpoints.GET_OBJECTS_BY_IDS(id_1, 0))
        return id_1
