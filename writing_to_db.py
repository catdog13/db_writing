import os
import dataset
import time
from modules import writer
db = dataset.connect('sqlite:///db_files\\video_list.db')


def folder_crawler(path_to_craw):
    start_time = time.time()
    db_name = path_to_craw[3:]
    print(db_name + " Starting")
    table = db[db_name]

    def file_walker():
        for dir_path, dir_names, file_names in os.walk(path_to_craw):
            for filename in [f for f in file_names if f.endswith('.mp4')]:
                file_path = os.path.join(dir_path, filename)
                writer(filename, file_path, table)

    file_walker()
    print(db_name + " Was Done In " + str(round((time.time() - start_time), 2)) + " seconds")


folder_crawler(r"E:\Movies")
