from endpoints.endpoints import Endpoints
from payloads.payloads import Payloads


class BaseMethods:
    endpoints = Endpoints()
    payloads = Payloads()
    response = None

    def check_response_is_200(self):
        assert self.response.status_code == 200, self.response.json()
        return True

    def check_response_is_404(self):
        assert self.response.status_code == 404, self.response.json()

    def check_name(self):
        assert self.response.json()["name"] == self.payloads.new_object["name"]
        return True

    def check_response_body_is_not_empty(self):
        assert self.response.json() is not None

    def check_object_id(self, id_1, id_2):
        assert self.response.json()[0]['id'] == str(id_1)
        assert self.response.json()[1]['id'] == str(id_2)
