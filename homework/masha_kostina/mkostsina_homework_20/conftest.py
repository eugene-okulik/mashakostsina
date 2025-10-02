import pytest
import requests
import allure
import json


@pytest.fixture(scope="session", autouse=True)
def start_and_finish():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture(autouse=True)
def before_after_each_test():
    print("before test")
    yield
    print("after test")


@pytest.fixture()
def new_obj_id():
    body = {"name": "New object", "data": {'color': 'pink', 'size': 'medium'}}
    response = requests.post("http://objapi.course.qa-practice.com/object", json=body)
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f"http://objapi.course.qa-practice.com/object/{obj_id}")


@pytest.fixture
def attach_response():
    def attach(response, name="Request/Response"):
        allure.attach(
            f"{response.request.method} {response.request.url}\n\n"
            f"Request body:\n{response.request.body}",
            name=f"{name} - Request",
            attachment_type=allure.attachment_type.JSON
        )

        allure.attach(
            f"Status code: {response.status_code}\n\nResponse body:\n{response.text}",
            name=f"{name} - Response",
            attachment_type=allure.attachment_type.JSON
        )

        try:
            return response.json()
        except (json.JSONDecodeError, ValueError):
            return response.text
    return attach


def pytest_configure(config):
    config.addinivalue_line("markers", "medium: marks tests as medium priority")
    config.addinivalue_line("markers", "critical: marks tests as critical priority")
