import dataset

db = dataset.connect('sqlite:///C:\\Users\Tom\\PycharmProjects\\db_writing\\video_list.db')

db_name = 'Movies'
table = db[db_name]
for x in range(360, 369):
    with_mp4 = table.find_one(id=x)['filename']
    without_mp4 = with_mp4[:-4]
    data = dict(id=x, movie_name=without_mp4)
    table.update(data, ['id'])
