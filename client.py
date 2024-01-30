import requests
import json

server = 'http://localhost:6000'


def upload_data(name, age):
    url = server + '/api/upload'
    data = {'name': name, 'age': age}
    headers = {'Content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200 and response.json()['status'] == 'Success':
        print('Data upload successful')
    else:
        print('Data upload failed')


def download_data(index):
    url = server + f'/api/download/{index}'

    response = requests.get(url)

    if response.status_code == 200:
        print(response.json())
    else:
        print('Data download failed')


if __name__ == '__main__':
    upload_data('John', 30)
    upload_data('Jane', 25)
    download_data(0)
    download_data(1)
