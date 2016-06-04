import dataset
from urllib.parse import quote_plus
db = dataset.connect('sqlite:///C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db')
table = db['Movies']


def url_phrasing_test():
    movie_name = quote_plus('+1')
    movie_year = '2013'
    url = 'http://www.omdbapi.com/?t={0}&y={1}&plot=short&r=json&tomatoes=true'.format(movie_name, movie_year)
    print(url)

if __name__ == '__main__':
    url_phrasing_test()
