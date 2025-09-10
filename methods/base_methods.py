import allure

from endpoints.endpoints import Endpoints
from payloads.payloads import Payloads, PayloadsNegative


class BaseMethods:
    endpoints = Endpoints()
    payloads = Payloads()
    response = None
    payloads_neg = PayloadsNegative()

    @allure.step("Проверить, что пришёл 200 статус код")
    def check_response_is_200(self):
        assert self.response.status_code == 200, self.response.json()
        return True

    @allure.step("Проверить, что пришёл 404 статус код")
    def check_response_is_404(self):
        assert self.response.status_code == 404, self.response.json()

    @allure.step("Проверить, имя объекта соответствуют имени объекта при создании")
    def check_name(self):
        assert self.response.json()["name"] == self.payloads.new_object["name"]
        return True

    @allure.step("Проверить, что ответ от серваре не пустой")
    def check_response_body_is_not_empty(self):
        assert self.response.json() is not None

    @allure.step("Проверить, что id объектов соответстуют искомым")
    def check_objects_id(self, id_1, id_2):
        assert self.response.json()[0]['id'] == str(id_1)
        assert self.response.json()[1]['id'] == str(id_2)

    @allure.step("Проверить, что пришел 400 статус код")
    def check_response_is_400(self):
        assert self.response.status_code == 400, self.response.json()

    @allure.step("Проверить, что в ответе от сервера пустой лист")
    def check_response_body_is_empty_list(self):
        assert self.response.json() == []

    @allure.step("ПРоверить, что id объекта соответствует искомому")
    def check_single_object_id(self, id_1):
        assert self.response.json()[0]['id'] == str(id_1)