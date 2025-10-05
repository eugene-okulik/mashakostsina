import pytest
import requests
import json
import allure
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject


@pytest.fixture(scope="session", autouse=True)
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def new_obj_id():
    body = {"name": "New object", "data": {'color': 'pink', 'size': 'medium'}}
    response = requests.post("http://objapi.course.qa-practice.com/object", json=body)
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f"http://objapi.course.qa-practice.com/object/{obj_id}")


@pytest.fixture(scope="session", autouse=True)
def update_put_object_endpoint():
    return UpdateObject()


@pytest.fixture(scope="session", autouse=True)
def update_patch_object_endpoint():
    return UpdateObject()


@pytest.fixture(scope="session", autouse=True)
def get_object_endpoint():
    return GetObject()


@pytest.fixture(scope="session", autouse=True)
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
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
