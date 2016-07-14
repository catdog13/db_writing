import dataset
import modules

dj_db_file = 'C:\\Users\\Tom\\Documents\\Python_Projects\\django_website\\db.sqlite3'
db_file = 'C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db'
db = dataset.connect('sqlite:///{}'.format(dj_db_file))

table = db['movies_moviedb']


def run_update(row_id):
    movie_path = table.find_one(id=row_id)['movie_path']
    movie_name = table.find_one(id=row_id)['movie_name']
    modules.ForMovies(movie_name, movie_path, table, None).update(row_id)


run_update('id_number')
