import pytest
from ProjectNameTest.Configs.Config import EnvData

@pytest.fixture(scope="session")
def env_data():
    return EnvData()
