import dataset
db = dataset.connect('sqlite:///C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db')
table = db['Movies']


def find_path():
    path_list = []
    for paths in table['path']:
        path_list.append(paths['path'])
    movie = 'E:\Movies\+1 (2013)\+1.mp4'
    if movie not in path_list:
        print('false')
    elif movie in path_list:
        print('true')

if __name__ == '__main__':
    find_path()
