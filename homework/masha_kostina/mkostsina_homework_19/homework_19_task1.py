import requests


def get_all_obj():
    response = requests.get("http://objapi.course.qa-practice.com/object").json()
    assert len(response) == 1, 'There are extra objects'


def get_obj_by_id():
    post_id = 518
    response = requests.get(f"http://objapi.course.qa-practice.com/object/{post_id}").json()
    assert response['id'] == post_id


def create_obj():
    body = {
        "name": "New object",
        "data": {'color': 'pink', 'size': 'medium'}
    }
    response = requests.post("http://objapi.course.qa-practice.com/object", json=body)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == 520, 'ID is incorrect'


def new_obj():
    body = {
        "name": "New object",
        "data": {'color': 'pink', 'size': 'medium'}
    }
    response = requests.post("http://objapi.course.qa-practice.com/object", json=body)
    return response.json()['id']


def put_obj():
    obj_id = new_obj()
    body = {
        "name": "New object UPD",
        "data": {'color': 'red', 'size': 'large'}
    }
    response = requests.put(f"http://objapi.course.qa-practice.com/object/{obj_id}", json=body).json()
    assert response['name'] == "New object UPD"
    assert response['data']['color'] == 'red'
    assert response['data']['size'] == 'large'
    clear(obj_id)


def patch_obj():
    obj_id = new_obj()
    body = {
        "name": "New object",
        "data": {'color': 'red', 'size': 'medium'}
    }
    response = requests.patch(f"http://objapi.course.qa-practice.com/object/{obj_id}", json=body).json()
    assert response['name'] == "New object"
    assert response['data']['color'] == 'red'
    assert response['data']['size'] == 'medium'
    clear(obj_id)


def clear(obj_id):
    requests.delete(f"http://objapi.course.qa-practice.com/object/{obj_id}")


def delete_obj():
    obj_id = new_obj()
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{obj_id}")
    return response.status_code
