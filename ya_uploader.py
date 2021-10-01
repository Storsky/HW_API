import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str):
        file_to = file_path.split('/')
        get_url = self._get_upload_link(disk_file_path=file_to[-1])
        url_ = get_url.get('href', '')
        response = requests.put(url_, data=open(file_path, 'rb'))
        if response.status_code == 201:
            print("Success")



if __name__ == '__main__':
    path_to_file = ''
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)