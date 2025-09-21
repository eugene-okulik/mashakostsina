import pytest
import requests


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
    return obj_id


@pytest.mark.medium
def test_get_all_obj():
    response = requests.get("http://objapi.course.qa-practice.com/object").json()
    assert len(response) == 1, 'There are extra objects'


@pytest.mark.critical
def test_get_obj_by_id(new_obj_id):
    response = requests.get(f"http://objapi.course.qa-practice.com/object/{new_obj_id}").json()
    assert response['id'] == new_obj_id


@pytest.mark.parametrize('body', [{"name": "New object1", "data": {'color': 'pink', 'size': 'large'}},
                                  {"name": "New object2", "data": {'color': 'pink', 'size': 'small'}},
                                  {"name": "New object3", "data": {'color': 'red', 'size': 'medium'}}])
def test_create_obj(body, new_obj_id):
    response = requests.post("http://objapi.course.qa-practice.com/object", json=body)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == new_obj_id + 1, 'ID is incorrect'


def test_put_obj(new_obj_id):
    body = {
        "name": "New object UPD",
        "data": {'color': 'red', 'size': 'large'}
    }
    response = requests.put(f"http://objapi.course.qa-practice.com/object/{new_obj_id}", json=body).json()
    assert response['name'] == "New object UPD"
    assert response['data']['color'] == 'red'
    assert response['data']['size'] == 'large'


def test_patch_obj(new_obj_id):
    body = {
        "name": "New object",
        "data": {'color': 'red', 'size': 'medium'}
    }
    response = requests.patch(f"http://objapi.course.qa-practice.com/object/{new_obj_id}", json=body).json()
    assert response['name'] == "New object"
    assert response['data']['color'] == 'red'
    assert response['data']['size'] == 'medium'


def test_delete_obj():
    body = {"name": "Object to delete", "data": {'color': 'yellow', 'size': 'medium'}}
    response = requests.post("http://objapi.course.qa-practice.com/object", json=body)
    assert response.status_code == 200
    obj_id = response.json()['id']

    delete_response = requests.delete(f"http://objapi.course.qa-practice.com/object/{obj_id}")
    assert delete_response.status_code == 200

    get_response = requests.get(f"http://objapi.course.qa-practice.com/object/{obj_id}")
    assert get_response.status_code == 404
