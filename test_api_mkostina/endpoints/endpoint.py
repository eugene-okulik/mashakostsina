import requests
import allure


class Endpoint:
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    json_response = None

    @allure.step("Set and parse response")
    def _set_response(self, response):
        self.response = response
        try:
            request = getattr(response, 'request', None)
            if request is not None:
                try:
                    body = request.body.decode() if isinstance(request.body, (bytes, bytearray)) else request.body
                except Exception:
                    body = str(request.body)
                allure.attach(
                    f"{request.method} {request.url}\n\nRequest body:\n{body}",
                    name="Request",
                    attachment_type=allure.attachment_type.TEXT
                )

            allure.attach(
                f"Status code: {response.status_code}\n\nResponse body:\n{response.text}",
                name="Response",
                attachment_type=allure.attachment_type.TEXT
            )
        except Exception:
            pass
        try:
            self.json_response = self.response.json()
        except (requests.exceptions.JSONDecodeError, ValueError):
            self.json_response = None
        return self.json_response

    @allure.step("Check response's status code")
    def check_response_status_code(self):
        assert self.response.status_code == 200, 'Status code is not 200'

    @allure.step("Check response's name")
    def check_response_name(self, name):
        assert self.json_response is not None, 'Response JSON is empty'
        assert self.json_response['name'] == name, 'Name is incorrect'

    @allure.step("Check response's data")
    def check_response_data(self, data):
        assert self.json_response is not None, 'Response JSON is empty'
        assert self.json_response['data'] == data, 'Data is incorrect'

    @allure.step("Check response color")
    def check_response_color(self, color):
        assert self.json_response['data']['color'] == color, 'Color is incorrect'

    @allure.step("Check response size")
    def check_response_size(self, size):
        assert self.json_response['data']['size'] == size, 'Size is incorrect'

    @allure.step("Check bad request (400)")
    def check_bad_request(self):
        assert self.response.status_code == 400, 'Expected 400 Bad Request'

    @allure.step("Check not found (404)")
    def check_not_found(self):
        assert self.response.status_code == 404, 'Expected 404 Not Found'
