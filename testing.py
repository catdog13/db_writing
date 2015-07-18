import modules

path = 'E:\Movies\300 Rise of an Empire (2014)\300 Rise of an Empire.mp4'
movie_name = '300: Rise of an Empire'
json_file = modules.get_json(movie_name, modules.get_movie_year(path))
output = modules.get_movie_id(json_file)
print(output)
