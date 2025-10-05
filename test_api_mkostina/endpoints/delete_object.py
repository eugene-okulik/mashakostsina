import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step("Delete an object")
    def delete_object(self, obj_id):
        return self._set_response(requests.delete(f"{self.url}/{obj_id}"))
