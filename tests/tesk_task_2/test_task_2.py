import pytest
from dotenv import load_dotenv
from tasks.task_2.YaDiskClass import YaApiHandler
import os

load_dotenv()


class TestCreateDir:
    ya_api_token = os.getenv('YA_API_TOKEN')

    def test_create_dir(self):
        test_user = YaApiHandler(TestCreateDir.ya_api_token)
        res = test_user.create_dir('new_folder2')
        # 409 - код того что папка уже существует, 200, 201 - два успеха
        assert res.status_code in (201, 200, 409)

    def test_error_400(self):
        test_user = YaApiHandler(TestCreateDir.ya_api_token)
        res = test_user.create_dir({'a': 1})
        assert res.status_code == 400

    def test_error_401(self):
        test_user = YaApiHandler('error')
        res = test_user.create_dir('folder')
        assert res.status_code == 401
