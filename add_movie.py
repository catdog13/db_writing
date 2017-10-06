import requests
import os
import datetime

api_key = '3d56ad21150323764ca7cf7ebcf26ccc'


def add_movie(path):
    creation_time = os.path.getctime(path)
    creation_date = datetime.date.fromtimestamp(creation_time)
    file_size = os.path.getsize(path)
    movie_id = 281778

    post_data = {'api_key': api_key,
                 'path': path,
                 'size': file_size,
                 'age': creation_date,
                 # 'movie_id': movie_id
                 }
    response = requests.post('http://127.0.0.1:8000/movies/add/', data=post_data)
    # response = requests.post('http://catdog13.com/movies/add/', data=post_data)
    content = response.json()
    if content['Added'] == 'True':
        return True
    elif content['Added'] == 'False':
        return False, content['Error']
    else:
        return False

if __name__ == '__main__':
    print(add_movie(r'E:\Movies\Survivor (2014)\Survivor.mp4'))
