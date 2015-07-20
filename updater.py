import dataset
from modules import *

db = dataset.connect('sqlite:///db_files\\video_list.db')
db_name = 'Movies'
table = db[db_name]

for x in range(1, 2):
    update(table, x)
