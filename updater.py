import dataset
import modules
from time import sleep

db = dataset.connect('sqlite:///C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db')
db_name = 'Movies'
table = db[db_name]
lower = 202
upper = len(table) + 45

for x in range(lower, upper):
    print('id is ' + str(x))
    movie_path = table.find_one(id=x)['path']
    movie_name = table.find_one(id=x)['movie_name']
    modules.ForMovies(movie_name, movie_path, table, None).update(x)
    print(movie_name + ' is done')
    sleep(1)
