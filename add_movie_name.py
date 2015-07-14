import dataset

db = dataset.connect('sqlite:///C:\\Users\Tom\\PycharmProjects\\un-watched_status\\video_list.db')

db_name = 'Movies'
table = db[db_name]
with_mp4 = table.find_one(id=1)
print(with_mp4)
data = dict(movie_name='10 Years')
table.update(data, 1)
print(with_mp4)
