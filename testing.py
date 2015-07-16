import dataset
db = dataset.connect('sqlite:///C:\\Users\Tom\\PycharmProjects\\db_writing\\db_files\\video_list.db')
db_name = 'Movies'
table = db[db_name]

for x in range(1, 2):
    movie_name = table.find_one(id=x)['movie_name']
    data = dict(id=x, movie_name=movie_name)
    table.update(data, ['id'])
