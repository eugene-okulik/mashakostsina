import pytest
import allure


NEGATIVE_DATA = [
    {"name": ["New object1"], "data": {'color': 'pink', 'size': 'large'}},
    {"name": {"New object2": ''}, "data": {'color': 'pink', 'size': 'small'}}
]


@allure.epic("Objects API")
@allure.feature("Objects")
@allure.story("Create")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("api", "smoke")
@allure.title("Создание объекта (позитив)")
@pytest.mark.parametrize('body', [
    {"name": "New object1", "data": {'color': 'pink', 'size': 'large'}},
    {"name": "New object2", "data": {'color': 'pink', 'size': 'small'}},
    {"name": "New object3", "data": {'color': 'red', 'size': 'medium'}}
])
def test_create_obj(body, create_object_endpoint, new_obj_id):
    create_object_endpoint.create_new_object(payload=body)
    create_object_endpoint.check_response_status_code()
    create_object_endpoint.check_response_id(new_obj_id)
    create_object_endpoint.check_response_name(body['name'])
    create_object_endpoint.check_response_data(body['data'])


@allure.epic("Objects API")
@allure.feature("Objects")
@allure.story("Create")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("api", "negative")
@allure.title("Создание объекта (негатив)")
@pytest.mark.parametrize('body', NEGATIVE_DATA)
def test_object_with_negative_data(body, create_object_endpoint):
    create_object_endpoint.create_new_object(body)
    create_object_endpoint.check_bad_request()


@allure.epic("Objects API")
@allure.feature("Objects")
@allure.story("Update")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("api", "update", "put", "positive")
@allure.title("Обновление объекта put")
def test_put_obj(new_obj_id, update_put_object_endpoint):
    body = {
        "name": "New object UPD",
        "data": {'color': 'red', 'size': 'large'}
    }
    update_put_object_endpoint.update_put_object(payload=body, obj_id=new_obj_id)
    update_put_object_endpoint.check_response_status_code()
    update_put_object_endpoint.check_response_id(new_obj_id)
    update_put_object_endpoint.check_response_name(body['name'])
    update_put_object_endpoint.check_response_color(body['data']['color'])
    update_put_object_endpoint.check_response_size(body['data']['size'])


@allure.epic("Objects API")
@allure.feature("Objects")
@allure.story("Update")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("api", "update", "put", "negative")
@allure.title("Обновление объекта put, негативный кейс")
def test_put_obj_with_negative_data(new_obj_id, update_put_object_endpoint):
    body = {
        "name": ["New object UPD"],
        "data": {'color': 'red', 'size': 'large'}
    }
    update_put_object_endpoint.update_put_object(payload=body, obj_id=new_obj_id)
    update_put_object_endpoint.check_bad_request()


@allure.epic("Objects API")
@allure.feature("Objects")
@allure.story("Update")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("api", "update", "patch", "positive")
@allure.title("Обновление объекта patch")
def test_patch_obj(new_obj_id, update_patch_object_endpoint):
    body = {
        "name": "New object PATCH",
        "data": {'color': 'green', 'size': 'small'}
    }
    update_patch_object_endpoint.update_patch_object(payload=body, obj_id=new_obj_id)
    update_patch_object_endpoint.check_response_status_code()
    update_patch_object_endpoint.check_response_id(new_obj_id)
    update_patch_object_endpoint.check_response_name(body['name'])
    update_patch_object_endpoint.check_response_color(body['data']['color'])
    update_patch_object_endpoint.check_response_size(body['data']['size'])


@allure.epic("Objects API")
@allure.feature("Objects")
@allure.story("Update")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("api", "update", "patch", "negative")
@allure.title("Обновление объекта patch, негативный кейс")
def test_patch_obj_with_negative_data(new_obj_id, update_patch_object_endpoint):
    body = {
        "name": ["New object PATCH"],
        "data": {'color': 'green', 'size': 'small'}
    }
    update_patch_object_endpoint.update_patch_object(payload=body, obj_id=new_obj_id)
    update_patch_object_endpoint.check_bad_request()


@allure.epic("Objects API")
@allure.feature("Objects")
@allure.story("Get")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("api", "smoke", "read")
@allure.title("Получение всех объектов")
def test_get_all_obj(get_object_endpoint):
    get_object_endpoint.get_all_object()
    get_object_endpoint.check_response_status_code()
    get_object_endpoint.check_len_of_response()


@allure.epic("Objects API")
@allure.feature("Objects")
@allure.story("Get")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("api", "read")
@allure.title("Получение объекта по id")
def test_get_obj_by_id(new_obj_id, get_object_endpoint):
    get_object_endpoint.get_object_by_id(new_obj_id)
    get_object_endpoint.check_response_status_code()
    get_object_endpoint.check_response_id(new_obj_id)


@allure.epic("Objects API")
@allure.feature("Objects")
@allure.story("Delete")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("api", "delete")
@allure.title("Удаление объекта")
def test_delete_obj(new_obj_id, delete_object_endpoint, get_object_endpoint):
    delete_object_endpoint.delete_object(new_obj_id)
    delete_object_endpoint.check_response_status_code()
    get_object_endpoint.get_object_by_id(new_obj_id)
    get_object_endpoint.check_not_found()
