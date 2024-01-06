import json
import numpy as np
 
f = open('C:/work-shop/Inputdata/level0.json')
 

data = json.load(f)

n = data['n_neighbourhoods']
l = []
for i in range(0,n):
    l.append(data['neighbourhoods']['n'+str(i)]['distances'])



# for i in data['neighbourhoods']:
#     print(i)
print(l)



f.close()