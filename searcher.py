from imdbpie import Imdb
import dataset
imdb = Imdb()
db = dataset.connect('sqlite:///C:\\Users\Tom\\PycharmProjects\\imdb_search\\video_list.db')
db_name = 'Movies'
table = db[db_name]

for x in range(100, 369):
    movie_name = table.find_one(id=x)['movie_name']
    movie = imdb.search_for_title(movie_name)
    movie_id = movie[0]['imdb_id']
    data = dict(id=x, imdb_id=movie_id)
    table.update(data, ['id'])
