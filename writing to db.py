import os
import dataset
import time
from imdbpie import Imdb
# db = dataset.connect('sqlite:///C:\\Users\Tom\\PycharmProjects\\un-watched_status\\video_list.db')
db = dataset.connect('sqlite:///C:\\Users\Tom\\video_list.db')
imdb = Imdb()


def folder_crawler(path_to_craw, unwatched, drop, add_id):
    start_time = time.time()
    db_name = path_to_craw[3:]
    print(db_name + " Starting")
    if drop:
        db[db_name].drop()
    table = db[db_name]

    def file_writer(dir_path, file_name, status):
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            file_size_bytes = file_size/1073741824
            without_mp4 = file_name[:-4]
            if status:
                view_status = "Unwatched"
            else:
                view_status = ""

            if add_id:
                if table.find_one(filename=file_name) is None:
                    movie = imdb.search_for_title(without_mp4)
                    movie_id = movie[0]['imdb_id']
                    table.insert(dict(filename=file_name, path=dir_path,
                                      file_size=(str(round(file_size_bytes, 2)) + ' GB'), status=view_status,
                                      movie_name=without_mp4, imdb_id=movie_id))
            else:
                if table.find_one(filename=file_name) is None:
                    table.insert(dict(filename=file_name, path=dir_path,
                                      file_size=(str(round(file_size_bytes, 2)) + ' GB'), status=view_status))

    def start_file_op():
            folder = path_to_craw
            folder = folder.replace('/', '\\')
            file_type = '.mp4'
            file_type = file_type.strip(".")
            for dir_path, dir_names, file_names in os.walk(folder):
                for filename in [f for f in file_names if f.endswith("." + file_type)]:
                    file_writer(dir_path, filename, unwatched)
    start_file_op()
    print(db_name + " Was Done In " + str(round((time.time() - start_time), 2)) + " seconds")

folder_crawler(r"E:\Movies", True, False, True)
folder_crawler(r"E:\TV", False, False, False)
