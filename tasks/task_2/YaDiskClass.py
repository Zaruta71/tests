import requests


class YaApiHandler:
    base_url = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_dir(self, dir_name='new_folder'):
        method_name = f'{self.base_url}v1/disk/resources'
        headers = self.get_headers()
        params = {'path': f'/{dir_name}'}
        response = requests.put(method_name, headers=headers, params=params)

        return response
