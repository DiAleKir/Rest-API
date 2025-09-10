import allure
import requests

from methods.base_methods import BaseMethods
from models.object_model import CreateObjectModel


class CreateObject(BaseMethods):

    @allure.step("Создать объект")
    def create_object(self):
        self.response = requests.post(
            url=self.endpoints.ADD_OBJECT,
            json=self.payloads.new_object
        )
        model = CreateObjectModel(**self.response.json())
        return model.id

class CreateObjectNegative(BaseMethods):

    @allure.step("Создать объект без тела запроса")
    def create_empty_object(self):
        self.response = requests.post(
            url=self.endpoints.ADD_OBJECT,
            json=self.payloads_neg.empty_body
        )

    @allure.step("Создать объект без имени")
    def create_object_without_name(self):
        self.response = requests.post(
            url=self.endpoints.ADD_OBJECT,
            json=self.payloads_neg.empty_name
        )

    @allure.step("Создать объект с невалидным именем")
    def create_object_with_invalid_name(self):
        self.response = requests.post(
            url=self.endpoints.ADD_OBJECT,
            json=self.payloads_neg.invalid_name
        )

    @allure.step("Создать объект без data в теле запроса")
    def create_object_without_data(self):
        self.response = requests.post(
            url=self.endpoints.ADD_OBJECT,
            json=self.payloads_neg.body_without_data
        )

    @allure.step("Создать объект без цены")
    def create_object_without_price(self):
        self.response = requests.post(
            url=self.endpoints.ADD_OBJECT,
            json=self.payloads_neg.data_without_price
        )

    @allure.step("Создать объект с отрицательной ценой")
    def create_object_with_negative_price(self):
        self.response = requests.post(
            url=self.endpoints.ADD_OBJECT,
            json=self.payloads_neg.negative_price
        )

    @allure.step("Создать объект с ценой равной 0")
    def create_object_with_price_is_0(self):
        self.response = requests.post(
            url=self.endpoints.ADD_OBJECT,
            json=self.payloads_neg.price_is_0
        )

    @allure.step("Создать объект с невалидной ценой")
    def create_object_with_invalid_price(self):
        self.response = requests.post(
            url=self.endpoints.ADD_OBJECT,
            json=self.payloads_neg.invalid_price
        )

    @allure.step("Создать объект с годом равным 0")
    def create_object_with_year_is_0(self):
        self.response = requests.post(
            url=self.endpoints.ADD_OBJECT,
            json=self.payloads_neg.year_is_0
        )

    @allure.step("Создать объект с отрицательным годом")
    def create_object_with_negative_year(self):
        self.response = requests.post(
            url=self.endpoints.ADD_OBJECT,
            json=self.payloads_neg.negative_year
        )

    @allure.step("Создать объект с невалидным годом")
    def create_object_with_invalid_year(self):
        self.response = requests.post(
            url=self.endpoints.ADD_OBJECT,
            json=self.payloads_neg.invalid_year
        )

    @allure.step("Создать объект с невалидным cpu")
    def create_object_with_invalid_cpu(self):
        self.response = requests.post(
            url=self.endpoints.ADD_OBJECT,
            json=self.payloads_neg.invalid_cpu
        )

    @allure.step("Создать объект с невалидным жестким диском")
    def create_object_with_invalid_hard_disk(self):
        self.response = requests.post(
            url=self.endpoints.ADD_OBJECT,
            json=self.payloads_neg.invalid_hard_disk
        )
