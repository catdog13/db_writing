import dataset

dj_db_file = 'C:\\Users\\Tom\\Documents\\Python_Projects\\django_website\\db.sqlite3'
db_file = 'C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db'
db = dataset.connect('sqlite:///{}'.format(dj_db_file))

table = db['movies_moviedb']


def status_update():
    movie_name = input('Name of Movie: ')
    movie = table.find_one(movie_name=movie_name)
    movie_id = movie['id']
    status_current = movie['status']
    data = dict()
    new_status = ''
    if status_current == 'Unwatched':
        new_status = 'is now marked Watched'
        data = dict(id=movie_id, status='Watched')
    elif status_current == 'Watched':
        new_status = 'is now marked Unwatched'
        data = dict(id=movie_id, status='Unwatched')
    table.update(data, ['id'])
    print('{0} {1}'.format(movie_name, new_status))


if __name__ == '__main__':
    while True:
        status_update()
