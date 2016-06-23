import os
import dataset
import time
import modules
db_file = 'C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db'
db = dataset.connect('sqlite:///{}'.format(db_file))


def folder_crawler(path_to_craw):
    start_time = time.time()
    db_name = path_to_craw[3:]
    print(db_name + ' Starting')

    def file_walker():
        if path_to_craw.endswith('Movies'):
            table = db[db_name]
            path_list = []
            for paths in table['path']:
                path_list.append(paths['path'])
            for root, subdir, files in os.walk(path_to_craw):
                for file in files:
                    if file.endswith('.mp4'):
                        full_path = os.path.join(root, file)
                        file_name = os.path.splitext(file)[0]
                        modules.ForMovies(file_name, full_path, table, path_list).writer()
        elif path_to_craw.endswith('TV'):
            db[db_name].drop()
            table = db[db_name]
            for shows in os.scandir(path_to_craw):
                modules.ForTv(shows.name, table).writer()

    file_walker()
    end_time = str(round((time.time() - start_time), 2))
    print('{0} Was done in {1} seconds'.format(db_name, end_time))


if __name__ == '__main__':
    folder_crawler(r'E:\Movies')
    # folder_crawler(r'D:\TV')
