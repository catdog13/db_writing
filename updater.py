import dataset
import modules

db = dataset.connect('sqlite:///C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db')
db_name = 'Movies'
table = db[db_name]
lower = 1
upper = len(table) + 1

for x in range(lower, upper):
    movie_path = table.find_one(id=x)['path']
    movie_name = table.find_one(id=x)['movie_name']
    modules.ForMovies(movie_name, movie_path, table).update(x)
