import dataset
from modules import *
db = dataset.connect('sqlite:///C:\\Users\Tom\\PycharmProjects\\db_writing\\db_files\\video_list.db')
table = db['Movie_Testing']


def run_update(row_id):
    update(table, row_id)

run_update('6')
