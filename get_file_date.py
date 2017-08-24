#!/usr/bin/env python3
import dataset
import os
# db_file = 'H:\\Projects\\db_writing\\db_files\\path_date.db'
db_file = '/media/tom/32GB/Projects/db_writing/db_files/path_date.db'
db = dataset.connect('sqlite:///{}'.format(db_file))
table = db['moviedb']


def folder_crawler(path_to_craw):
    db.begin()
    for root, subdir, files in os.walk(path_to_craw):
        for file in files:
            if file.endswith('.mp4'):
                full_path = os.path.join(root, file)
                creation_time = os.path.getctime(full_path)

                data = dict(movie_path=full_path,
                            creat_date=creation_time)
                table.insert(data)
    db.commit()

if __name__ == '__main__':
    # folder_crawler(r'I:\Movies')
    folder_crawler(r'/media/tom/arrrrrrrrr/Movies')
