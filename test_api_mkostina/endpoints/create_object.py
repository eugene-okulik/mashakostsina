import requests
import allure
from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    @allure.step("Create a new object")
    def create_new_object(self, payload):
        return self._set_response(requests.post(self.url, json=payload))

    @allure.step("Check response's id")
    def check_response_id(self, id):
        assert self.json_response['id'] == id + 1, 'ID is incorrect'
