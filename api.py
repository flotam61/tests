import requests

yatoken = ''
URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {yatoken}'}

def create_folder(path):
    res = requests.put(f'{URL}?path={path}', headers=headers)
    if res.status_code == 201:
        print(f'Все успешно, код {res.status_code}')
    else:
        print(f'Произошла ошибка, код {res.status_code}')
    return res.status_code

create_folder('test')