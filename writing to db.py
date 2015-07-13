import os
import dataset
import time
# db = dataset.connect('sqlite:///C:\\Users\\Tom\\Documents\\GitHub\\un-watched_status\\test files\\video_list.db')
db = dataset.connect('sqlite:///C:\\Users\Tom\\video_list.db')


def folder_crawler(path_to_craw, unwatched, drop):
    start_time = time.time()
    db_name = path_to_craw[3:]
    print(db_name + " Starting")
    if drop:
        db[db_name].drop()
    table = db[db_name]

    def file_writer(dir_path, file_name, status):
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            file_size_bytes = file_size/1073741824
            if status:
                view_status = "Unwatched"
            else:
                view_status = ""

            if table.find_one(filename=file_name) is None:
                table.insert(dict(filename=file_name, path=dir_path,
                                  file_size=(str(round(file_size_bytes, 2)) + ' GB'), status=view_status))

    def start_file_op():
            folder = path_to_craw
            folder = folder.replace('/', '\\')
            file_type = '.mp4'
            file_type = file_type.strip(".")
            for dir_path, dir_names, file_names in os.walk(folder):
                for filename in [f for f in file_names if f.endswith("." + file_type)]:
                    file_writer(dir_path, filename, unwatched)
    start_file_op()
    print(db_name + " Was Done In " + str(round((time.time() - start_time), 2)) + " seconds")

folder_crawler(r"E:\Movies", True, False)
folder_crawler(r"E:\TV", False, False)
input(' ')
