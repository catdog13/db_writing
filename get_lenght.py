import subprocess
import dataset
db = dataset.connect('sqlite:///C:\\Users\Tom\\PycharmProjects\\db_writing\\video_list.db')
db_name = 'Movies'
table = db[db_name]


def get_length(filename):
    result = subprocess.Popen(["ffprobe", filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for x in result.stdout.readlines():
        if rb"Duration" in x:
            movie_length = (x[12:23])
            return str(movie_length)[2:-4]


def write_to_db():
    for x in range(51, 369):
        movie_name = table.find_one(id=x)['path']
        movie_length = get_length(movie_name)
        data = dict(id=x, length=movie_length)
        table.update(data, ['id'])

if __name__ == '__main__':
    write_to_db()
