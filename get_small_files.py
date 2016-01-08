import dataset


db = dataset.connect('sqlite:///C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db')
table = db['Movies']
db_mem = dataset.connect('sqlite:///:memory:')
small_files_list = db_mem['list']


for movie in table:
    if float(movie['file_size'][:-3]) < 3:
        small_files_list.insert(dict(file_name=movie['movie_name'], file_size=movie['file_size']))

result = small_files_list.all()
dataset.freeze(result, format='csv', filename='db_files\\small_movies.csv')
# dataset.freeze(result, format='json', filename='db_files\\small_movies.json')
# dataset.freeze(result, format='tabson', filename='db_files\\small_movies.tabson')
