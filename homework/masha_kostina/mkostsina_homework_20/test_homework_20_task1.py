import pytest
import requests
import allure


@allure.feature("Objects")
@allure.story("Get objects")
@allure.tag("smoke")
@allure.title("Получение всех объектов")
@allure.testcase("https://google.com/", "Test case 1")
@allure.issue("https://google.com/", "Bug 003")
@pytest.mark.medium
def test_get_all_obj(attach_response):
    with allure.step("Run get request for all objects"):
        response = requests.get("http://objapi.course.qa-practice.com/object")
        attach_response(response, name="Get all objects")
        data = response.json()

    with allure.step("Check number of objects"):
        assert len(data) == 2, 'There are extra objects'


@allure.feature("Objects")
@allure.story("Get objects")
@allure.tag("smoke")
@allure.title("Получение объекта по id")
@pytest.mark.critical
def test_get_obj_by_id(new_obj_id, attach_response):
    with allure.step(f'Run request for object by id - {new_obj_id}'):
        response = attach_response(
            requests.get(f"http://objapi.course.qa-practice.com/object/{new_obj_id}"),
            name="Get object by id"
        )
    with allure.step(f'Check response id with {new_obj_id}'):
        assert response['id'] == new_obj_id


@allure.feature("Objects")
@allure.story("Create objects")
@allure.tag("smoke")
@allure.title("Создание объекта")
@pytest.mark.parametrize('body', [
    {"name": "New object1", "data": {'color': 'pink', 'size': 'large'}},
    {"name": "New object2", "data": {'color': 'pink', 'size': 'small'}},
    {"name": "New object3", "data": {'color': 'red', 'size': 'medium'}}
])
def test_create_obj(body, new_obj_id, attach_response):
    with allure.step("Create an object"):
        response = attach_response(
            requests.post("http://objapi.course.qa-practice.com/object", json=body),
            name="Create object"
        )
    with allure.step("Check response's status code"):
        assert requests.post("http://objapi.course.qa-practice.com/object", json=body).status_code == 200, \
            'Status code is incorrect'
    with allure.step("Check id in response"):
        assert response['id'] == new_obj_id + 1, 'ID is incorrect'


@allure.feature("Test")
@allure.story("Update objects")
@allure.title("Обновление объекта put")
def test_put_obj(new_obj_id, attach_response):
    body = {
        "name": "New object UPD",
        "data": {'color': 'red', 'size': 'large'}
    }
    with allure.step(f'Update an object by a {body}'):
        response = attach_response(
            requests.put(f"http://objapi.course.qa-practice.com/object/{new_obj_id}", json=body),
            name="Update object PUT"
        )
    with allure.step("Check name in response"):
        assert response['name'] == "New object UPD"
    with allure.step("Check color in response"):
        assert response['data']['color'] == 'red'
    with allure.step("Check size in response"):
        assert response['data']['size'] == 'large'


@allure.feature("Test")
@allure.story("Update objects")
@allure.title("Обновление объекта patch")
def test_patch_obj(new_obj_id, attach_response):
    body = {
        "name": "New object",
        "data": {'color': 'red', 'size': 'medium'}
    }
    with allure.step(f'Update an object by a {body}'):
        response = attach_response(
            requests.patch(f"http://objapi.course.qa-practice.com/object/{new_obj_id}", json=body),
            name="Update object PATCH"
        )
    with allure.step("Check name in response"):
        assert response['name'] == "New object"
    with allure.step("Check color in response"):
        assert response['data']['color'] == 'red'
    with allure.step("Check size in response"):
        assert response['data']['size'] == 'medium'


@allure.feature("Test2")
@allure.story("Delete objects")
@allure.title("Удаление объекта")
def test_delete_obj(new_obj_id, attach_response):
    with allure.step(f'Run request to delete the object with id {new_obj_id}'):
        delete_response = requests.delete(f"http://objapi.course.qa-practice.com/object/{new_obj_id}")
        attach_response(delete_response, name="Delete object")
    with allure.step("Check response's status code"):
        assert delete_response.status_code == 200

    with allure.step(f'Run request to get the object with id {new_obj_id} after deleting'):
        get_response = requests.get(f"http://objapi.course.qa-practice.com/object/{new_obj_id}")
        attach_response(get_response, name="Get deleted object")
    with allure.step("Check response's status code"):
        assert get_response.status_code == 404
