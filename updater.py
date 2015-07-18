import dataset
from modules import *
db = dataset.connect('sqlite:///C:\\Users\Tom\\PycharmProjects\\db_writing\\db_files\\video_list.db')
db_name = 'Movies'
table = db[db_name]

for x in range(351, 370):
    update(table, x)
