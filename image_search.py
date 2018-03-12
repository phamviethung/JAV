import os
import urllib
import ast
read_models = open('models.txt','r')
list_models = ast.literal_eval(read_models.read())

#print list_models[0]

from bs4 import BeautifulSoup
import urllib2
#from sightengine.client import SightengineClient
import json

headers = {}
#headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
# headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
# pure_keyword = keywords[j].replace(' ','%20')

headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"

#client = SightengineClient("46210461", "qouMN5MTJfcTxZND4qSV")

for i in range(0, 3):

    base_path = list_models[i]['name']
    print base_path
    image_path = base_path + '/Images'
    os.makedirs(image_path)

    pure_keyword = list_models[i]['name'].replace(' ', '%20')
    url = 'https://www.google.com/search?q=' + pure_keyword + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
    req = urllib2.Request(url, headers=headers)
    resp = urllib2.urlopen(req)

    soup = BeautifulSoup(resp, 'lxml')



    #f = open(list_models[i]['name'] + '.txt', 'w')
    count = 0

    for j in soup.find_all('div', {'class': 'rg_meta notranslate'}):
        link_in = (json.loads(j.text)['ou'])
        #print link_in
        #f.write(link_in)
        #f.write('\n')


        '''
        check = client.check('nudity').set_url(link_in)
        if check['status'] == 'success':
            #print check['nudity']['raw']
            f.write(str(check['nudity']['raw']))
            f.write('\n')
            count += 1
        else:
            #print check['error']
            f.write(str(check['error']))
            f.write('\n')
        '''

        try:
            urllib.urlretrieve(link_in, os.path.join(image_path, link_in.split('/')[-1]))
            count+=1
        except Exception as e:
            print e

    print count
    #f.close()