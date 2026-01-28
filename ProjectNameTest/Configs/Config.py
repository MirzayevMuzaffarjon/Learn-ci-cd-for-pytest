import os
from dotenv import load_dotenv


class EnvData:
    load_dotenv()
    phone_number = os.getenv("PHONE_NUMBER")
    name = os.getenv("NAME")
    username_test = os.getenv("USERNAME_TEST")
    password = os.getenv("PASSWORD")
    total = os.getenv("TOTAL")