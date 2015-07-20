import dataset

db = dataset.connect('sqlite:///db_files\\video_list.db')
table = db['Movies']

dataset.freeze(table, format='csv', filename='db_files\\Movie_list.csv')
dataset.freeze(table, format='json', filename='db_files\\Movie_list.json')
dataset.freeze(table, format='tabson', filename='db_files\\Movie_list.tabson')