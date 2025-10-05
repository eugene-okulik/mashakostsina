import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.step("Update an object")
    def update_put_object(self, payload, obj_id):
        return self._set_response(requests.put(f"{self.url}/{obj_id}", json=payload))

    @allure.step("Patch an object")
    def update_patch_object(self, payload, obj_id):
        return self._set_response(requests.patch(f"{self.url}/{obj_id}", json=payload))

    @allure.step("Check response's id")
    def check_response_id(self, id):
        actual_id = self.json_response['id']
        try:
            actual_id_int = int(actual_id)
        except (TypeError, ValueError):
            assert False, f'ID is not numeric: {actual_id}'
        assert actual_id_int == id, f'ID is incorrect: expected {id}'
