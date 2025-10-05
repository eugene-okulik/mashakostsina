import requests
import allure
from endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step("Get all objects")
    def get_all_object(self):
        return self._set_response(requests.get(self.url))

    @allure.step("Get object by ID")
    def get_object_by_id(self, obj_id):
        return self._set_response(requests.get(f'{self.url}/{obj_id}'))

    @allure.step("Check len of response")
    def check_len_of_response(self):
        assert len(self.json_response) == 1, 'There are extra objects'

    @allure.step("Check response's id")
    def check_response_id(self, id):
        assert self.json_response['id'] == id, 'ID is incorrect'
