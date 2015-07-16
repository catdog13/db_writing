import os
import subprocess
from imdbpie import Imdb


def get_length(filename):
    result = subprocess.Popen(["ffprobe", filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for x in result.stdout.readlines():
        if rb"Duration" in x:
            movie_length = (x[12:23])
            return str(movie_length)[2:-4]


def get_movie_name(filename):
    movie_name = filename[:-4]
    return movie_name


def get_view_status():
    view_status = "Unwatched"
    return view_status


def get_movie_id(filename):
    imdb = Imdb()
    movie = imdb.search_for_title(get_movie_name(filename))
    movie_id = movie[0][str('imdb_id')]
    return movie_id


def get_movie_size(path):
    file_size = os.path.getsize(path)
    file_size_bytes = file_size/1073741824
    return str(round(file_size_bytes, 2)) + ' GB'
