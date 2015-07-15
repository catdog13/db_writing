import dataset
db = dataset.connect('sqlite:///C:\\Users\Tom\\PycharmProjects\\db_writing\\video_list.db')
db_name = 'Movies'
table = db[db_name]


def merger():
    for x in range(101, 369):
        old_path = table.find_one(id=x)['path']
        file_name = table.find_one(id=x)['filename']
        new_path = old_path + '\\' + file_name
        data = dict(id=x, path=new_path)
        table.update(data, ['id'])

if __name__ == '__main__':
    merger()
