import os
import requests
from urllib.parse import quote_plus


class ForMovies:
    def __init__(self, movie_name, movie_path, table, path_table):
        self.movie_name = movie_name
        self.movie_path = movie_path
        self.table = table
        self.path_table = path_table
    json_file = {}
    status = True

    def get_view_status(self):
        if self.status:
            view_status = 'Unwatched'
        else:
            view_status = 'Watched'
        return view_status

    def get_movie_size(self):
        file_size = os.path.getsize(self.movie_path)
        file_size_bytes = file_size / 1073741824
        return str(round(file_size_bytes, 2)) + ' GB'

    def get_movie_year(self):
        part_1 = self.movie_path.split('(')
        movie_year = part_1[1].split(')')
        return movie_year[0]

    def get_json(self):
        movie_name = quote_plus(self.movie_name)
        url = 'http://www.omdbapi.com/?t={0}&y={1}&plot=short&r=json&tomatoes=true'\
            .format(movie_name, self.get_movie_year())
        # print(url)
        json_file = requests.get(url)
        self.json_file = json_file.json()
        return json_file.json()

    def get_runtime(self):
        runtime = self.json_file['Runtime']
        return runtime

    def get_movie_id(self):
        movie_id = self.json_file['imdbID']
        return movie_id

    def get_movie_imdb_rating(self):
        rating = self.json_file['imdbRating']
        movie_rating = rating + "/10"
        return movie_rating

    def get_movie_genre(self):
        movie_genre = self.json_file['Genre']
        return movie_genre

    def get_movie_mpaa_rating(self):
        movie_mpaa_rating = self.json_file['Rated']
        return movie_mpaa_rating

    def get_movie_release_date(self):
        movie_release = self.json_file['Released']
        release_year = movie_release[-4:]
        release_month = movie_release[3:][:4]
        movie_release_date = release_year + ' ' + release_month
        return movie_release_date

    def get_movie_plot(self):
        movie_plot = self.json_file['Plot']
        return movie_plot

    def get_actors(self):
        actors = self.json_file['Actors']
        return actors

    def get_tomato_rating(self):
        rating = self.json_file['tomatoMeter']
        if rating == 'N/A':
            format_rating = 'N/A'
        else:
            format_rating = ("{0:0=3d}".format(int(rating)))
        return format_rating

    def get_response(self):
        response = self.json_file['Response']
        return response

    def get_length(self):
        length = len(self.table) + 1
        return length

    def update(self, x):
        self.get_json()
        data = dict(id=x,
                    imdb_id=self.get_movie_id(),
                    file_size=self.get_movie_size(),
                    runtime=self.get_runtime(),
                    imdb_rating=self.get_movie_imdb_rating(),
                    genre=self.get_movie_genre(),
                    mpaa_rating=self.get_movie_mpaa_rating(),
                    release_date=self.get_movie_release_date(),
                    plot=self.get_movie_plot(),
                    actors=self.get_actors(),
                    tomato_rating=self.get_tomato_rating()
                    )
        self.table.update(data, ['id'])

    def writer(self):
        if self.movie_path not in self.path_table:
            self.get_json()
            if self.get_response() == 'True':
                data = dict(id=self.get_length(),
                            imdb_id=self.get_movie_id(),
                            file_size=self.get_movie_size(),
                            runtime=self.get_runtime(),
                            imdb_rating=self.get_movie_imdb_rating(),
                            genre=self.get_movie_genre(),
                            mpaa_rating=self.get_movie_mpaa_rating(),
                            release_date=self.get_movie_release_date(),
                            plot=self.get_movie_plot(),
                            movie_name=self.movie_name,
                            status=self.get_view_status(),
                            path=self.movie_path,
                            actors=self.get_actors(),
                            tomato_rating=self.get_tomato_rating()
                            )
                self.table.insert(data)
            else:
                print(self.movie_name + ' Not Found')


class ForTv:
    def __init__(self, series_name, table):
        self.series_name = series_name.split(' - ')[0]
        self.table = table
    json_file = {}
    status = True

    def get_json(self):
        show_name = self.series_name.replace('&', '%26')
        show_name = show_name.split('(')[0]
        if show_name == 'Agents of S.H.I.E.L.D':
            show_name = 'Agents of S.H.I.E.L.D.'
        json_file = requests.get('http://www.omdbapi.com/?t=' + show_name + '&type=series')
        self.json_file = json_file.json()
        return json_file.json()

    def get_year(self):
        year = self.json_file['Year']
        return year

    def get_runtime(self):
        runtime = self.json_file['Runtime']
        return runtime

    def get_show_genre(self):
        show_genre = self.json_file['Genre']
        return show_genre

    def get_show_plot(self):
        show_plot = self.json_file['Plot']
        return show_plot

    def get_actors(self):
        actors = self.json_file['Actors']
        return actors

    def get_imdb_rating(self):
        rating = self.json_file['imdbRating']
        return rating

    def get_imdb_id(self):
        show_id = self.json_file['imdbID']
        return show_id

    def get_length(self):
        length = len(self.table) + 1
        return length

    def writer(self):
        series_name = self.series_name
        self.get_json()
        data = dict(id=self.get_length(),
                    release_year=self.get_year(),
                    runtime=self.get_runtime(),
                    genre=self.get_show_genre(),
                    plot=self.get_show_plot(),
                    actors=self.get_actors(),
                    rating=self.get_imdb_rating(),
                    imDB_ID=self.get_imdb_id(),
                    show_name=series_name,
                    )
        self.table.insert(data)
