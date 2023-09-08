from dotenv import load_dotenv
import os
from tasks.task_3.task_3 import ya_authorization

load_dotenv()


class TestCreateDir:
    ya_login = os.getenv('YA_LOGIN')
    ya_password = os.getenv('YA_PASSWORD')

    def test_authorization(self):
        res = ya_authorization(login=TestCreateDir.ya_login, password=TestCreateDir.ya_password)
        expected = 'https://id.yandex.ru/'
        assert res == expected
