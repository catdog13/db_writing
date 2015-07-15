import subprocess


def get_length(filename):
    result = subprocess.Popen(["ffprobe", filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for x in result.stdout.readlines():
        if rb"Duration" in x:
            movie_length = (x[12:23])
            return str(movie_length)[2:-4]

print(get_length(r'E:\\Movies\\5 to 7 (2014)\\5 to 7.mp4'))
