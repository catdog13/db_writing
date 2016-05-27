import dataset
db = dataset.connect('sqlite:///C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db')
table = db['Movies']


def status_update():
    movie_name = input('Name of Movie: ')
    movie = table.find_one(movie_name=movie_name)
    movie_id = movie['id']
    status_current = movie['status']
    data = dict()
    if status_current == 'Unwatched':
        data = dict(id=movie_id, status='Watched')
    elif status_current == 'Watched':
        data = dict(id=movie_id, status='Unwatched')
    else:
        print("it didn't work")
    table.update(data, ['id'])

if __name__ == '__main__':
    while True:
        status_update()
