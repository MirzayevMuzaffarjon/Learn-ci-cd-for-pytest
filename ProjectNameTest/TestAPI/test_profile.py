import allure, time

@allure.epic("Profile")
@allure.feature("Profile Feature One")
@allure.story("Get Profile Happy Flow")
def test_get_profile_happy_flow(env_data):
    time.sleep(1)
    assert env_data.username_test == "TEST USERNAME"

@allure.epic("Profile")
@allure.feature("Profile Feature One")
@allure.story("Get Profile With Invalid Token")
def test_trying_to_get_profile_with_invalid_token():
    time.sleep(1)
    pass

@allure.epic("Profile")
@allure.feature("Profile Feature Two")
@allure.story("Edit Profile Avatar")
def test_edit_profile_avatar():
    time.sleep(1)
    pass

@allure.epic("Profile")
@allure.feature("Profile Feature Two")
@allure.story("Edit Profile Phone Number")
def test_edit_profile_phone_number():
    time.sleep(1)
    pass

@allure.epic("Profile")
@allure.feature("Profile Feature Two")
@allure.story("Edit Profile Name")
def test_edit_profile_name():
    time.sleep(1)
    pass