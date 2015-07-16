import dataset
import time
from modules import *
# db = dataset.connect('sqlite:///C:\\Users\Tom\\PycharmProjects\\db_writing\\video_list.db')
db = dataset.connect('sqlite:///C:\\Users\Tom\\video_list.db')


def folder_crawler(path_to_craw):
    start_time = time.time()
    db_name = path_to_craw[3:]
    print(db_name + " Starting")
    table = db[db_name]

    def file_writer(dir_path, file_name):
        file_path = os.path.join(dir_path, file_name)
        if table.find_one(movie_name=get_movie_name(file_name)) is None:
            table.insert(dict(movie_name=get_movie_name(file_name),
                              status=get_view_status(),
                              imdb_id=get_movie_id(file_name),
                              length=get_length(file_path),
                              file_size=get_movie_size(file_path),
                              path=file_path))

    def start_file_op():
            for dir_path, dir_names, file_names in os.walk(path_to_craw):
                for filename in [f for f in file_names if f.endswith('.mp4')]:
                    file_writer(dir_path, filename)
    start_file_op()
    print(db_name + " Was Done In " + str(round((time.time() - start_time), 2)) + " seconds")

folder_crawler(r"E:\Movies")
