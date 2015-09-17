import modules

movie_path = 'D:\Movies\Teen Lust (2015)\Teen Lust.mp4'
movie_name = 'Teen Lust'
statement = modules.ForMovies(movie_name, movie_path, None).get_response()
print(statement)
if statement == 'True':
    print('Found')
elif statement == 'False':
    print('Not Found')
else:
    print('Done messed up')
