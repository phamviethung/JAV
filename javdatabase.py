from bs4 import BeautifulSoup
import urllib2

base_url = 'http://www.javdatabase.com/idols'
base_page = urllib2.urlopen(base_url)
base_soup = BeautifulSoup(base_page, 'lxml')
alphabets = []
for i in base_soup.find_all('div', {'class': 'alphabet'}):
    alphabets.append(i.text)
#print alphabets

page_urls = []
for i in alphabets:
    if i == 'A':
        page_urls.append(base_url)
    else:
        page_urls.append(base_url + '-' + i)

models = []

for page_url in page_urls:
    page = urllib2.urlopen(page_url)
    soup = BeautifulSoup(page, 'lxml')

    for i in soup.find_all('div', {'class': 'searchitem'}):
        model_overview_dict = {}
        model_overview_dict['name'] = i.find('a').text
        model_overview_dict['src'] = i.find('a')['href']


        movies = []
        each_model_page = urllib2.urlopen(i.find('a')['href'])
        #print i.find('a')['href']
        each_model_soup = BeautifulSoup(each_model_page, 'lxml')
        for j in each_model_soup.find_all('div', {'class': 'featured-thumbnail'}):
            each_poster_page = urllib2.urlopen(j.find('a')['href'])
            #print j.find('a')['href']
            each_poster_soup = BeautifulSoup(each_poster_page, 'lxml')
            for k in each_poster_soup.find_all('div', {'class': 'cover'}):
                movie_dict = {}
                each_poster_page = urllib2.urlopen(k.find('img')['src'])
                #print k.find('img')['src']
            movie_title = each_poster_soup.find_all('div', {'class': 'single_post'})[0].find_all('h3')[0].text
            movie_dict['movie_title'] = movie_title
            movie_poster = each_poster_soup.find_all('div', {'class': 'cover'})[0].find('img')['src']
            movie_dict['movie_poster'] = movie_poster
            movie_info = []
            for h in each_poster_soup.find_all('div', {'class': 'movieinfo'})[0].find('ul').find_all('li'):
                movie_info.append(h.text)
            movie_dict['movie_info'] = movie_info
            movies.append(movie_dict)
        model_overview_dict['movies'] = movies
        models.append(model_overview_dict)
        #print models

import json
with open('jav_db.txt', 'w') as outfile:
    json.dump(models, outfile)