import os
import dataset
import time
import modules
db = dataset.connect('sqlite:///C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db')


def folder_crawler(path_to_craw):
    start_time = time.time()
    db_name = path_to_craw[3:]
    print(db_name + ' Starting')
    table = db[db_name]

    def file_walker():
        for root, subdir, files in os.walk(path_to_craw):
            for file in files:
                if file.endswith('.mp4'):
                    full_path = os.path.join(root, file)
                    modules.ForMovies(file[:-4], full_path, table).writer()

    file_walker()
    print(db_name + ' Was Done In ' + str(round((time.time() - start_time), 2)) + ' seconds')


if __name__ == '__main__':
    folder_crawler(r'D:\Movies')
