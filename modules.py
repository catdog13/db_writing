import os
import requests


class ForMovies:
    def __init__(self, movie_name, movie_path, table):
        self.movie_name = movie_name
        self.movie_path = movie_path
        self.table = table
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
        movie_name = self.movie_name.replace('&', '%26')
        json_file = requests.get('http://www.omdbapi.com/?t=' + movie_name + '&y=' +
                                 self.get_movie_year() + '&plot=short&r=json&tomatoes=true')
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
        return rating

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
        if self.table.find_one(path=self.movie_path) is None:
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
    def __init__(self, series_name, show_path, table, file_name):
        self.series_name = series_name.split(' - ')[0]
        self.show_path = show_path
        self.table = table
        self.file_name = file_name
    json_file = {}
    status = True

    def get_view_status(self):
        if self.status:
            view_status = 'Unwatched'
        else:
            view_status = 'Watched'
        return view_status

    def get_show_size(self):
        file_size = os.path.getsize(self.show_path)
        file_size_bytes = file_size / 1073741824
        return str(round(file_size_bytes, 2)) + ' GB'

    def get_season(self):
        season_episode = self.file_name.split(' - ')[1]
        season = season_episode[1:-3]
        return season

    def get_episode(self):
        season_episode = self.file_name.split(' - ')[1]
        episode = season_episode[4:]
        return episode

    def get_json(self):
        show_name = self.series_name.replace('&', '%26')
        json_file = requests.get('http://www.omdbapi.com/?t=' + show_name +
                                 '&Season=' + self.get_season() + '&Episode=' + self.get_episode())
        self.json_file = json_file.json()
        return json_file.json()

    def get_runtime(self):
        runtime = self.json_file['Runtime']
        return runtime

    def get_series_id(self):
        series_id = self.json_file['seriesID']
        return series_id

    def get_episode_id(self):
        episode_id = self.json_file['imdbID']
        return episode_id

    def get_show_title(self):
        show_title = self.json_file['Title']
        return show_title

    def get_show_genre(self):
        show_genre = self.json_file['Genre']
        return show_genre

    def get_episode_release_date(self):
        episode_release = self.json_file['Released']
        release_year = episode_release[-4:]
        release_month = episode_release[3:][:4]
        release_day = episode_release[:2]
        episode_release_date = release_year + ' ' + release_month + ' ' + release_day
        return episode_release_date

    def get_show_plot(self):
        show_plot = self.json_file['Plot']
        return show_plot

    def get_actors(self):
        actors = self.json_file['Actors']
        return actors

    def get_length(self):
        length = len(self.table) + 1
        return length

    def update(self, x):
        series_name = self.series_name
        self.get_json()
        data = dict(id=x,
                    imdb_series_id=self.get_series_id(),
                    imdb_episode_id=self.get_episode_id(),
                    title=self.get_show_title(),
                    file_size=self.get_show_size(),
                    runtime=self.get_runtime(),
                    genre=self.get_show_genre(),
                    release_date=self.get_episode_release_date(),
                    plot=self.get_show_plot(),
                    show_name=series_name,
                    path=self.show_path,
                    actors=self.get_actors(),
                    episode=self.get_episode(),
                    season=self.get_season(),
                    )
        self.table.update(data, ['id'])

    def writer(self):
        if self.table.find_one(path=self.show_path) is None:
            series_name = self.series_name
            self.get_json()
            data = dict(id=self.get_length(),
                        imdb_series_id=self.get_series_id(),
                        imdb_episode_id=self.get_episode_id(),
                        title=self.get_show_title(),
                        file_size=self.get_show_size(),
                        runtime=self.get_runtime(),
                        genre=self.get_show_genre(),
                        release_date=self.get_episode_release_date(),
                        plot=self.get_show_plot(),
                        show_name=series_name,
                        path=self.show_path,
                        actors=self.get_actors(),
                        episode=self.get_episode(),
                        season=self.get_season(),
                        )
            self.table.insert(data)

    def writer_simple(self):
        if self.table.find_one(path=self.show_path) is None:
            show_name = self.file_name
            self.get_json()
            data = dict(id=self.get_length(),
                        file_size=self.get_show_size(),
                        movie_name=show_name,
                        path=self.show_path,
                        )
            self.table.insert(data)
