# code by Sanjana R (21pd31)

import json
import numpy as np
 
f = open('C:/work-shop/Inputdata/level1a.json')
 

data = json.load(f)

n = data['n_neighbourhoods']

dist = []
dist.append([0])
res = data['restaurants']['r0']['neighbourhood_distance']
dist[0].extend(res)
for i in range(0,n):
    dist.append([res[i]])
    dist[i+1].extend(data['neighbourhoods']['n'+str(i)]['distances'])


for i in dist:
    print(i)
order_quantity = []
for i in range(0,n):
    order_quantity.append(data['neighbourhoods']['n'+str(i)]['order_quantity'])
print(order_quantity)
print(sum(order_quantity))

capacity = data['vehicles']['v0']['capacity']
print(capacity)

ans  = []
def knapSack(W, wt, val, n): 
    if n == 0 or W == 0: 
        return 0
  
    if (wt[n-1] > W): 
        return knapSack(W, wt, val, n-1) 
  
    else: 
        a = val[n-1] + knapSack(W-wt[n-1], wt, dist[n-1], n-1)
        b = knapSack(W, wt, val, n-1)
        if (a>b):
            l.append()
        return max( 
            val[n-1] + knapSack( 
                W-wt[n-1], wt, dist[n-1], n-1), 
            knapSack(W, wt, val, n-1)) 
  
  
profit = dist[0]
weight = order_quantity
W = capacity
print(knapSack(W, weight, profit, n)) 