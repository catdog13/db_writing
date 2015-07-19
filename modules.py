import os
import requests


def get_movie_name(path):
    part_1 = path.split('\\')
    part_2 = part_1[3][:-4]
    movie_name = part_2.split('(')
    return movie_name[0]


def get_view_status(status):
    if status:
        view_status = 'Unwatched'
    else:
        view_status = 'Watched'
    return view_status


def get_movie_size(path):
    file_size = os.path.getsize(path)
    file_size_bytes = file_size/1073741824
    return str(round(file_size_bytes, 2)) + ' GB'


def get_movie_year(path):
    part_1 = path.split('(')
    movie_year = part_1[1].split(')')
    return movie_year[0]


def get_json(movie_name, year):
    movie_name = movie_name.replace('&', '%26')
    json_file = requests.get('http://www.omdbapi.com/?t=' + movie_name + '&y=' + year + '&plot=short&r=json')
    return json_file.json()


def get_runtime(json_file):
    runtime = json_file['Runtime']
    return runtime


def get_movie_id(json_file):
    movie_id = json_file['imdbID']
    return movie_id


def get_movie_imdb_rating(json_file):
    rating = json_file['imdbRating']
    movie_rating = rating + "/10"
    return movie_rating


def get_movie_genre(json_file):
    movie_genre = json_file['Genre']
    return movie_genre


def get_movie_mpaa_rating(json_file):
    movie_mpaa_rating = json_file['Rated']
    return movie_mpaa_rating


def get_movie_release_date(json_file):
    movie_release_date = json_file['Released']
    return movie_release_date


def get_movie_plot(json_file):
    movie_plot = json_file['Plot']
    return movie_plot


def writer(file_name, movie_path, table):
    if table.find_one(path=movie_path) is None:
        movie_name = file_name[:-4]
        json_file = get_json(movie_name, get_movie_year(movie_path))
        data = dict(imdb_id=get_movie_id(json_file),
                    file_size=get_movie_size(movie_path),
                    runtime=get_runtime(json_file),
                    imdb_rating=get_movie_imdb_rating(json_file),
                    genre=get_movie_genre(json_file),
                    mpaa_rating=get_movie_mpaa_rating(json_file),
                    release_date=get_movie_release_date(json_file),
                    plot=get_movie_plot(json_file),
                    movie_name=movie_name,
                    status=get_view_status(True),
                    path=movie_path,
                    )
        table.insert(data)


def update(table, x):
    movie_path = table.find_one(id=x)['path']
    movie_name = table.find_one(id=x)['movie_name']
    json_file = get_json(movie_name, get_movie_year(movie_path))
    data = dict(id=x, imdb_id=get_movie_id(json_file),
                file_size=get_movie_size(movie_path),
                runtime=get_runtime(json_file),
                imdb_rating=get_movie_imdb_rating(json_file),
                genre=get_movie_genre(json_file),
                mpaa_rating=get_movie_mpaa_rating(json_file),
                release_date=get_movie_release_date(json_file),
                plot=get_movie_plot(json_file)
                )
    table.update(data, ['id'])
