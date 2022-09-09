from pprint import pprint

import requests

import os

class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self,file_path:str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        path_to_file_disk = os.path.basename(file_path)
        params = {"path": path_to_file_disk, "overwrite": "true"}
        response_1 = requests.get(upload_url, headers=headers, params=params)
        print(type(response_1))
        pprint(response_1.json())

        href = response_1.json().get('href','')
        print(href)

        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
             print("Success")

if __name__ == '__main__':
    token = ''
    path_to_file = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

