import dataset
from urllib.parse import quote_plus
dj_db_file = 'C:\\Users\\Tom\\Documents\\Python_Projects\\django_website\\db.sqlite3'
db_file = 'C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db'
db = dataset.connect('sqlite:///{}'.format(dj_db_file))

table = db['movies_moviedb']


def url_phrasing_test():
    movie_name = quote_plus('+1')
    movie_year = '2013'
    url = 'http://www.omdbapi.com/?t={0}&y={1}&plot=short&r=json&tomatoes=true'.format(movie_name, movie_year)
    print(url)

if __name__ == '__main__':
    url_phrasing_test()
