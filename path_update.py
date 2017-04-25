#!/usr/bin/env python3
import dataset
import os

# db_file = 'I:\\MovieTable\\MovieTable.sqlite3'
db_file = '/media/tom/arrrrrrrrr/!..scripts/db_files/path_date.db'
db = dataset.connect('sqlite:///{}'.format(db_file))
# table = db['old_movies_moviedb']
table = db['moviedb']


def run_update(row_id):
    old_movie_path = table.find_one(id=row_id)['movie_path']
    new_path = change_path(old_movie_path)
    update(row_id, new_path)


# 'E:\Movies\10 Years (2011)\10 Years.mp4'
# '/media/tom/arrrrrrrrr/Movies/10 Years (2011)/10 Years.mp4'

def change_path(old_path):
    new_base = '/media/tom/arrrrrrrrr/'
    base_path = old_path[3:].replace('\\', '/')
    new_path = os.path.join(new_base, base_path)
    return new_path


def update(x, movie_path):
    data = dict(id=x,
                movie_path=movie_path,
                )
    table.update(data, ['id'])

if __name__ == '__main__':
    # change_path('E:\\Movies\\10 Years (2011)\\10 Years.mp4')

    # lower = 701
    # upper = 746

    # for row_id in range(lower, upper):
        # run_update(row_id)
        
        
    run_update(746)
