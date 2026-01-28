import allure, time

@allure.epic("Product List API")
@allure.feature("Get Product List")
@allure.story("Get Product List Without Params")
def test_get_product_list_without_params(env_data):
    time.sleep(1)
    assert env_data.total == '15000'

@allure.epic("Product List API")
@allure.feature("Get Product List")
@allure.story("Get Product List With Params")
def test_get_product_list_with_params(env_data):
    time.sleep(1)
    assert env_data.total == '15000'

@allure.epic("Product List API")
@allure.feature("Get Product List")
@allure.story("Get Product List With Json Body")
def test_get_product_list_with_json_body(env_data):
    time.sleep(1)
    pass
