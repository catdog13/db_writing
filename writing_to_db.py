import os
import subprocess
import dataset
import time
from imdbpie import Imdb
db = dataset.connect('sqlite:///C:\\Users\Tom\\PycharmProjects\\db_writing\\video_list.db')
# db = dataset.connect('sqlite:///C:\\Users\Tom\\video_list.db')
imdb = Imdb()


def folder_crawler(path_to_craw):
    start_time = time.time()
    db_name = path_to_craw[3:]
    print(db_name + " Starting")
    table = db[db_name]

    def get_length(filename):
        result = subprocess.Popen(["ffprobe", filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for x in result.stdout.readlines():
            if rb"Duration" in x:
                movie_length = (x[12:23])
                return str(movie_length)[2:-4]

    def file_writer(dir_path, file_name):
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            file_size_bytes = file_size/1073741824
            without_mp4 = file_name[:-4]
            view_status = "Unwatched"

            if table.find_one(movie_name=without_mp4) is None:
                movie = imdb.search_for_title(without_mp4)
                movie_id = movie[0]['imdb_id']
                table.insert(dict(movie_name=without_mp4,
                                  status=view_status,
                                  imdb_id=movie_id,
                                  length=get_length(file_path),
                                  file_size=(str(round(file_size_bytes, 2)) + ' GB'),
                                  path=file_path))

    def start_file_op():
            folder = path_to_craw
            folder = folder.replace('/', '\\')
            file_type = '.mp4'
            file_type = file_type.strip(".")
            for dir_path, dir_names, file_names in os.walk(folder):
                for filename in [f for f in file_names if f.endswith("." + file_type)]:
                    file_writer(dir_path, filename)
    start_file_op()
    print(db_name + " Was Done In " + str(round((time.time() - start_time), 2)) + " seconds")

folder_crawler(r"E:\Movies")
