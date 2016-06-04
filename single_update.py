import dataset
import modules

db = dataset.connect('sqlite:///C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db')
table = db['Movies']


def run_update(row_id):
    movie_path = table.find_one(id=row_id)['path']
    movie_name = table.find_one(id=row_id)['movie_name']
    modules.ForMovies(movie_name, movie_path, table, None).update(row_id)


run_update('id_number')
