import dataset

dj_db_file = 'C:\\Users\\Tom\\Documents\\Python_Projects\\django_website\\db.sqlite3'
db_file = 'C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db'
db = dataset.connect('sqlite:///{}'.format(dj_db_file))

table = db['movies_moviedb']

db_mem = dataset.connect('sqlite:///:memory:')
small_files_list = db_mem['list']

for movie in table:
    if float(movie['file_size'][:-3]) < 3:
        small_files_list.insert(dict(file_name=movie['movie_name'], file_size=movie['file_size']))

result = small_files_list.all()
dataset.freeze(result, format='csv', filename='db_files\\small_movies.csv')
# dataset.freeze(result, format='json', filename='db_files\\small_movies.json')
# dataset.freeze(result, format='tabson', filename='db_files\\small_movies.tabson')
