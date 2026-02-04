import allure, time, logging

@allure.epic("Authorization")
@allure.feature("Login")
@allure.story("Login Happy Flow")
def test_login_happy_flow(env_data):
    time.sleep(2)
    logging.info("Login Happy Flow info logging")
    assert env_data.phone_number == "998995556677"

@allure.epic("Authorization")
@allure.feature("Login")
@allure.story("Login With Not Exist Email")
def test_trying_to_login_with_not_exist_email(env_data):
    logging.info("Logging Info login with not exist email")
    time.sleep(1)
    assert env_data.name == "TEST_NAMEE"

@allure.epic("Authorization")
@allure.feature("Login")
@allure.story("Login With Invalid Email")
def test_trying_to_login_with_invalid_email():
    time.sleep(1)
    pass

@allure.epic("Authorization")
@allure.feature("Login")
@allure.story("Login Incorrect Password")
def test_trying_to_login_with_incorrect_password():
    time.sleep(1)
    pass

@allure.epic("Authorization")
@allure.feature("Registration")
@allure.story("Registration Happy Flow")
def test_registration_happy_flow():
    time.sleep(1)
    pass

@allure.epic("Authorization")
@allure.feature("Registration")
@allure.story("Registration With Exist Email")
def test_registration_with_exist_email():
    time.sleep(1)
    pass

@allure.epic("Authorization")
@allure.feature("Registration")
@allure.story("Registration With Invalid Email")
def test_registration_with_invalid_email():
    time.sleep(1)
    pass