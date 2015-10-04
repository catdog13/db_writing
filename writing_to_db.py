import os
import dataset
import time
import modules
db = dataset.connect('sqlite:///C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db')


def folder_crawler(path_to_craw):
    start_time = time.time()
    db_name = path_to_craw[3:]
    print(db_name + ' Starting')

    def file_walker():
        if path_to_craw.endswith('Movies'):
            table = db[db_name]
            for root, subdir, files in os.walk(path_to_craw):
                for file in files:
                    if file.endswith('.mp4'):
                        full_path = os.path.join(root, file)
                        modules.ForMovies(file[:-4], full_path, table).writer()
        elif path_to_craw.endswith('TV'):
            db[db_name].drop()
            table = db[db_name]
            for shows in os.scandir(path_to_craw):
                modules.ForTv(shows.name, table).writer()

    file_walker()
    print(db_name + ' Was Done In ' + str(round((time.time() - start_time), 2)) + ' seconds')


if __name__ == '__main__':
    folder_crawler(r'D:\Movies')
    # folder_crawler(r'D:\TV')
