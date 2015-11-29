import dataset
db = dataset.connect('sqlite:///C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db')


def path_changer():
    table = db['Movies']
    for x in range(1, 467):
        old_path = table.find_one(id=x)['path']
        new_path = old_path.replace('D:\\', 'E:\\')
        data = dict(id=x,
                    path=new_path)
        table.update(data, ['id'])


if __name__ == '__main__':
    path_changer()
