import dataset

dj_db_file = 'C:\\Users\\Tom\\Documents\\Python_Projects\\django_website\\db.sqlite3'
db_file = 'C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db'
db = dataset.connect('sqlite:///{}'.format(dj_db_file))

table = db['movies_moviedb']

dataset.freeze(table, format='csv', filename='db_files\\Movie_list.csv')
dataset.freeze(table, format='json', filename='db_files\\Movie_list.json')
dataset.freeze(table, format='tabson', filename='db_files\\Movie_list.tabson')
