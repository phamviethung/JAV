import os
import urllib
import ast
read_models = open('models.txt','r')
list_models = ast.literal_eval(read_models.read())
read_details = open('details.txt','r')
list_details = ast.literal_eval(read_details.read())

for i in range(774, len(list_models)):
    base_path = list_models[i]['name']
    print base_path
    profile_path = base_path + '/Profile'
    profile_url = list_models[i]['src']
    os.makedirs(profile_path)
    urllib.urlretrieve(profile_url, os.path.join(profile_path, profile_url.split('/')[-1]))

    poster_path = base_path + '/Posters'
    os.makedirs(poster_path)
    for movie in list_details[i]['movies']:
        poster_url = movie['movie_poster']
        urllib.urlretrieve(poster_url, os.path.join(poster_path, poster_url.split('/')[-1]))


