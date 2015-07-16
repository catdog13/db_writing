import dataset
from modules import *
db = dataset.connect('sqlite:///C:\\Users\Tom\\PycharmProjects\\db_writing\\db_files\\video_list.db')
db_name = 'Movies'
table = db[db_name]

for x in range(1, 2):
    movie_path = table.find_one(id=x)['path']
    data = dict(id=x, file_size=get_movie_size(movie_path))
    table.update(data, ['id'])
