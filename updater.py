import dataset
import modules
from time import sleep

dj_db_file = 'C:\\Users\\Tom\\Documents\\Python_Projects\\django_website\\db.sqlite3'
db_file = 'C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db'
db = dataset.connect('sqlite:///{}'.format(dj_db_file))

table = db['movies_moviedb']

lower = 202
upper = len(table) + 45

for x in range(lower, upper):
    print('id is ' + str(x))
    movie_path = table.find_one(id=x)['path']
    movie_name = table.find_one(id=x)['movie_name']
    modules.ForMovies(movie_name, movie_path, table, None).update(x)
    print(movie_name + ' is done')
    sleep(1)
