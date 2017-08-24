import os
import time
import requests
import datetime

api_key = '3d56ad21150323764ca7cf7ebcf26ccc'


def folder_crawler(path_to_craw):
    start_time = time.time()
    db_name = path_to_craw[3:]
    print(db_name + ' Starting')

    def add_movie(path):
        creation_time = os.path.getctime(path)
        creation_date = datetime.date.fromtimestamp(creation_time)
        file_size = os.path.getsize(path)

        post_data = {'api_key': api_key,
                     'path': path,
                     'size': file_size,
                     'age': creation_date}
        response = requests.post('http://127.0.0.1:8000/movies/add/', data=post_data)
        content = response.json()
        if content['Added'] == 'True':
            return True
        elif content['Added'] == 'False':
            return False, content['Error']
        else:
            return False

    def get_paths():
        path_list = []
        url = 'http://127.0.0.1:8000/movies/paths/'
        json = requests.get(url).json()
        for path in json:
            path_list.append(path['path'])
        return path_list

    def file_walker():
            path_list = get_paths()
            for root, subdir, files in os.walk(path_to_craw):
                for file in files:
                    if file.endswith('.mp4'):
                        full_path = os.path.join(root, file)
                        if full_path not in path_list:
                            print('starting ' + full_path)
                            print(add_movie(full_path))
                            time.sleep(7)

    file_walker()
    end_time = str(round((time.time() - start_time), 2))
    print('{0} Was done in {1} seconds'.format(db_name, end_time))


if __name__ == '__main__':
    folder_crawler(r'E:\Movies')
    # folder_crawler(r'D:\TV')
