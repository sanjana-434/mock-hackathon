# code by Sanjana R (21pd31)

import json
import numpy as np
 
f = open('C:/work-shop/Inputdata/level1a.json')
 

data = json.load(f)

n = data['n_neighbourhoods']

dist = []
for i in range(0,n):
    dist.append(data['neighbourhoods']['n'+str(i)]['distances'])
print(dist)
order_quantity = []
for i in range(0,n):
    order_quantity.append(data['neighbourhoods']['n'+str(i)]['order_quantity'])
print(order_quantity)