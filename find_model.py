# coding: utf-8
import ast
read_models = open('models.txt','r')
list_models = ast.literal_eval(read_models.read())


'''
count = 0
for model in list_models:
    if model['name'] == 'Mion Sonoda':
        break
    else:
        count += 1

print count
'''

print list_models[560]
