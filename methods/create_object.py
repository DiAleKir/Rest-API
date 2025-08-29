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
