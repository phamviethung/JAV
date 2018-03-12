from bs4 import BeautifulSoup
import urllib2


base_url = 'http://javmodel.com/jav/homepages.php'
base_page = urllib2.urlopen(base_url)
base_soup = BeautifulSoup(base_page, 'lxml')

# Find max_model_page (35)
if len(base_soup.find('ul', {'class': 'pagination pagination-2 dark'}).find_all('li')) == 1:
    max_model_page = 1
else:
    max_model_page = int(base_soup.find('ul', {'class': 'pagination pagination-2 dark'}).find_all('li')[-2].text)

# Create list of all models
models = []

for i in range(1, max_model_page + 1):
    base_url = 'http://javmodel.com/jav/homepages.php?page=' + str(i)
    print base_url
    base_page = urllib2.urlopen(base_url)
    base_soup = BeautifulSoup(base_page, 'lxml')

    for i in base_soup.find_all('div', {'class': 'col-sm-6 col-md-3 el mb40'}):
        model_overview_dict = {}
        model_overview_dict['name'] = i.find('img')['alt']
        model_overview_dict['src'] = i.find('img')['src']
        model_overview_dict['href'] = i.find('a')['href']
        model_overview_dict['tag'] = i.find('p', {'class': 'text'}).text
        models.append(model_overview_dict)

# Create list of all movies of each model
details = []

for model in models:
    model_url = 'http://javmodel.com' + model['href']
    print model_url
    model_page = urllib2.urlopen(model_url)
    model_soup = BeautifulSoup(model_page, 'lxml')
    if len(model_soup.find('ul', {'class': 'pagination pagination-2 dark'}).find_all('li')) == 1:
        max_movie_page = 1
    else:
        max_movie_page = int(model_soup.find('ul', {'class': 'pagination pagination-2 dark'}).find_all('li')[-2].text)


    model_dict = {}
    info = []
    for i in range(len(model_soup.find('ul', {'class': 'unstyled-list list-medium'}).find_all('li'))):
        info.append(model_soup.find('ul', {'class': 'unstyled-list list-medium'}).find_all('li')[i].text)

    model_dict['info'] = info

    movies = []
    for i in range(1, max_movie_page + 1):
        model_url = 'http://javmodel.com' + model['href'] + '?page=' + str(i) + '&num=3'
        print model_url
        model_page = urllib2.urlopen(model_url)
        model_soup = BeautifulSoup(model_page, 'lxml')

        for i in model_soup.find_all('div', {'class': 'row blog-item'}):

            movie_dict = {}

            movie_code = i.find('img')['alt']
            movie_poster = i.find('img')['src']
            movie_title = i.find('div', {'class': 'col-sm-12 col-md-8 wow fadeInRight'}).find('a').text
            movie_info = []
            for j in range(len(i.find('div', {'class': 'col-sm-12 col-md-8 wow fadeInRight'}).find('ul').find_all('li'))):
                movie_info.append(
                    i.find('div', {'class': 'col-sm-12 col-md-8 wow fadeInRight'}).find('ul').find_all('li')[j].text)

            movie_dict['movie_code'] = movie_code
            movie_dict['movie_poster'] = movie_poster
            movie_dict['movie_title'] = movie_title
            movie_dict['movie_info'] = movie_info
            movies.append(movie_dict)

        model_dict['movies'] = movies
    details.append(model_dict)

print len(details)

import json
with open('models.txt', 'w') as outfile:
    json.dump(models, outfile)
with open('details.txt', 'w') as outfile:
    json.dump(details, outfile)


