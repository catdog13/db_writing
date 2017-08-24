import requests


def get_paths():
    path_list = []
    url = 'http://127.0.0.1:8000/movies/paths/'
    json = requests.get(url).json()
    for path in json:
        path_list.append(path['path'])
    return path_list

if __name__ == '__main__':
    print(get_paths())
