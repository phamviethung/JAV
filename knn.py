import ast
read_models = open('models.txt','r')
list_models = ast.literal_eval(read_models.read())
read_details = open('details.txt','r')
list_details = ast.literal_eval(read_details.read())

Year = []
Breast = []
Waist = []
Hips = []
Height = []
for i in list_details:
    if i['info'][0].split(':')[1] == ' ':
        Year.append(float('nan'))
    else:
        Year.append(int(i['info'][0].split('/')[-1]))

    if i['info'][2].split(':')[1] == '  cm':
        Breast.append(float('nan'))
    else:
        Breast.append(int(i['info'][2].split(':')[-1].split()[0]))

    if i['info'][3].split(':')[1] == '  cm':
        Waist.append(float('nan'))
    else:
        Waist.append(int(i['info'][3].split(':')[-1].split()[0]))

    if i['info'][4].split(':')[1] == '  cm':
        Hips.append(float('nan'))
    else:
        Hips.append(int(i['info'][4].split(':')[-1].split()[0]))

    if i['info'][5].split(':')[1] == '  cm':
        Height.append(float('nan'))
    else:
        Height.append(int(i['info'][5].split(':')[-1].split()[0]))

# find unique element in a list
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

tag_list = []
for i in list_models:
    tag_list += i['tag'].replace(',\u00a0', '').split('\n')

tag_list = unique_list(tag_list)
tag_list.remove('')

import pandas as pd
from pandas import DataFrame
df = DataFrame(columns=tag_list)

# list name
name = []
for i in list_models:
    name.append(i['name'])
df['Name'] = name

# add tag
for i in range(0, len(list_models)):
    tags = list_models[i]['tag'].replace(',\u00a0', '').split('\n')
    del tags[-1]
    for j in tags:
        df.loc[i][j] = 1

# add Year, Breast, Waist, Hips, Height
df['Year'] = Year
df['Breast'] = Breast
df['Waist'] = Waist
df['Hips'] = Hips
df['Height'] = Height

# Fill N/A value and Normalizing between [0, 1]
from sklearn import preprocessing
df2 = df[['Year', 'Breast', 'Waist', 'Hips', 'Height'] + tag_list].fillna(0)
x = df2.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df2 = pd.DataFrame(x_scaled)

# Cosine similarity
from sklearn.metrics.pairwise import cosine_similarity
cosine_list = cosine_similarity(df2)
print cosine_list
''''
file = open('cosine.txt', 'w')
for i in cosine_list:
  file.write("%s\n" % i)

file.close()
'''

