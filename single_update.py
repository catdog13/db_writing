import dataset
from modules import *

db = dataset.connect('sqlite:///C:\\Users\Tom\\video_list.db')
table = db['Movies']


def run_update(row_id):
    update(table, row_id)


run_update('id_number')
